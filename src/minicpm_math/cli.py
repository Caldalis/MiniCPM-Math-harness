"""``minicpm-math`` command line: prove, solve, bench, check."""

from __future__ import annotations

import argparse
import asyncio
import importlib.util
import json
import os
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import httpx
from rich.console import Console
from rich.table import Table

from . import __version__, prompts
from .client import Backend, BackendError
from .events import Tracker
from .parsing import first_line, last_boxed
from .swarm import PROFILES, AnswerResult, ProofResult, Swarm, SwarmConfig, config_for
from .template import BOS, render_chat
from .trace import Recorder, new_run_dir
from .ui import fmt_time, fmt_tokens, live_view

DEFAULT_URL = "http://127.0.0.1:8000/v1"
CONCURRENCY = {"quick": 4, "standard": 8, "heavy": 32, "swarm": 64}
MATH_EXTRA = 'pip install "minicpm-math[math] @ git+https://github.com/Caldalis/MiniCPM-Math-harness"'

out = Console()
err = Console(stderr=True)


def read_problem(arg: str) -> str:
    if arg == "-":
        return sys.stdin.read().strip()
    path = Path(arg)
    try:
        is_file = len(arg) < 4096 and path.is_file()
    except (OSError, ValueError):  # e.g. "File name too long": the argument is the problem text itself
        is_file = False
    if is_file:
        return path.read_text(encoding="utf-8").strip()
    return arg.strip()


def missing_math_modules() -> List[str]:
    """Modules of the ``math`` extra that are not installed (math-verify exists for Python 3.10+ only)."""
    names = ["sympy", "numpy"] + (["math_verify"] if sys.version_info >= (3, 10) else [])
    return [name for name in names if importlib.util.find_spec(name) is None]


# ------------------------------------------------------------------------ arguments

def _add_server_args(p: argparse.ArgumentParser) -> None:
    g = p.add_argument_group("server")
    g.add_argument("--base-url", default=os.environ.get("MINICPM_MATH_BASE_URL", DEFAULT_URL),
                   help=f"OpenAI-compatible endpoint (env MINICPM_MATH_BASE_URL, default {DEFAULT_URL})")
    g.add_argument("--model", default=os.environ.get("MINICPM_MATH_MODEL"),
                   help="model name; default: first model the server lists")
    g.add_argument("--api-key", default=os.environ.get("MINICPM_MATH_API_KEY"))
    g.add_argument("--concurrency", type=int, help="max requests in flight (default depends on --profile)")
    g.add_argument("--no-thinking-kwarg", action="store_true",
                   help="do not send chat_template_kwargs (for servers that reject unknown fields)")
    g.add_argument("--no-min-p", action="store_true", help="do not send min_p=0")
    g.add_argument("--no-raw", action="store_true",
                   help="never use /completions (disables forced finish of truncated reasoning)")


def _add_swarm_args(p: argparse.ArgumentParser) -> None:
    g = p.add_argument_group("swarm")
    g.add_argument("--profile", choices=list(PROFILES), default="standard",
                   help="quick (laptop) | standard | heavy (one GPU) | swarm (many GPUs)")
    g.add_argument("--max-tokens", type=int, help="per-call token budget for provers, solvers and refiners")
    g.add_argument("--budget", type=int,
                   help="soft cap on completion tokens for the run: no new calls start once it is spent, "
                        "calls already running finish")
    g.add_argument("--temperature", type=float)
    g.add_argument("--top-p", type=float)
    g.add_argument("--seed", type=int)
    g.add_argument("--no-exec", action="store_true", help="never execute model-written Python")
    g.add_argument("--no-early-stop", action="store_true")
    g.add_argument("--no-force-finish", action="store_true")


def _add_prove_args(p: argparse.ArgumentParser) -> None:
    g = p.add_argument_group("proof search")
    g.add_argument("--provers", type=int, help="parallel first attempts")
    g.add_argument("--verifiers", type=int, help="independent verifier votes per candidate")
    g.add_argument("--rounds", type=int, help="repair rounds after the first wave")
    g.add_argument("--refine-top", type=int, help="candidates repaired per round")
    g.add_argument("--accept-grade", type=int, help="minimum 0-7 grade every verifier must give (default 6)")
    g.add_argument("--scribe", choices=["auto", "always", "never"])
    g.add_argument("--no-lab", action="store_true", help="skip brute-force checking scripts")
    v = p.add_argument_group("external verifier (optional: small prover, bigger checker)")
    v.add_argument("--verifier-base-url")
    v.add_argument("--verifier-model")
    v.add_argument("--verifier-api-key")


