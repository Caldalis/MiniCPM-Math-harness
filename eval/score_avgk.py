#!/usr/bin/env python3
"""Score avg@k answer runs written by sample_avgk.py: avg@k, maj@k, pass@k, truncation and token statistics.

A sample counts as correct only if it ended on its own (finish == "stop") and its answer matches the gold one
(normalized strings, then math-verify symbolic equivalence re-checked by exact simplification). A sample that ran
into the context limit counts as unanswered, as it would for one plain API call. maj@k votes over the answered
samples; ties go to the answer that finished first, as in the harness, and are counted separately.

The standard error of avg@k only covers the finite number of samples per problem. With two models, the script also
prints the gap between them with a 95% interval from a paired bootstrap over the problems, which covers the choice
of problems as well.

usage: python eval/score_avgk.py RUNS16 DATA_DIR [-k 16] [--models math,base] [--json OUT.json]
       (RUNS16/<model>/samples.jsonl, DATA_DIR/<dataset>.jsonl with "id" and "answer")
"""
from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from pathlib import Path

from minicpm_math.parsing import answers_match

DATASETS = {"aime25": "AIME 2025", "aime26": "AIME 2026", "hmmt26": "HMMT Feb 2026"}


def load_samples(path: Path):
    """{(ds, id): {i: row}}, first successful row per sample."""
    per: dict = {}
    if not path.exists():
        return per
    for line in open(path, encoding="utf-8"):
        row = json.loads(line)
        if "error" in row:
            continue
        per.setdefault((row["ds"], str(row["id"])), {}).setdefault(row["i"], row)
    return per


def score_problem(gold: str, rows: list) -> dict:
    marks = [r.get("finish") == "stop" and bool(r.get("answer")) and answers_match(gold, r["answer"]) for r in rows]
    buckets: list = []  # [representative answer, votes], in finishing order
    for r in sorted(rows, key=lambda r: r.get("t_end", 0)):
        if r.get("finish") != "stop" or not r.get("answer"):
            continue
        for b in buckets:
            if answers_match(b[0], r["answer"]):
                b[1] += 1
                break
        else:
            buckets.append([r["answer"], 1])
    top = max(buckets, key=lambda b: b[1]) if buckets else None  # max() keeps the earliest on ties
    tied = len(buckets) > 1 and sorted((b[1] for b in buckets), reverse=True)[:2] == [top[1], top[1]]
    return {"acc": sum(marks) / len(rows), "maj": bool(top) and answers_match(gold, top[0]), "pass": any(marks),
            "tied": tied, "truncated": sum(r.get("finish") == "length" for r in rows) / len(rows),
            "tokens": [r["completion_tokens"] for r in rows], "k": len(rows)}


def paired_interval(a: dict, b: dict, reps: int = 10000, seed: int = 0) -> tuple:
    """Mean of a - b over the shared problems and its 95% interval when the problems are resampled."""
    diffs = [a[pid] - b[pid] for pid in sorted(set(a) & set(b))]
    rng = random.Random(seed)
    n = len(diffs)
    means = sorted(sum(rng.choice(diffs) for _ in range(n)) / n for _ in range(reps))
    return sum(diffs) / n, means[int(0.025 * reps)], means[int(0.975 * reps) - 1]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("runs")
    p.add_argument("data")
    p.add_argument("-k", type=int, default=16)
    p.add_argument("--models", default="math,base")
    p.add_argument("--json")
    args = p.parse_args()
    out: dict = {}
    for model in args.models.split(","):
        samples = load_samples(Path(args.runs) / model / "samples.jsonl")
        for ds, name in DATASETS.items():
            golds = {str(json.loads(l)["id"]): json.loads(l)["answer"] for l in open(Path(args.data) / f"{ds}.jsonl")}
            scored, partial = {}, 0
            for pid, gold in golds.items():
                rows = [samples.get((ds, pid), {}).get(i) for i in range(args.k)]
                if all(rows):
                    scored[pid] = score_problem(gold, rows)
                elif any(rows):
                    partial += 1
            n = len(scored)
            if not n:
                out[f"{model}/{ds}"] = {"problems": 0, "expected": len(golds), "partial": partial}
                continue
            mean = lambda key: sum(float(v[key]) for v in scored.values()) / n
            # standard error of avg@k from the finite number of samples per problem
            se = math.sqrt(sum(v["acc"] * (1 - v["acc"]) / (args.k - 1) for v in scored.values())) / n
            tokens = [t for v in scored.values() for t in v["tokens"]]
            out[f"{model}/{ds}"] = {
                "problems": n, "expected": len(golds), "partial": partial, "k": args.k,
                f"avg@{args.k}": round(100 * mean("acc"), 2), "se": round(100 * se, 2),
                f"maj@{args.k}": round(100 * mean("maj"), 2), f"pass@{args.k}": round(100 * mean("pass"), 2),
                "truncated": round(100 * mean("truncated"), 2),
                "tied": sum(v["tied"] for v in scored.values()),
                "tied_correct": sum(v["tied"] and v["maj"] for v in scored.values()),
                "mean_tokens": round(statistics.mean(tokens)), "median_tokens": round(statistics.median(tokens)),
                "per_problem": {pid: round(v["acc"], 4) for pid, v in scored.items()},
            }
    k = args.k
    print(f"| model | benchmark | problems | avg@{k} (±SE) | maj@{k} | pass@{k} | hit 128K | ties (correct) | mean / median tokens |")
    print("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for key, v in out.items():
        model, ds = key.split("/")
        if not v["problems"]:
            print(f"| {model} | {DATASETS[ds]} | 0/{v['expected']} ({v['partial']} partial) | | | | | | |")
            continue
        print(f"| {model} | {DATASETS[ds]} | {v['problems']}/{v['expected']} | {v[f'avg@{k}']:.1f} (±{v['se']:.1f}) | "
              f"{v[f'maj@{k}']:.1f} | {v[f'pass@{k}']:.1f} | {v['truncated']:.1f}% | {v['tied']} ({v['tied_correct']}) | "
              f"{v['mean_tokens'] / 1000:.1f}K / {v['median_tokens'] / 1000:.1f}K |")
    models = args.models.split(",")
    compare: dict = {}
    if len(models) == 2:
        first, second = models
        for ds, name in DATASETS.items():
            a = out.get(f"{first}/{ds}", {}).get("per_problem")
            b = out.get(f"{second}/{ds}", {}).get("per_problem")
            if a and b:
                gap, low, high = paired_interval(a, b)
                compare[ds] = {"gap": round(100 * gap, 2), "low": round(100 * low, 2), "high": round(100 * high, 2)}
        if compare:
            print(f"\n| benchmark | avg@{k}: {first} - {second} | 95% interval (paired bootstrap over problems) |")
            print("|---|---:|---:|")
            for ds, c in compare.items():
                print(f"| {DATASETS[ds]} | {c['gap']:+.1f} | {c['low']:+.1f} to {c['high']:+.1f} |")
    if args.json:
        Path(args.json).write_text(json.dumps({**out, "compare": compare} if compare else out, indent=2))


if __name__ == "__main__":
    main()
