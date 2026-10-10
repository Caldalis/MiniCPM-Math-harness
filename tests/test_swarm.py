"""End-to-end swarm logic against a scripted fake backend (no model needed)."""

import asyncio
from typing import Callable, List

from minicpm_math.client import BackendError, Generation
from minicpm_math.swarm import Swarm, config_for
from minicpm_math.template import BOS

ROLE_MARKERS = [
    ("verifier", "You are a strict grader"),
    ("refiner", "## Reviewer reports"),
    ("scribe", "scratch work of a strong student"),
    ("lab", "tests this solution by brute force"),
    ("coder", "with the help of a computer"),
    ("prover", "Write a complete and rigorous proof."),
    ("solver", "Please reason step by step"),
]


def role_of(text: str) -> str:
    for role, marker in ROLE_MARKERS:
        if marker in text:
            return role
    raise AssertionError(f"unknown prompt: {text[:80]}")


class FakeBackend:
    base_url = "fake://"
    model = "fake"
    raw_bos = BOS

    def __init__(self, script: Callable[[str, str, int], Generation]):
        self.script = script
        self.counts = {}
        self.raw_prompts: List[str] = []

    async def model_name(self) -> str:
        return self.model

    async def aclose(self) -> None:
        pass

    async def chat(self, messages, *, max_tokens, temperature=0.9, top_p=0.95, thinking=True, seed=None,
                   on_progress=None) -> Generation:
        text = messages[-1]["content"]
        role = role_of(text)
        self.counts[role] = self.counts.get(role, 0) + 1
        n = self.counts[role]
        if on_progress:
            on_progress(0, "think")
        await asyncio.sleep(0.005 * n)  # later calls finish later, like a real server
        return self.script(role, text, n)

    async def complete(self, prompt, *, max_tokens, temperature=0.9, top_p=0.95, seed=None,
                       on_progress=None) -> Generation:
        self.raw_prompts.append(prompt)
        return Generation(content="Final solution written after the forced finish. " * 30,
                          finish_reason="stop", completion_tokens=50)


def gen(content: str = "", reasoning: str = "thinking...", finish: str = "stop", tokens: int = 100) -> Generation:
    return Generation(reasoning=reasoning, content=content, finish_reason=finish, completion_tokens=tokens, seconds=1.0)


PROOF = "Proof. " + "Every step is justified carefully. " * 40 + "QED."
LAB_OK = "```python\nprint('PASS: small cases agree')\n```"


async def test_solve_votes_and_stops_early():
    def script(role, text, n):
        return gen(r"so the answer is \boxed{38}" if n != 2 else r"\boxed{28}")

    backend = FakeBackend(script)
    swarm = Swarm(backend, config_for("standard", solvers=8, exec_code=False))
    result = await swarm.solve("Find the sum of all n such that n^2 - 19n + 99 is a square.")
    assert result.answer == "38"
    assert result.votes[0] == ("38", sum(1 for s in result.samples if s["normalized"] == "38"))
    assert result.decided_early and len(result.samples) < 8


async def test_equivalent_answers_share_a_vote():
    forms = [r"\boxed{\frac{3}{4}}", r"\boxed{0.75}", r"\boxed{\dfrac{6}{8}}", r"\boxed{1/2}"]

    def script(role, text, n):
        return gen(forms[(n - 1) % len(forms)])

    swarm = Swarm(FakeBackend(script), config_for("standard", solvers=4, exec_code=False, early_stop=False))
    result = await swarm.solve("What is 3/4?")
    assert result.votes[0][1] == 3 and result.answer == r"\frac{3}{4}"


async def test_program_aided_votes():
    def script(role, text, n):
        if role == "coder":
            return gen("```python\nprint(sum(n for n in range(1, 100) if int((n*n-19*n+99)**0.5)**2 == n*n-19*n+99))\n```")
        return gen(r"\boxed{28}")

    swarm = Swarm(FakeBackend(script), config_for("standard", solvers=1, coders=3, early_stop=False))
    result = await swarm.solve("Find the sum of all n such that n^2 - 19n + 99 is a square.")
    assert result.answer == "38" and dict(result.votes) == {"38": 3, "28": 1}


async def test_prove_accepts_when_all_verifiers_agree():
    def script(role, text, n):
        return {"prover": gen(PROOF), "lab": gen(LAB_OK), "verifier": gen(r"No issues found. \boxed{7}")}[role]

    backend = FakeBackend(script)
    swarm = Swarm(backend, config_for("standard", provers=2, verifiers=3))
    result = await swarm.prove("Prove that the sum of two even numbers is even.")
    assert result.status == "accepted"
    assert result.best.grades == [7, 7, 7]
    assert result.to_dict()["proof"] == PROOF
    assert "PASS" in (result.best.lab_output or "")
    assert backend.counts.get("refiner", 0) == 0


