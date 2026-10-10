"""The proof swarm.

``Swarm.prove`` runs provers in parallel, rescues truncated or thin write-ups, checks each
candidate with a brute-force "lab" script and several adversarial verifiers, repairs the
most promising candidates, and returns the best one together with how it was graded.
``Swarm.solve`` is the cheaper answer mode: many solvers (optionally program-aided) vote on
a final ``\\boxed{}`` answer, stopping as soon as the vote is mathematically decided.

Every stage maps to a failure mode observed when MiniCPM5-2B-Math was evaluated
single-shot; see docs/how-it-works.md.
"""

from __future__ import annotations

import asyncio
import re
import time
import zlib
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Awaitable, Dict, Iterable, List, Optional, Tuple

from . import prompts
from .client import Backend, BackendError, Generation
from .events import Tracker
from .parsing import (
    answers_match,
    count_critical,
    extract_code,
    extract_issues,
    last_boxed,
    last_line,
    normalize_answer,
    parse_grade,
    split_reasoning,
    trim_middle,
)
from .sandbox import available_modules, run_python
from .template import THINK_CLOSE, forced_finish_prompt
from .trace import Recorder


@dataclass
class SwarmConfig:
    # proof mode
    provers: int = 8
    verifiers: int = 3
    rounds: int = 2
    refine_top: int = 2
    accept_grade: int = 6
    staged_verify: bool = True
    lab: bool = True
    scribe: str = "auto"  # auto | always | never
    strategies: bool = True
    # answer mode
    solvers: int = 8
    coders: int = 0
    # max completion tokens per call
    prover_tokens: int = 32768
    solver_tokens: int = 32768
    verifier_tokens: int = 16384
    refiner_tokens: int = 32768
    scribe_tokens: int = 16384
    lab_tokens: int = 8192
    finish_tokens: int = 6144
    notes_chars: int = 60000  # reasoning handed to scribes/refiners (~18K tokens)
    budget: Optional[int] = None  # soft cap on completion tokens: no new calls once spent, running calls finish
    # sampling (the settings the model was evaluated with)
    temperature: float = 0.9
    top_p: float = 0.95
    seed: Optional[int] = None
    # behaviour
    force_finish: bool = True
    early_stop: bool = True
    exec_code: bool = True
    exec_timeout: float = 20.0


PROFILES: Dict[str, Dict[str, Any]] = {
    # laptop demo: a few agents, short budgets
    "quick": dict(provers=4, verifiers=2, rounds=1, refine_top=1, solvers=4, prover_tokens=16384,
                  solver_tokens=16384, verifier_tokens=8192, refiner_tokens=16384, scribe_tokens=8192,
                  lab_tokens=6144, notes_chars=20000),
    "standard": dict(),
    # one GPU (e.g. a 24 GB RTX 4090 with vLLM)
    "heavy": dict(provers=16, verifiers=4, rounds=3, refine_top=3, solvers=16, coders=4, prover_tokens=65536,
                  solver_tokens=65536, verifier_tokens=24576, refiner_tokens=65536, scribe_tokens=16384),
    # a node of GPUs; the long budgets match what Putnam-level problems needed in testing
    "swarm": dict(provers=64, verifiers=4, rounds=4, refine_top=8, solvers=64, coders=16, prover_tokens=98304,
                  solver_tokens=98304, verifier_tokens=32768, refiner_tokens=98304, scribe_tokens=24576),
}


def config_for(profile: str = "standard", **overrides: Any) -> SwarmConfig:
    if profile not in PROFILES:
        raise ValueError(f"unknown profile {profile!r}; choose from {', '.join(PROFILES)}")
    values = dict(PROFILES[profile])
    values.update({k: v for k, v in overrides.items() if v is not None})
    return SwarmConfig(**values)


