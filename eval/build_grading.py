#!/usr/bin/env python3
"""Build blind grading packets for the 128K ProofBench-Basic runs: 16 single calls + 1 swarm proof per problem.

Every proof gets its own packet (problem, official reference solution, official grading guidelines, one proof)
under an opaque id, so a grader cannot tell a single call from the swarm. A single call that ended without a
write-up (it ran into the 128K limit, or stopped inside its reasoning) submitted nothing; by the rubric that is
Incorrect (0), so it is scored 0 directly and gets no packet. The key (id -> origin) goes to grading-key.json,
which graders never see. Packets are dealt into grader batches of at most --batch proofs, each batch holding
proofs of one problem in shuffled order.

Ids, shuffles and batches are drawn from a seeded generator per problem, so re-running the script after more
problems have finished gives the same packets for the ones already built (grading can start before every run is
done). Problems whose 16 single calls or swarm proof are not complete yet are skipped.

usage: python eval/build_grading.py PROOF_SINGLE_DIR SWARM_DIR DATA_JSONL OUT_DIR [-n 16] [--batch 9]
"""
from __future__ import annotations

import argparse
import gzip
import json
import random
import re
from pathlib import Path


def swarm_proofs(root: Path) -> dict:
    out = {}
    for bench in sorted(root.glob("bench-*-proofbench-basic")):
        if not (bench / "results.jsonl").exists():
            continue
        for line in open(bench / "results.jsonl"):
            row = json.loads(line)
            if "error" in row:
                continue
            run = bench / "runs" / Path(row["run"]).name
            result = json.load(open(run / "result.json"))
            text = (result.get("proof") or "").strip()
            if not text and (run / "final.md").exists():
                m = re.search(r"\n## Proof\n\n(.*?)\n## Candidates", (run / "final.md").read_text(), re.S)
                text = m.group(1).strip() if m else ""
            out[row["id"]] = {"text": text, "status": result.get("status"), "best": result.get("best"),
                              "grades": result.get("grades"), "tokens": result.get("tokens"), "run": str(run)}
    return out


def packet(pid: str, item: dict, text: str, label: str) -> str:
    return "\n".join([f"# {label}", "", "## Problem", "", item["problem"], "", "## Reference solution", "",
                      item.get("Solution", "(none)"), "", "## Grading guidelines", "",
                      item.get("Grading guidelines", "(none)"), "", "## Proof", "",
                      text or "(no proof submitted)", ""])


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("single")
    p.add_argument("swarm")
    p.add_argument("data")
    p.add_argument("out")
    p.add_argument("-n", type=int, default=16)
    p.add_argument("--batch", type=int, default=9)
    args = p.parse_args()
    out = Path(args.out)
    (out / "packets").mkdir(parents=True, exist_ok=True)
    data = {}
    for line in open(args.data):
        item = json.loads(line)
        data[item["id"]] = {**item, **(item.get("reference") or {})}
    swarm = swarm_proofs(Path(args.swarm))
    key, batches, auto, skipped = {}, [], {}, []
    for pid in sorted(data):
        traces = [Path(args.single) / "traces" / "proofbench-basic" / pid / f"A{i + 1}.json.gz" for i in range(args.n)]
        if pid not in swarm or not all(t.exists() for t in traces):
            skipped.append(pid)
            continue
        rng = random.Random(f"20261009/{pid}")
        proofs = []
        for i, trace in enumerate(traces):
            t = json.load(gzip.open(trace, "rt", encoding="utf-8"))
            text = (t.get("content") or "").strip() if t.get("finish") == "stop" else ""
            proofs.append(({"pid": pid, "origin": "single", "sample": f"A{i + 1}", "finish": t.get("finish"),
                            "tokens": t.get("completion_tokens")}, text))
        sw = swarm[pid]
        proofs.append(({"pid": pid, "origin": "swarm", "status": sw["status"], "best": sw["best"],
                        "self_grades": sw["grades"], "tokens": sw["tokens"]}, sw["text"]))
        labels = rng.sample(range(16 ** 6), len(proofs))
        graded = []
        for (meta, text), number in zip(proofs, labels):
            label = f"{pid}-{number:06x}"
            key[label] = meta
            if not text:
                auto[label] = {"category": "Incorrect", "score": 0, "reason": "no proof submitted"}
                continue
            (out / "packets" / f"{label}.md").write_text(packet(pid, data[pid], text, label), encoding="utf-8")
            graded.append(label)
        rng.shuffle(graded)
        k = max(1, -(-len(graded) // args.batch))  # batches per problem, sizes as even as possible
        for j in range(k):
            chunk = graded[j::k]
            if chunk:
                batches.append({"batch": f"{pid}-b{j + 1}", "problem": pid, "packets": [f"packets/{x}.md" for x in chunk]})
    (out / "grading-key.json").write_text(json.dumps(key, indent=1))
    (out / "auto-grades.json").write_text(json.dumps(auto, indent=1))
    (out / "batches.json").write_text(json.dumps(batches, indent=1))
    n_packets = sum(len(b["packets"]) for b in batches)
    print(f"{len(key) // (args.n + 1)} problems, {len(key)} proofs: {n_packets} packets in {len(batches)} batches, "
          f"{len(auto)} scored 0 without a packet; skipped (not finished yet): {', '.join(skipped) or 'none'}")


if __name__ == "__main__":
    main()
