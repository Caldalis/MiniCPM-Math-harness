"""Benchmark runner.

For answer benchmarks one ``solve`` run per problem yields three numbers at once:
``pass@1`` (mean accuracy of individual samples, i.e. the single-shot model), ``maj@k``
(the swarm's voted answer) and ``pass@k`` (at least one sample right). Comparing the
first two is the honest measure of what the harness adds.

Proof benchmarks are run with ``prove`` and written out for external grading; the
harness' own self-verification grades are recorded but are not a substitute for a grader.
"""

from __future__ import annotations

import csv
import io
import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

HF = "https://huggingface.co"
ROWS_API = "https://datasets-server.huggingface.co/rows"
IMOBENCH = "gh:google-deepmind/superhuman@80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench"

# Pinned public sources (the AIME 2025 and IMO-Bench revisions match the ones used in our own testing).
ALIASES = {
    "aime25": [
        "hf:opencompass/AIME2025@a6ad95f611d72cf628a80b58bd0432ef6638f958/aime2025-I.jsonl",
        "hf:opencompass/AIME2025@a6ad95f611d72cf628a80b58bd0432ef6638f958/aime2025-II.jsonl",
    ],
    "aime26": ["hf-rows:MathArena/aime_2026"],
    "hmmt26": ["hf-rows:MathArena/hmmt_feb_2026"],
    "answerbench": [f"{IMOBENCH}/answerbench_v2.csv"],
    "proofbench": [f"{IMOBENCH}/proofbench_v2.csv"],
    "proofbench-basic": [f"{IMOBENCH}/proofbench_v2.csv#PB-Basic"],
}

PROBLEM_KEYS = ("problem", "question", "prompt", "Problem", "Question")
ANSWER_KEYS = ("answer", "Answer", "Short Answer", "final_answer", "gold", "ground_truth")
ID_KEYS = ("id", "ID", "Problem ID", "problem_id", "problem_idx", "idx", "unique_id")
REFERENCE_KEYS = ("Solution", "solution", "Grading guidelines", "grading_guidelines")


