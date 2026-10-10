#!/usr/bin/env python3
"""Un-blind the 128K ProofBench-Basic grades and print the proof tables.

Single call (avg@16): per problem, the mean 0-7 score and the share of the 16 samples graded Correct (7);
"complete proofs" is the sum of those shares over the 30 problems, i.e. how many problems one plain call solves on
average. pass@16 counts problems where at least one of the 16 calls is Correct (an oracle pick, for reference).
Swarm: the one proof the harness returns per problem.

usage: python eval/grade_summary.py GRADING_DIR [--json OUT.json]
       (GRADING_DIR holds grading-key.json, auto-grades.json and grades/*.json from the graders)
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

CATEGORIES = ("Correct", "Almost", "Partial", "Incorrect")


def category(score: int) -> str:
    return "Correct" if score == 7 else "Almost" if score >= 5 else "Partial" if score >= 1 else "Incorrect"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("grading")
    p.add_argument("--json")
    args = p.parse_args()
    root = Path(args.grading)
    key = json.load(open(root / "grading-key.json"))
    grades = dict(json.load(open(root / "auto-grades.json")))
    for f in sorted((root / "grades").glob("*.json")):
        grades.update(json.load(open(f)))
    missing = sorted(set(key) - set(grades))
    if missing:
        raise SystemExit(f"{len(missing)} proofs have no grade, e.g. {missing[:5]}")

    single, swarm = defaultdict(list), {}
    for label, meta in key.items():
        score = int(grades[label]["score"])
        entry = {**meta, "label": label, "score": score, "category": category(score),
                 "reason": grades[label].get("reason", "")}
        if meta["origin"] == "single":
            single[meta["pid"]].append(entry)
        else:
            swarm[meta["pid"]] = entry
    pids = sorted(single)
    per = {}
    for pid in pids:
        s = single[pid]
        per[pid] = {"single_mean": sum(e["score"] for e in s) / len(s),
                    "single_correct": sum(e["score"] == 7 for e in s) / len(s),
                    "single_any_correct": any(e["score"] == 7 for e in s),
                    "single_no_proof": sum(e.get("finish") != "stop" for e in s), "k": len(s),
                    "single_scores": [e["score"] for e in sorted(s, key=lambda e: int(e["sample"][1:]))]}
        if pid in swarm:
            w = swarm[pid]
            per[pid].update(swarm_score=w["score"], swarm_status=w.get("status"), swarm_tokens=w.get("tokens"),
                            swarm_reason=w["reason"])
    n = len(pids)
    k = max(v["k"] for v in per.values())
    cats_single = Counter(e["category"] for s in single.values() for e in s)
    out = {
        "problems": n, "k": k,
        "single": {"complete_proofs": round(sum(v["single_correct"] for v in per.values()), 2),
                   "mean_score": round(sum(v["single_mean"] for v in per.values()) / n, 2),
                   f"pass@{k}": sum(v["single_any_correct"] for v in per.values()),
                   "no_proof_rate": round(sum(v["single_no_proof"] for v in per.values()) / (n * k), 4),
                   "categories_per_problem": {c: round(cats_single[c] / k, 2) for c in CATEGORIES}},
    }
    if swarm:
        w = [per[pid] for pid in pids if "swarm_score" in per[pid]]
        accepted = [v for v in w if v["swarm_status"] == "accepted"]
        out["swarm"] = {
            "problems": len(w), "complete_proofs": sum(v["swarm_score"] == 7 for v in w),
            "mean_score": round(sum(v["swarm_score"] for v in w) / len(w), 2),
            "categories": {c: sum(category(v["swarm_score"]) == c for v in w) for c in CATEGORIES},
            "accepted": len(accepted), "accepted_correct": sum(v["swarm_score"] == 7 for v in accepted),
            "better_than_single_mean": sum(v["swarm_score"] > v["single_mean"] for v in w),
            "worse_than_single_mean": sum(v["swarm_score"] < v["single_mean"] for v in w),
            "mean_tokens": round(sum(v["swarm_tokens"] or 0 for v in w) / len(w)),
        }
    out["per_problem"] = per

    s = out["single"]
    print(f"| | Complete proofs | Mean score (0–7) | Correct | Almost | Partial | Incorrect |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    c = s["categories_per_problem"]
    print(f"| single call (avg@{k}) | {s['complete_proofs']:.1f} / {n} | {s['mean_score']:.2f} | {c['Correct']:.1f} | "
          f"{c['Almost']:.1f} | {c['Partial']:.1f} | {c['Incorrect']:.1f} |")
    if swarm:
        w = out["swarm"]
        c = w["categories"]
        print(f"| swarm | {w['complete_proofs']} / {w['problems']} | {w['mean_score']:.2f} | {c['Correct']} | "
              f"{c['Almost']} | {c['Partial']} | {c['Incorrect']} |")
        print(f"\nswarm accepted {w['accepted']}, of which graded Correct {w['accepted_correct']}; better than the "
              f"single-call mean on {w['better_than_single_mean']} problems, worse on {w['worse_than_single_mean']}")
    print(f"single call: pass@{k} {s[f'pass@{k}']}/{n}; no proof (hit 128K or no write-up) {100 * s['no_proof_rate']:.1f}%")
    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