@dataclass
class Candidate:
    id: str
    text: str
    origin: str  # prover | scribe | refiner
    parent: Optional[str] = None
    notes: str = ""  # reasoning trace behind the text
    finish: Optional[str] = None
    lab_output: Optional[str] = None
    grades: List[int] = field(default_factory=list)
    reports: List[str] = field(default_factory=list)
    consensus: bool = True  # set to False when the candidate is not in the largest final-answer group

    @property
    def lab_clean(self) -> bool:
        """The brute-force check ran, printed at least one PASS and no FAIL."""
        out = self.lab_output or ""
        return bool(re.search(r"^\s*PASS", out, re.M)) and not re.search(r"^\s*FAIL", out, re.M)

    @property
    def mean_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else -1.0

    @property
    def min_grade(self) -> int:
        return min(self.grades) if self.grades else -1

    def summary(self) -> Dict[str, Any]:
        return {
            "id": self.id, "origin": self.origin, "parent": self.parent, "finish": self.finish,
            "grades": self.grades, "mean_grade": round(self.mean_grade, 2), "chars": len(self.text),
            "consensus": self.consensus, "lab_clean": self.lab_clean,
            "issues": [i for r in self.reports for i in extract_issues(r, limit=6)][:12],
            "lab": self.lab_output,
        }


@dataclass
class ProofResult:
    problem: str
    status: str  # accepted | unverified | failed
    proof: str
    best: Optional[Candidate]
    candidates: List[Candidate]
    tokens: int
    seconds: float
    calls: int

    def to_dict(self) -> Dict[str, Any]:
        return {
            "mode": "prove", "status": self.status, "best": self.best.id if self.best else None,
            "grades": self.best.grades if self.best else [], "proof": self.proof, "tokens": self.tokens,
            "seconds": round(self.seconds, 1), "calls": self.calls,
            "candidates": [c.summary() for c in self.candidates],
        }


@dataclass
class AnswerResult:
    problem: str
    answer: Optional[str]
    votes: List[Tuple[str, int]]
    samples: List[Dict[str, Any]]
    tokens: int
    seconds: float
    calls: int
    decided_early: bool

    @property
    def agreement(self) -> float:
        counted = sum(n for _, n in self.votes)
        return self.votes[0][1] / counted if counted else 0.0

    @property
    def tied(self) -> bool:
        """True when the top answers have equal votes; the earliest-finished one is then reported."""
        return len(self.votes) > 1 and self.votes[0][1] == self.votes[1][1]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "mode": "solve", "answer": self.answer, "votes": self.votes, "agreement": round(self.agreement, 3),
            "tied": self.tied, "decided_early": self.decided_early, "tokens": self.tokens,
            "seconds": round(self.seconds, 1), "calls": self.calls, "samples": self.samples,
        }


_ANSWER_LABEL = re.compile(r"^(?:final\s+)?answer\s*(?:is)?\s*[:=]?\s*", re.I)