def _add_solve_args(p: argparse.ArgumentParser) -> None:
    g = p.add_argument_group("answer voting")
    g.add_argument("-n", "--solvers", type=int, help="chain-of-thought solvers")
    g.add_argument("--coders", type=int, help="program-aided solvers (their programs are executed locally)")


def _add_output_args(p: argparse.ArgumentParser) -> None:
    g = p.add_argument_group("output")
    g.add_argument("--out", default="runs", help="directory for run traces ('' disables tracing)")
    g.add_argument("--no-ui", action="store_true", help="plain log lines instead of the live dashboard")
    g.add_argument("--json", action="store_true", help="print the result as JSON on stdout")
    g.add_argument("--snapshot", metavar="SVG", help="save the final dashboard as an SVG image")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="minicpm-math",
        description="A proof swarm for MiniCPM5-2B-Math: parallel provers, adversarial verifiers, "
                    "brute-force checks and repair, against any OpenAI-compatible server.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("prove", help="search for a complete proof")
    p.add_argument("problem", help="problem text, a path to a .md/.txt file, or '-' for stdin")
    for add in (_add_server_args, _add_swarm_args, _add_prove_args, _add_output_args):
        add(p)

    s = sub.add_parser("solve", help="answer a question by (optionally program-aided) voting")
    s.add_argument("problem", help="problem text, a path to a .md/.txt file, or '-' for stdin")
    for add in (_add_server_args, _add_swarm_args, _add_solve_args, _add_output_args):
        add(s)

    b = sub.add_parser("bench", help="run a benchmark (answer accuracy, or proof dumps for grading)")
    b.add_argument("data", help="aime25 | aime26 | hmmt26 | file.jsonl | hf:org/name@rev/file.jsonl | hf-rows:org/name")
    b.add_argument("--mode", choices=["solve", "prove"], default="solve")
    b.add_argument("--limit", type=int)
    b.add_argument("--ids", help="comma-separated problem ids to run")
    b.add_argument("--early-stop", action="store_true",
                   help="allow early stopping (off by default so pass@1 is unbiased)")
    b.add_argument("--jobs", type=int, default=1, help="problems run concurrently (keeps a GPU server busy)")
    for add in (_add_server_args, _add_swarm_args, _add_prove_args, _add_solve_args, _add_output_args):
        add(b)

    c = sub.add_parser("check", help="check that a server speaks the MiniCPM5 format")
    _add_server_args(c)
    return parser


def build_config(args: argparse.Namespace, mode: str) -> SwarmConfig:
    o: Dict[str, Any] = dict(temperature=args.temperature, top_p=args.top_p, seed=args.seed, budget=args.budget)
    if args.max_tokens:
        o.update(prover_tokens=args.max_tokens, solver_tokens=args.max_tokens, refiner_tokens=args.max_tokens)
    if args.no_exec:
        o["exec_code"] = False
    if args.no_early_stop:
        o["early_stop"] = False
    if args.no_force_finish:
        o["force_finish"] = False
    if mode == "prove":
        o.update(provers=args.provers, verifiers=args.verifiers, rounds=args.rounds, refine_top=args.refine_top,
                 accept_grade=args.accept_grade, scribe=args.scribe)
        if args.no_lab:
            o["lab"] = False
    else:
        o.update(solvers=args.solvers, coders=args.coders)
    return config_for(args.profile, **o)


def build_backends(args: argparse.Namespace) -> Tuple[Backend, Optional[Backend]]:
    concurrency = args.concurrency or CONCURRENCY.get(getattr(args, "profile", "standard"), 8)
    main = Backend(
        args.base_url, args.model, args.api_key, concurrency=concurrency,
        thinking_kwarg=not args.no_thinking_kwarg, min_p=None if args.no_min_p else 0.0,
        raw_bos=None if args.no_raw else BOS,
    )
    verifier = None
    if getattr(args, "verifier_base_url", None):
        verifier = Backend(
            args.verifier_base_url, args.verifier_model, args.verifier_api_key or args.api_key,
            concurrency=concurrency, thinking_kwarg=False, min_p=None, raw_bos=None,
        )
    return main, verifier


# --------------------------------------------------------------------------- output