def _get_json(url: str) -> Any:
    with urllib.request.urlopen(url, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _get_text(url: str) -> str:
    with urllib.request.urlopen(url, timeout=120) as resp:
        return resp.read().decode("utf-8")


def _parse_records(text: str, name: str) -> List[Dict[str, Any]]:
    if name.endswith(".jsonl"):
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    if name.endswith(".csv"):
        return list(csv.DictReader(io.StringIO(text)))
    data = json.loads(text)
    return data if isinstance(data, list) else data.get("data") or data.get("rows") or []


def _gh_file(spec: str) -> List[Dict[str, Any]]:
    # gh:<owner>/<repo>@<rev>/<path>
    owner, rest = spec[len("gh:"):].split("/", 1)
    repo_rev, path = rest.split("/", 1)
    repo, _, rev = repo_rev.partition("@")
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{rev or 'main'}/{path}"
    return _parse_records(_get_text(url), path)


def _hf_file(spec: str) -> List[Dict[str, Any]]:
    # hf:<org>/<name>[@rev]/<path>
    body = spec[len("hf:"):]
    org, rest = body.split("/", 1)
    name, path = rest.split("/", 1)
    rev = "main"
    if "@" in name:
        name, rev = name.split("@", 1)
    url = f"{HF}/datasets/{org}/{name}/resolve/{rev}/{path}"
    return _parse_records(_get_text(url), path)


def _hf_rows(spec: str) -> List[Dict[str, Any]]:
    # hf-rows:<org>/<name>[:config[:split]] via the datasets-server API (works for parquet datasets)
    body = spec[len("hf-rows:"):]
    repo, _, rest = body.partition(":")
    config, _, split = rest.partition(":")
    if not config or not split:
        info = _get_json(f"https://datasets-server.huggingface.co/splits?dataset={urllib.parse.quote(repo)}")
        first = info["splits"][0]
        config, split = config or first["config"], split or first["split"]
    rows: List[Dict[str, Any]] = []
    while True:
        query = urllib.parse.urlencode({"dataset": repo, "config": config, "split": split,
                                        "offset": len(rows), "length": 100})
        page = _get_json(f"{ROWS_API}?{query}")
        batch = [r["row"] for r in page.get("rows", [])]
        rows.extend(batch)
        if not batch or len(rows) >= page.get("num_rows_total", len(rows)):
            return rows


def _pick(record: Dict[str, Any], keys) -> Optional[Any]:
    for key in keys:
        if record.get(key) not in (None, ""):
            return record[key]
    return None


def load_items(spec: str) -> List[Dict[str, Any]]:
    """Load ``[{"id", "problem", "answer"}]`` from a local .jsonl/.json file, an alias, or HF."""
    sources = ALIASES.get(spec, [spec])
    items: List[Dict[str, Any]] = []
    for source in sources:
        source, _, id_prefix = source.partition("#")
        if source.startswith("hf:"):
            records = _hf_file(source)
        elif source.startswith("hf-rows:"):
            records = _hf_rows(source)
        elif source.startswith("gh:"):
            records = _gh_file(source)
        else:
            path = Path(source)
            records = _parse_records(path.read_text(encoding="utf-8"), path.name)
        prefix = Path(source.split("/")[-1]).stem if len(sources) > 1 else ""
        for i, record in enumerate(records):
            problem = _pick(record, PROBLEM_KEYS)
            if not problem:
                continue
            rid = _pick(record, ID_KEYS)
            rid = str(rid) if rid is not None else str(i + 1)
            if id_prefix and not rid.startswith(id_prefix):
                continue
            answer = _pick(record, ANSWER_KEYS)
            reference = {k: record[k] for k in REFERENCE_KEYS if record.get(k)}
            items.append({"id": f"{prefix}-{rid}" if prefix else rid, "problem": str(problem).strip(),
                          "answer": None if answer is None else str(answer).strip(), "reference": reference})
    return items


def score_answer_run(gold: Optional[str], result: Any) -> Dict[str, Any]:
    """Per-problem scores; pass@1 is reported separately for chain-of-thought and program-aided samples."""
    from .parsing import answers_match

    # the gold answer goes first: answers_match treats its first argument as the reference
    row: Dict[str, Any] = {"correct": answers_match(gold, result.answer), "tied": result.tied,
                           "samples": len(result.samples)}
    hits = []
    for kind in ("think", "code"):
        group = [s for s in result.samples if s["kind"] == kind]
        marks = [answers_match(gold, s["answer"]) for s in group]
        hits += marks
        if marks:
            row[f"pass_at_1_{kind}"] = sum(marks) / len(marks)
        if kind == "think" and group:
            # A plain single call answers only if it finished on its own: force-finished, truncated and loop-cut
            # samples (whose answer may come from the tail of the reasoning) count as unanswered.
            stopped = [s.get("finish") == "stop" for s in group]
            row["pass_at_1_think_strict"] = sum(m and ok for m, ok in zip(marks, stopped)) / len(group)
            row["forced_rate"] = sum(s.get("finish") == "forced" for s in group) / len(group)
    row["pass_at_k"] = any(hits)
    return row


def summarize_answers(rows: List[Dict[str, Any]], k: int) -> Dict[str, Any]:
    scored = [r for r in rows if "correct" in r]
    if not scored:
        return {}
    n = len(scored)
    out: Dict[str, Any] = {}
    for key, label in (("pass_at_1_think", "pass@1"), ("pass_at_1_think_strict", "pass@1 (no forced finish)"),
                       ("forced_rate", "forced finish rate"), ("pass_at_1_code", "pass@1 (program-aided)")):
        values = [r[key] for r in scored if key in r]
        if values:
            out[label] = round(sum(values) / len(values), 4)
    out[f"maj@{k}"] = round(sum(r["correct"] for r in scored) / n, 4)
    out[f"pass@{k}"] = round(sum(r["pass_at_k"] for r in scored) / n, 4)
    # Ties are broken by finishing order, so a tied "correct" vote is luck; report how often it happened.
    out["tied_votes"] = sum(1 for r in scored if r.get("tied"))
    out["tied_and_correct"] = sum(1 for r in scored if r.get("tied") and r["correct"])
    return out


def reference_markdown(item: Dict[str, Any]) -> str:
    parts = [f"# Reference for {item['id']}", "", "## Problem", "", item["problem"]]
    if item.get("answer"):
        parts += ["", "## Short answer", "", item["answer"]]
    for key, text in (item.get("reference") or {}).items():
        parts += ["", f"## {key}", "", str(text).strip()]
    return "\n".join(parts) + "\n"