class Swarm:
    def __init__(
        self,
        backend: Backend,
        config: Optional[SwarmConfig] = None,
        *,
        verifier: Optional[Backend] = None,
        tracker: Optional[Tracker] = None,
        recorder: Optional[Recorder] = None,
    ):
        self.backend = backend
        self.verifier_backend = verifier or backend
        self.config = config or SwarmConfig()
        self.tracker = tracker or Tracker()
        self.recorder = recorder or Recorder()
        self.tokens = 0
        self.calls = 0
        self.errors: List[BaseException] = []
        self._modules = available_modules() if self.config.exec_code else []

    # ------------------------------------------------------------------ plumbing

    def _seed(self, key: Any) -> Optional[int]:
        if self.config.seed is None:
            return None
        offset = key if isinstance(key, int) else zlib.crc32(str(key).encode()) % 100_000
        return self.config.seed + offset

    def _budget_left(self) -> bool:
        return self.config.budget is None or self.tokens < self.config.budget

    async def _call(
        self,
        agent_id: str,
        role: str,
        messages: prompts.Messages,
        *,
        max_tokens: int,
        thinking: bool = True,
        backend: Optional[Backend] = None,
        seed: Optional[int] = None,
        finish: bool = True,
    ) -> Generation:
        backend = backend or self.backend
        cfg = self.config
        self.tracker.add(agent_id, role)
        request = {"messages": messages, "max_tokens": max_tokens, "thinking": thinking, "seed": seed}

        def progress(tokens: int, phase: str) -> None:
            self.tracker.update(agent_id, status=phase, tokens=tokens)

        counted = 0  # tokens of this agent already added to self.tokens
        try:
            gen = await backend.chat(messages, max_tokens=max_tokens, temperature=cfg.temperature, top_p=cfg.top_p,
                                     thinking=thinking, seed=seed, on_progress=progress)
            self.calls += 1
            self.tokens += gen.completion_tokens
            counted = gen.completion_tokens
            self.recorder.call(agent_id, role, request, gen)
            if gen.truncated and thinking and cfg.force_finish and backend.raw_bos is not None:
                gen = await self._force_finish(agent_id, backend, messages, gen)
        except asyncio.CancelledError:
            # cancelled work still cost compute
            self.tokens += max(0, self.tracker.agents[agent_id].tokens - counted)
            self.tracker.finish(agent_id, "cancelled")
            raise
        except Exception as exc:
            self.tracker.finish(agent_id, "failed", note=f"{type(exc).__name__}: {exc}"[:90])
            self.recorder.call(agent_id, role, request, None, error=repr(exc))
            raise
        self.tracker.update(agent_id, tokens=gen.completion_tokens)
        if finish:
            self.tracker.finish(agent_id, "done", note=gen.finish_reason or "")
        return gen

    async def _force_finish(self, agent_id: str, backend: Backend, messages: prompts.Messages, gen: Generation) -> Generation:
        """Close a truncated (or looping) thinking trace and let the model write its answer.

        If the finish fails, the truncated generation is returned as it is: its reasoning can still be
        rescued by a scribe, so a failed finish must not sink the candidate.
        """
        cfg = self.config
        self.tracker.update(agent_id, status="write", note="forced finish")
        reasoning = gen.reasoning
        tail: Optional[Generation] = None
        error: Optional[Exception] = None
        for _ in range(3):
            prompt = forced_finish_prompt(messages, reasoning, bos=backend.raw_bos)
            try:
                tail = await backend.complete(
                    prompt, max_tokens=cfg.finish_tokens, temperature=cfg.temperature, top_p=cfg.top_p,
                    on_progress=lambda n, _: self.tracker.update(agent_id, tokens=gen.completion_tokens + n),
                )
                break
            except BackendError as err:
                error = err
                if err.status != 400 or len(reasoning) < 8000:
                    break
                reasoning = trim_middle(reasoning, len(reasoning) // 2)  # prompt did not fit the context
            except Exception as err:  # e.g. the connection failed after the client's retries
                error = err
                break
        if tail is None:
            self.tracker.note(f"{agent_id} forced finish failed: {error!r}"[:120])
            self.recorder.call(f"{agent_id}+finish", "finisher", {"prompt_chars": len(prompt)}, None, error=repr(error))
            return gen
        self.calls += 1
        self.tokens += tail.completion_tokens
        self.recorder.call(f"{agent_id}+finish", "finisher", {"prompt_chars": len(prompt)}, tail)
        content = split_reasoning(tail.content)[1] if THINK_CLOSE in tail.content else tail.content
        return Generation(
            reasoning=gen.reasoning, content=content, finish_reason="forced", prompt_tokens=gen.prompt_tokens,
            completion_tokens=gen.completion_tokens + tail.completion_tokens, seconds=gen.seconds + tail.seconds,
        )

    async def _gather(self, coros: Iterable[Awaitable[Any]], stop: Optional[asyncio.Event] = None) -> None:
        """Run ``coros`` concurrently; cancel whatever is left once ``stop`` is set."""
        tasks = [asyncio.ensure_future(c) for c in coros]
        if not tasks:
            return
        stopper = asyncio.ensure_future(stop.wait()) if stop is not None else None
        pending = set(tasks)
        try:
            while pending:
                waiting = pending | ({stopper} if stopper else set())
                done, _ = await asyncio.wait(waiting, return_when=asyncio.FIRST_COMPLETED)
                pending -= done
                if stopper is not None and stopper in done:
                    break
        finally:
            for task in pending:
                task.cancel()
            if stopper is not None:
                stopper.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
        for task in tasks:
            if not task.cancelled() and task.exception() is not None:
                self.errors.append(task.exception())
                self.tracker.note(f"agent error: {task.exception()!r}"[:120])

    # ---------------------------------------------------------------- proof mode

    def _accepted(self, cand: Candidate) -> bool:
        return len(cand.grades) >= self.config.verifiers and cand.min_grade >= self.config.accept_grade

    def _rank(self, cand: Candidate) -> Tuple[Any, ...]:
        return (self._accepted(cand), cand.consensus, round(cand.mean_grade, 3), cand.min_grade, cand.lab_clean,
                len(cand.grades), bool(cand.text))

    @staticmethod
    def _mark_consensus(pool: List[Candidate]) -> None:
        """Flag candidates whose final boxed answer agrees with the most common one among the candidates.

        Self-verification by a small model is often lenient, and agreement on the final answer is a signal that
        does not depend on the verifier. ``_rank`` puts it right after acceptance and above the mean grade, so it
        decides between accepted candidates and also between unaccepted ones whose grades differ. Candidates are
        grouped by their last ``\\boxed{}`` answer (compared with ``answers_match``); once there are two or more
        groups and one of them is largest, every candidate outside it, including those without a short boxed
        answer, counts as not agreeing. A refined candidate counts as an attempt of its own, although it usually
        keeps its parent's answer.
        """
        buckets: List[List[Candidate]] = []
        for cand in pool:
            answer = last_boxed(cand.text)
            if not answer or len(answer) > 80:  # no short final answer (e.g. a pure "show that" proof)
                continue
            for bucket in buckets:
                if answers_match(last_boxed(bucket[0].text), answer):
                    bucket.append(cand)
                    break
            else:
                buckets.append([cand])
        if len(buckets) < 2:
            return
        top = max(len(b) for b in buckets)
        leaders = [b for b in buckets if len(b) == top]
        if len(leaders) == 1:
            for cand in pool:
                cand.consensus = cand in leaders[0]

    async def prove(self, problem: str) -> ProofResult:
        cfg = self.config
        start = time.monotonic()
        self.tracker.mode = self.tracker.mode or "prove"
        pool: List[Candidate] = []
        stop = asyncio.Event()

        async def develop(cand: Candidate, gen: Generation) -> None:
            cand = await self._maybe_scribe(problem, cand, gen)
            await self._evaluate(problem, cand)
            pool.append(cand)
            self._update_status(pool)
            if self._accepted(cand):
                stop.set()

        async def attempt(i: int) -> None:
            if not self._budget_left():
                return
            agent = f"P{i + 1}"
            hint = prompts.STRATEGIES[i % len(prompts.STRATEGIES)] if cfg.strategies else ""
            gen = await self._call(agent, "prover", prompts.prover(problem, hint),
                                   max_tokens=cfg.prover_tokens, seed=self._seed(i))
            await develop(Candidate(agent, gen.content.strip(), "prover", notes=gen.reasoning, finish=gen.finish_reason), gen)

        await self._gather((attempt(i) for i in range(cfg.provers)), stop if cfg.early_stop else None)

        refined = set()
        for rnd in range(1, cfg.rounds + 1):
            if stop.is_set() or not self._budget_left():
                break
            ranked = sorted((c for c in pool if c.text and c.id not in refined), key=self._rank, reverse=True)
            parents = ranked[: cfg.refine_top]
            if not parents:
                break
            self.tracker.note(f"round {rnd}: repairing {', '.join(p.id for p in parents)}")

            async def repair(j: int, parent: Candidate, rnd: int = rnd) -> None:
                refined.add(parent.id)
                await self._run_lab(problem, parent)  # computational evidence for the repair
                agent = f"R{rnd}.{j + 1}"
                notes = trim_middle(parent.notes, cfg.notes_chars // 2) if parent.notes else ""
                gen = await self._call(agent, "refiner",
                                       prompts.refiner(problem, parent.text, parent.reports, parent.lab_output, notes),
                                       max_tokens=cfg.refiner_tokens, seed=self._seed(1000 * rnd + j))
                await develop(Candidate(agent, gen.content.strip(), "refiner", parent=parent.id,
                                        notes=gen.reasoning, finish=gen.finish_reason), gen)

            await self._gather((repair(j, p) for j, p in enumerate(parents)), stop if cfg.early_stop else None)

        if not pool and self.errors:
            raise self.errors[0]
        self._mark_consensus(pool)
        best = max(pool, key=self._rank) if pool else None
        status = "failed" if best is None or not best.text else ("accepted" if self._accepted(best) else "unverified")
        return ProofResult(problem, status, best.text if best else "", best, pool,
                           self.tokens, time.monotonic() - start, self.calls)

    async def _maybe_scribe(self, problem: str, cand: Candidate, gen: Generation) -> Candidate:
        """Rewrite the proof from the reasoning trace when the final write-up lost it."""
        cfg = self.config
        if cfg.scribe == "never" or not gen.reasoning or not self._budget_left():
            return cand
        forced = gen.finish_reason == "forced"
        # Only clearly thin or force-finished write-ups. A ratio to the reasoning length is a poor signal:
        # concise, complete proofs often follow long reasoning, and rewriting them can drop steps.
        if cfg.scribe == "auto" and not (forced or len(cand.text) < 600):
            return cand
        agent = cand.id.replace("P", "S", 1) if cand.id.startswith("P") else f"{cand.id}s"
        notes = trim_middle(gen.reasoning, cfg.notes_chars)
        out = await self._call(agent, "scribe", prompts.scribe(problem, notes, cand.text),
                               max_tokens=cfg.scribe_tokens, seed=self._seed(agent), finish=False)
        text = out.content.strip()
        # A rewrite of a thin draft must add material; a rewrite of a forced finish only has to be substantial.
        if len(text) < 400 or (not forced and len(text) <= len(cand.text)):
            self.tracker.finish(agent, "done", note="kept original")
            return cand
        self.tracker.finish(agent, "done", note=f"rewrote {cand.id}")
        return Candidate(agent, text, "scribe", parent=cand.id, notes=gen.reasoning, finish=out.finish_reason)

    async def _evaluate(self, problem: str, cand: Candidate) -> None:
        """Screen with one verifier, then run the lab and the confirming verifiers on survivors."""
        cfg = self.config
        if not cand.text:
            cand.grades.append(0)
            cand.reports.append("[CRITICAL] Empty solution.")
            return
        if not self._budget_left():  # the budget is a soft cap: no new calls, but the candidate stays in the pool
            return
        if not (cfg.staged_verify and cfg.verifiers > 1):
            await self._run_lab(problem, cand)
            await self._verify(problem, cand, range(cfg.verifiers))
            return
        await self._verify(problem, cand, range(1))
        if cand.min_grade >= cfg.accept_grade and self._budget_left():
            await self._run_lab(problem, cand)
            await self._verify(problem, cand, range(1, cfg.verifiers))

    async def _run_lab(self, problem: str, cand: Candidate) -> None:
        cfg = self.config
        if not (cfg.lab and cfg.exec_code) or cand.lab_output is not None or not self._budget_left():
            return
        try:
            cand.lab_output = await self._lab(problem, cand)
        except Exception as exc:  # a failed lab check must not sink the candidate
            self.tracker.note(f"{cand.id} lab failed: {exc!r}"[:120])

    async def _verify(self, problem: str, cand: Candidate, indices: Iterable[int]) -> None:
        cfg = self.config

        async def one(k: int) -> None:
            agent = f"{cand.id}/V{k + 1}"
            gen = await self._call(agent, "verifier", prompts.verifier(problem, cand.text, cand.lab_output),
                                   max_tokens=cfg.verifier_tokens, backend=self.verifier_backend,
                                   seed=self._seed(agent), finish=False)
            report = gen.content.strip() or trim_middle(gen.reasoning, 6000)
            grade = parse_grade(gen.content) if gen.content else None
            if grade is None:
                grade = parse_grade(gen.reasoning[-3000:])
            note = ""
            if grade is None:
                grade, note = 0, " (no grade found)"
            elif grade > 4 and count_critical(report) > 0:
                grade, note = 4, " (capped: critical issue listed)"
            cand.grades.append(grade)
            cand.reports.append(report)
            self.tracker.finish(agent, "done", note=f"grade {grade}/7{note}")

        await self._gather(one(k) for k in indices)

    async def _lab(self, problem: str, cand: Candidate) -> Optional[str]:
        cfg = self.config
        agent = f"{cand.id}/L"
        gen = await self._call(agent, "lab", prompts.lab(problem, cand.text, self._modules, cfg.exec_timeout),
                               max_tokens=cfg.lab_tokens, seed=self._seed(agent), finish=False)
        code = extract_code(gen.content) or extract_code(gen.reasoning)
        if not code:
            self.tracker.finish(agent, "done", note="no program")
            return None
        self.tracker.update(agent, status="exec")
        result = await run_python(code, timeout=cfg.exec_timeout)
        output = result.summary()
        passed = len(re.findall(r"^\s*PASS", output, re.M))
        failed = len(re.findall(r"^\s*FAIL", output, re.M))
        verdict = f"{passed} pass / {failed} fail" if passed or failed else ("error" if not result.ok else "ran")
        self.tracker.finish(agent, "done", note=verdict)
        self.recorder.event("lab", agent=agent, code=code, output=output, seconds=round(result.seconds, 2))
        return output

    def _update_status(self, pool: List[Candidate]) -> None:
        graded = [c for c in pool if c.grades]
        if not graded:
            return
        best = max(graded, key=self._rank)
        mark = "accepted" if self._accepted(best) else "best so far"
        self.tracker.status = f"{mark}: {best.id} grades {best.grades} (mean {best.mean_grade:.1f})"

    # --------------------------------------------------------------- answer mode

    async def solve(self, problem: str) -> AnswerResult:
        cfg = self.config
        start = time.monotonic()
        self.tracker.mode = self.tracker.mode or "solve"
        votes: Counter = Counter()
        shown: Dict[str, str] = {}
        samples: List[Dict[str, Any]] = []
        coders = cfg.coders if cfg.exec_code else 0
        total = cfg.solvers + coders
        stop = asyncio.Event()
        decided = {"early": False}

        def record(agent: str, kind: str, raw: Optional[str], gen: Generation) -> None:
            norm = normalize_answer(raw) if raw else None
            if norm:
                # equivalent answers (3/4, 0.75, \frac{6}{8}, ...) share one vote bucket
                norm = next((k for k in votes if k == norm or answers_match(shown[k], raw)), norm)
                votes[norm] += 1
                shown.setdefault(norm, raw)
            samples.append({"agent": agent, "kind": kind, "answer": raw, "normalized": norm,
                            "tokens": gen.completion_tokens, "finish": gen.finish_reason})
            self.tracker.finish(agent, "done", note=f"→ {raw}" if raw else "no answer")
            ranking = votes.most_common()
            self.tracker.status = "votes: " + "  ".join(f"{shown[a]} ×{n}" for a, n in ranking[:5])
            if cfg.early_stop and ranking and not stop.is_set():
                lead = ranking[0][1]
                runner_up = ranking[1][1] if len(ranking) > 1 else 0
                if lead > runner_up + (total - len(samples)):  # no outcome of the rest can change the winner
                    decided["early"] = len(samples) < total
                    stop.set()

        async def think(i: int) -> None:
            if not self._budget_left():
                return
            agent = f"A{i + 1}"
            gen = await self._call(agent, "solver", prompts.solver(problem),
                                   max_tokens=cfg.solver_tokens, seed=self._seed(i), finish=False)
            raw = last_boxed(gen.content) if gen.content else last_boxed(gen.reasoning[-2000:])
            record(agent, "think", raw, gen)

        async def code(i: int) -> None:
            if not self._budget_left():
                return
            agent = f"C{i + 1}"
            gen = await self._call(agent, "coder", prompts.coder(problem, self._modules, cfg.exec_timeout),
                                   max_tokens=cfg.solver_tokens, seed=self._seed(500 + i), finish=False)
            program = extract_code(gen.content) or extract_code(gen.reasoning)
            raw = None
            if program:
                self.tracker.update(agent, status="exec")
                result = await run_python(program, timeout=cfg.exec_timeout)
                self.recorder.event("exec", agent=agent, code=program, output=result.summary())
                line = last_line(result.stdout) if result.ok else None
                if line:
                    raw = _ANSWER_LABEL.sub("", line).strip() or None
            record(agent, "code", raw or last_boxed(gen.content), gen)

        jobs: List[Awaitable[Any]] = []
        for i in range(max(cfg.solvers, coders)):  # interleave so both kinds start early
            if i < cfg.solvers:
                jobs.append(think(i))
            if i < coders:
                jobs.append(code(i))
        await self._gather(jobs, stop if cfg.early_stop else None)

        if not samples and self.errors:
            raise self.errors[0]
        ranking = votes.most_common()
        answer = shown[ranking[0][0]] if ranking else None
        return AnswerResult(problem, answer, [(shown[a], n) for a, n in ranking], samples,
                            self.tokens, time.monotonic() - start, self.calls, decided["early"])