def proof_markdown(result: ProofResult, cfg: SwarmConfig) -> str:
    best = result.best
    if result.status == "accepted":
        status = (f"**accepted**: every one of {len(best.grades)} verifiers gave at least {cfg.accept_grade}/7. "
                  "Self-verification by a 2B model is evidence, not a guarantee; check the proof.")
    elif result.status == "unverified":
        status = "**unverified**: no candidate passed self-verification; this is the best attempt found."
    else:
        status = "**failed**: no candidate solution was produced."
    lines = [
        "# MiniCPM-Math proof report", "",
        f"- Status: {status}",
        f"- Best candidate: `{best.id}` ({best.origin}{' of ' + best.parent if best.parent else ''}), "
        f"grades {best.grades}" if best else "- Best candidate: none",
        f"- Compute: {result.tokens:,} completion tokens, {result.calls} calls, {fmt_time(result.seconds)}",
        "", "## Problem", "", result.problem, "", "## Proof", "", result.proof or "_none_", "",
        "## Candidates", "", "| id | origin | parent | grades | mean | chars |", "|---|---|---|---|---|---|",
    ]
    for c in sorted(result.candidates, key=lambda c: c.mean_grade, reverse=True):
        lines.append(f"| {c.id} | {c.origin} | {c.parent or ''} | {c.grades} | {c.mean_grade:.1f} | {len(c.text)} |")
    if best and best.reports:
        lines += ["", "## Verifier reports for the best candidate", ""]
        for i, report in enumerate(best.reports, 1):
            lines += [f"### Verifier {i}", "", report.strip(), ""]
    return "\n".join(lines).rstrip() + "\n"


def answer_markdown(result: AnswerResult) -> str:
    lines = ["# MiniCPM-Math answer report", "",
             f"- Answer: **{result.answer}**" + (" (tied vote: the earliest-finished answer is shown)" if result.tied else ""),
             f"- Agreement: {result.agreement:.0%} of {sum(n for _, n in result.votes)} counted votes"
             + (" (stopped early: vote decided)" if result.decided_early else ""),
             f"- Compute: {result.tokens:,} completion tokens, {result.calls} calls, {fmt_time(result.seconds)}",
             "", "## Problem", "", result.problem, "", "## Votes", "", "| answer | votes |", "|---|---|"]
    lines += [f"| {a} | {n} |" for a, n in result.votes]
    return "\n".join(lines) + "\n"


def print_proof(result: ProofResult, run_dir: Optional[Path]) -> None:
    best = result.best
    style = {"accepted": "bold green", "unverified": "bold yellow", "failed": "bold red"}[result.status]
    err.print()
    err.print(f"[{style}]{result.status.upper()}[/]  best {best.id if best else '-'}  grades {best.grades if best else []}"
              f"  ·  {fmt_tokens(result.tokens)} tokens  ·  {result.calls} calls  ·  {fmt_time(result.seconds)}")
    if run_dir:
        err.print(f"[dim]report: {run_dir / 'final.md'}[/]")
    err.print()
    print(result.proof)


def print_answer(result: AnswerResult, run_dir: Optional[Path]) -> None:
    table = Table(box=None, header_style="bold dim")
    table.add_column("answer")
    table.add_column("votes", justify="right")
    for answer, n in result.votes[:8]:
        table.add_row(answer, str(n))
    err.print()
    err.print(table)
    err.print(f"[dim]{fmt_tokens(result.tokens)} tokens · {result.calls} calls · {fmt_time(result.seconds)}"
              + (" · stopped early" if result.decided_early else "") + "[/]")
    if run_dir:
        err.print(f"[dim]report: {run_dir / 'final.md'}[/]")
    print(result.answer if result.answer is not None else "(no answer)")


# ----------------------------------------------------------------------------- runs

async def _reach(*backends: Optional[Backend]) -> None:
    """Contact every server before any work starts, so an unreachable one fails at once with one clear error."""
    for backend in backends:
        if backend is None:
            continue
        if backend.model is None:
            await backend.model_name()
            continue
        try:
            await backend.list_models()
        except BackendError:
            pass  # the server answers; it just does not list its models