async def test_prove_repairs_after_bad_reviews():
    def script(role, text, n):
        if role == "prover":
            return gen(PROOF)
        if role == "lab":
            return gen(LAB_OK)
        if role == "refiner":
            return gen("Repaired proof. " + PROOF)
        if role == "verifier":
            return gen(r"No issues found. \boxed{7}") if "Repaired proof." in text else gen("[CRITICAL] wrong.\n\\boxed{1}")
        raise AssertionError(role)

    backend = FakeBackend(script)
    swarm = Swarm(backend, config_for("standard", provers=2, verifiers=2, rounds=2, refine_top=1))
    result = await swarm.prove("Prove something.")
    assert result.status == "accepted" and result.best.origin == "refiner"
    assert result.best.parent in ("P1", "P2")
    # staged verification: rejected first-wave candidates got a single verifier vote each
    assert all(len(c.grades) == 1 for c in result.candidates if c.origin == "prover")


async def test_critical_issue_caps_grade_and_blocks_acceptance():
    def script(role, text, n):
        return {"prover": gen(PROOF), "lab": gen(LAB_OK),
                "verifier": gen("[CRITICAL] The case n=1 fails.\n\\boxed{7}"),
                "refiner": gen(PROOF)}[role]

    swarm = Swarm(FakeBackend(script), config_for("standard", provers=1, verifiers=2, rounds=1))
    result = await swarm.prove("Prove something.")
    assert result.status == "unverified"
    assert all(g <= 4 for c in result.candidates for g in c.grades)


async def test_truncated_prover_is_force_finished_and_scribed():
    def script(role, text, n):
        if role == "prover":
            return gen("", reasoning="long scratch work " * 200, finish="length", tokens=32768)
        if role == "scribe":
            return gen("Clean proof from the notes. " + PROOF)
        return {"lab": gen(LAB_OK), "verifier": gen(r"\boxed{7}")}[role]

    backend = FakeBackend(script)
    swarm = Swarm(backend, config_for("standard", provers=1, verifiers=1))
    result = await swarm.prove("Prove something hard.")
    assert backend.raw_prompts and backend.raw_prompts[0].endswith("</think>\n\n")
    assert result.best.origin == "scribe" and result.best.parent == "P1"
    assert result.status == "accepted"


async def test_failed_forced_finish_keeps_the_candidate():
    def script(role, text, n):
        if role == "prover":
            return gen("", reasoning="long scratch work " * 200, finish="length", tokens=32768)
        if role == "scribe":
            return gen("Clean proof from the notes. " + PROOF)
        return {"lab": gen(LAB_OK), "verifier": gen(r"\boxed{7}")}[role]

    class NoCompletions(FakeBackend):
        async def complete(self, prompt, **kwargs):
            raise BackendError("404 from fake:///completions", 404)

    swarm = Swarm(NoCompletions(script), config_for("standard", provers=1, verifiers=1))
    result = await swarm.prove("Prove something hard.")
    assert result.status == "accepted" and result.best.origin == "scribe"
    assert any("forced finish failed" in line for line in swarm.tracker.log)


async def test_concise_proof_after_long_reasoning_is_not_rewritten():
    def script(role, text, n):
        if role == "prover":
            return gen("Short but complete proof. " * 30, reasoning="long exploration " * 3000)
        return {"lab": gen(LAB_OK), "verifier": gen(r"\boxed{7}")}[role]

    backend = FakeBackend(script)
    result = await Swarm(backend, config_for("standard", provers=1, verifiers=1)).prove("Prove it.")
    assert backend.counts.get("scribe", 0) == 0 and result.best.origin == "prover"


async def test_thin_draft_keeps_original_when_rewrite_adds_nothing():
    def script(role, text, n):
        if role == "prover":
            return gen("Proof sketch: induct on n. " * 20, reasoning="notes " * 500)  # 539 chars: thin
        if role == "scribe":
            return gen("Induct on n. " * 35)  # 454 chars: substantial, but shorter than the draft
        return {"lab": gen(LAB_OK), "verifier": gen(r"\boxed{7}")}[role]

    backend = FakeBackend(script)
    result = await Swarm(backend, config_for("standard", provers=1, verifiers=1)).prove("Prove it.")
    assert backend.counts["scribe"] == 1 and result.best.origin == "prover"


async def test_answer_consensus_breaks_ties_between_equally_graded_proofs():
    answers = {1: "5", 2: "7", 3: "7"}

    def script(role, text, n):
        if role == "prover":
            return gen(PROOF + f" Hence the answer is \\boxed{{{answers[n]}}}.")
        return {"lab": gen(LAB_OK), "verifier": gen(r"No issues found. \boxed{7}")}[role]

    swarm = Swarm(FakeBackend(script), config_for("standard", provers=3, verifiers=1, early_stop=False))
    result = await swarm.prove("Determine the answer.")
    assert result.best.text.endswith(r"\boxed{7}.")
    assert {c.id: c.consensus for c in result.candidates}["P1"] is False


async def test_spent_budget_skips_screening():
    def script(role, text, n):
        return {"prover": gen(PROOF, tokens=30000), "lab": gen(LAB_OK), "verifier": gen(r"\boxed{7}")}[role]

    backend = FakeBackend(script)
    result = await Swarm(backend, config_for("standard", provers=2, verifiers=3, budget=10000)).prove("Prove it.")
    # the provers were already running when the budget ran out; nothing new starts after that
    assert backend.counts.get("verifier", 0) == 0 and result.status == "unverified" and result.tokens == 60000