async def _run_one(args: argparse.Namespace, mode: str, problem: str, cfg: SwarmConfig,
                   backend: Backend, verifier: Optional[Backend], run_root: Optional[str],
                   label: str = "") -> Tuple[Any, Optional[Path]]:
    run_dir = new_run_dir(run_root, problem, mode) if run_root else None
    recorder = Recorder(run_dir)
    model = await backend.model_name()
    tracker = Tracker(title=(label + " " if label else "") + first_line(problem, 160),
                      mode=f"{mode} · {args.profile}", backend=f"{model} @ {backend.base_url}")
    recorder.write_text("problem.md", problem + "\n")
    recorder.write_json("config.json", {"mode": mode, "profile": args.profile, "model": model,
                                        "base_url": backend.base_url, "config": asdict(cfg), "version": __version__})
    swarm = Swarm(backend, cfg, verifier=verifier, tracker=tracker, recorder=recorder)
    with live_view(tracker, enabled=not args.no_ui, snapshot=getattr(args, "snapshot", None)):
        result = await (swarm.prove(problem) if mode == "prove" else swarm.solve(problem))
    recorder.write_json("result.json", result.to_dict())
    if mode == "prove":
        recorder.write_text("final.md", proof_markdown(result, cfg))
    else:
        recorder.write_text("final.md", answer_markdown(result))
    return result, run_dir


async def cmd_task(args: argparse.Namespace, mode: str) -> int:
    problem = read_problem(args.problem)
    if not problem:
        err.print("[red]empty problem[/]")
        return 2
    cfg = build_config(args, mode)
    backend, verifier = build_backends(args)
    try:
        await _reach(backend, verifier)
        result, run_dir = await _run_one(args, mode, problem, cfg, backend, verifier, args.out or None)
    finally:
        await backend.aclose()
        if verifier:
            await verifier.aclose()
    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    elif mode == "prove":
        print_proof(result, run_dir)
    else:
        print_answer(result, run_dir)
    return 0


async def cmd_bench(args: argparse.Namespace) -> int:
    from .bench import load_items, reference_markdown, score_answer_run, summarize_answers

    items = load_items(args.data)
    if args.ids:
        wanted = {x.strip() for x in args.ids.split(",")}
        items = [it for it in items if it["id"] in wanted]
    if args.limit:
        items = items[: args.limit]
    if not items:
        err.print("[red]no problems loaded[/]")
        return 2
    if not args.early_stop:
        args.no_early_stop = True
    if args.jobs > 1:
        args.no_ui = True  # one dashboard per problem would interleave
    cfg = build_config(args, args.mode)
    backend, verifier = build_backends(args)
    try:
        await _reach(backend, verifier)  # an unreachable server: one error now, not one per problem
    except BaseException:
        await backend.aclose()
        if verifier:
            await verifier.aclose()
        raise
    root = Path(args.out or "runs") / f"bench-{time.strftime('%Y%m%d-%H%M%S')}-{Path(args.data).stem}"
    root.mkdir(parents=True, exist_ok=True)
    (root / "config.json").write_text(json.dumps({"data": args.data, "mode": args.mode, "profile": args.profile,
                                                  "config": asdict(cfg), "version": __version__}, indent=2))
    jobs = asyncio.Semaphore(max(1, args.jobs))
    write_lock = asyncio.Lock()

    async def run_item(k: int, item: Dict[str, Any]) -> Dict[str, Any]:
        label = f"[{k}/{len(items)} {item['id']}]"
        async with jobs:
            row: Dict[str, Any] = {"id": item["id"], "gold": item["answer"]}
            try:
                result, run_dir = await _run_one(args, args.mode, item["problem"], cfg, backend, verifier,
                                                 str(root / "runs"), label)
            except Exception as exc:  # keep going; one bad problem should not end a long benchmark
                row["error"] = repr(exc)
                err.print(f"{label} [red]error[/] {exc!r}")
            else:
                row.update(run=str(run_dir) if run_dir else None, tokens=result.tokens,
                           seconds=round(result.seconds, 1))
                if args.mode == "solve":
                    row.update(answer=result.answer, votes=result.votes, **score_answer_run(item["answer"], result))
                    mark = ("[green]✓[/]" if row["correct"] else "[red]✗[/]") + (" (tie)" if row["tied"] else "")
                    single = row.get("pass_at_1_think", row.get("pass_at_1_code", 0.0))
                    err.print(f"{label} {mark} answer {result.answer!r} gold {item['answer']!r} "
                              f"pass@1 {single:.2f} over {row['samples']} samples")
                else:
                    row.update(status=result.status, grades=result.best.grades if result.best else [])
                    proofs = root / "proofs"
                    proofs.mkdir(exist_ok=True)
                    (proofs / f"{item['id']}.md").write_text(proof_markdown(result, cfg), encoding="utf-8")
                    if item.get("reference") or item.get("answer"):
                        (proofs / f"{item['id']}.reference.md").write_text(reference_markdown(item), encoding="utf-8")
                    err.print(f"{label} {result.status} grades {row['grades']}")
            async with write_lock:
                with open(root / "results.jsonl", "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            return row

    try:
        rows = await asyncio.gather(*(run_item(k, item) for k, item in enumerate(items, 1)))
    finally:
        await backend.aclose()
        if verifier:
            await verifier.aclose()

    done = [r for r in rows if "error" not in r]
    k = cfg.solvers + (cfg.coders if cfg.exec_code else 0)
    summary: Dict[str, Any] = {"data": args.data, "mode": args.mode, "profile": args.profile, "n": len(done),
                               "errors": len(rows) - len(done), "model": backend.model,
                               "tokens": sum(r["tokens"] for r in done),
                               "gpu_seconds": round(sum(r["seconds"] for r in done), 1)}
    if args.mode == "solve":
        summary.update(summarize_answers(done, k))
    else:
        summary["accepted"] = sum(r["status"] == "accepted" for r in done)
    (root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    err.print_json(json.dumps(summary))
    err.print(f"[dim]results: {root}[/]")
    return 0


async def cmd_check(args: argparse.Namespace) -> int:
    missing = missing_math_modules()
    if missing:
        effects = []
        lacking = [m for m in ("sympy", "numpy") if m in missing]
        if lacking:
            effects.append(f"lab and coder scripts cannot use {' or '.join(lacking)}")
        if "math_verify" in missing:
            effects.append("answers that are equal only symbolically count as different votes")
        err.print(f"warning: the math extra is not installed (missing {', '.join(missing)}): {'; '.join(effects)}. "
                  f"Install it with: {MATH_EXTRA}", style="yellow", markup=False, highlight=False)
    backend, _ = build_backends(args)
    try:
        models = await backend.list_models()
        err.print(f"models: {models}")
        model = await backend.model_name()
        gen = await backend.chat(prompts.solver("What is 17 * 23?"), max_tokens=2048, thinking=True)
        err.print(f"chat ({model}): finish={gen.finish_reason} tokens={gen.completion_tokens} "
                  f"{gen.tokens_per_second:.1f} tok/s")
        err.print(f"  reasoning separated: {'yes' if gen.reasoning else 'no'} ({len(gen.reasoning)} chars)")
        boxed = last_boxed(gen.content)
        err.print(f"  boxed answer: {boxed!r} (expected '391')" if boxed else
                  f"  answer (no \\boxed{{}}): {first_line(gen.content, 100)!r}")
        if backend.raw_bos is not None:
            prompt = render_chat([{"role": "user", "content": "Say OK."}], enable_thinking=False, bos=backend.raw_bos)
            raw = await backend.complete(prompt, max_tokens=16, temperature=0.0, top_p=1.0)
            err.print(f"raw /completions (used for forced finish): ok, {raw.completion_tokens} tokens")
            err.print("  BOS: the server adds its own, so raw prompts are sent without one"
                      if await backend.raw_bos_doubled() else "  BOS: taken from the raw prompt (the server adds none)")
    finally:
        await backend.aclose()
    return 0


def _failed_server(exc: httpx.TransportError, args: argparse.Namespace) -> Tuple[str, str]:
    """Base URL and flag of the server that a failed request went to: the verifier's or the main one."""
    try:
        url = str(exc.request.url)
    except RuntimeError:  # the error carries no request
        url = ""
    verifier = (getattr(args, "verifier_base_url", None) or "").rstrip("/")
    if verifier and url.startswith(verifier):
        return verifier, "--verifier-base-url"
    return args.base_url.rstrip("/"), "--base-url"


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command in ("prove", "solve"):
            return asyncio.run(cmd_task(args, args.command))
        if args.command == "bench":
            return asyncio.run(cmd_bench(args))
        return asyncio.run(cmd_check(args))
    except KeyboardInterrupt:
        err.print("\n[yellow]interrupted[/]")
        return 130
    except httpx.TransportError as exc:
        url, flag = _failed_server(exc, args)
        cause = f"{type(exc).__name__}: {exc}".rstrip(": ")
        if isinstance(exc, (httpx.ConnectError, httpx.ConnectTimeout, httpx.UnsupportedProtocol)):
            message = (f"cannot reach the model server at {url} ({cause}). Start one (see README) or pass {flag}; "
                       "llama-server listens on 8080 unless you pass --port, LM Studio on 1234, Ollama on 11434.")
        else:
            message = f"lost the connection to the model server at {url} ({cause})."
        err.print(message, style="red", markup=False, highlight=False)
        return 2
    except BackendError as exc:
        err.print(f"error: {exc}", style="red", markup=False, highlight=False)
        return 1


if __name__ == "__main__":
    sys.exit(main())
