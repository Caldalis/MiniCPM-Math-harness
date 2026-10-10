"""Write the public result files in docs/results/ from the raw avg@16 runs and the blind grades.

- answers.json: the scores from score_avgk.py plus every sample's answer, finish reason and length, per problem
- proofbench-basic.json: per problem, the blind grades of the 16 single calls and of the swarm's proof
- proofbench-basic/<id>.md: the problem, the swarm's proof with its grade, and every single-call proof with its grade
- README.md: what the files hold and the licenses of the benchmark material in them

usage: python eval/export_results.py RUNS16 GRADING_DIR DATA_DIR OUT_DIR
  RUNS16       math/ and base/ (answer samples), proof-single/ (single-call proofs), swarm/ (bench-*-proofbench-basic)
  GRADING_DIR  grading-key.json, auto-grades.json and grades/ (see GRADING.md)
  DATA_DIR     aime25.jsonl, aime26.jsonl, hmmt26.jsonl, proofbench-basic.jsonl
"""
import gzip
import json
import subprocess
import sys
from pathlib import Path

from minicpm_math.parsing import answers_match

runs, grading, data_dir, out = (Path(a) for a in sys.argv[1:5])
K = 16
MODELS = (("math", "MiniCPM5-2B-Math"), ("base", "MiniCPM5-2B"))
IMOBENCH = "https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench"
SOURCE = (f"Problem statement from IMO-ProofBench (Basic set; Luong et al., 2025), [google-deepmind/superhuman@80b2527]"
          f"({IMOBENCH}), Copyright 2025 Google LLC, licensed under "
          "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged. Grades are blind grades "
          "by one AI grader (Claude Opus 5.5) using the official reference solution and grading guidelines; they are "
          "not human-reviewed and not comparable with the human-graded scores in the IMO-ProofBench paper.")
README = f"""# Result files

Written by [`eval/export_results.py`](../../eval/export_results.py) from the raw runs. The protocol is in
[docs/results.md](../results.md).

| File | Contents |
|---|---|
| `answers.json` | AIME 2025, AIME 2026 and HMMT February 2026: the scores, and every sample's answer, finish reason and length |
| `proofbench-basic.json` | IMO-ProofBench Basic: the blind grade of every single-call proof and of the swarm's proof |
| `proofbench-basic/<id>.md` | one page per problem: the problem, the swarm's proof and all 16 single-call proofs, with grades and reasons |

## Licenses of the benchmark material

The model outputs, grades and scores here are released under the repository's Apache-2.0 license. The benchmark
material they contain keeps its own license:

- The problem statements in `proofbench-basic/` are from IMO-ProofBench (Luong et al., 2025),
  [google-deepmind/superhuman]({IMOBENCH}), Copyright 2025 Google LLC, licensed under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged.
- The `gold` answers in `answers.json` come from [opencompass/AIME2025](https://huggingface.co/datasets/opencompass/AIME2025)
  (MIT) for AIME 2025, and from MathArena's [aime_2026](https://huggingface.co/datasets/MathArena/aime_2026) and
  [hmmt_feb_2026](https://huggingface.co/datasets/MathArena/hmmt_feb_2026) datasets (Dekoninck et al., 2026), licensed
  under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

How to cite the benchmarks is in [docs/results.md](../results.md#citing-the-benchmarks).
"""


def category(score: int) -> str:
    return "Correct" if score == 7 else "Almost" if score >= 5 else "Partial" if score >= 1 else "Incorrect"


def first_rows(path: Path) -> dict:
    rows: dict = {}
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        if "error" not in r:
            rows.setdefault((r["ds"], str(r["id"]), r["i"]), r)
    return rows


# ---------------------------------------------------------------- answer benchmarks
out.mkdir(parents=True, exist_ok=True)
tmp = out / ".scores.json"
subprocess.run([sys.executable, str(Path(__file__).with_name("score_avgk.py")), str(runs), str(data_dir), "-k", str(K),
                "--json", str(tmp)], check=True, capture_output=True, text=True)
scores = json.loads(tmp.read_text())
tmp.unlink()
answers = {"protocol": {"samples_per_problem": K, "max_model_len": 131072, "kv_cache": "bf16",
                        "forced_finish": False, "loop_guard": False, "seed": "20261008 + sample index",
                        "sampling": {"MiniCPM5-2B-Math": {"temperature": 0.9, "top_p": 0.95, "min_p": 0.0},
                                     "MiniCPM5-2B": {"temperature": 1.0, "top_p": 0.95, "min_p": 0.0}},
                        "scoring": "correct = finished on its own (finish == stop) and answer matches the gold one"},
           "summary": {}, "problems": {}}
if scores.get("compare"):
    answers["gap"] = {"description": "avg@16 of MiniCPM5-2B-Math minus MiniCPM5-2B in points, with the 95% interval of "
                                     "a paired bootstrap over the problems (10,000 resamples, seed 0)",
                      **scores["compare"]}
for model, name in MODELS:
    rows = first_rows(runs / model / "samples.jsonl")
    for ds in ("aime25", "aime26", "hmmt26"):
        s = {k: v for k, v in scores[f"{model}/{ds}"].items() if k != "per_problem"}
        answers["summary"].setdefault(name, {})[ds] = s
        for line in open(data_dir / f"{ds}.jsonl", encoding="utf-8"):
            item = json.loads(line)
            pid = str(item["id"])
            samples = []
            for i in range(K):
                r = rows[(ds, pid, i)]
                samples.append({"agent": r["agent"], "answer": r.get("answer"), "finish": r.get("finish"),
                                "tokens": r.get("completion_tokens"),
                                "correct": r.get("finish") == "stop" and bool(r.get("answer"))
                                and answers_match(item["answer"], r["answer"])})
            answers["problems"].setdefault(name, {}).setdefault(ds, {})[pid] = {
                "gold": item["answer"], "accuracy": round(sum(x["correct"] for x in samples) / K, 4),
                "samples": samples}
(out / "answers.json").write_text(json.dumps(answers, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- proofs
key = json.loads((grading / "grading-key.json").read_text())
grades = json.loads((grading / "auto-grades.json").read_text())
for f in sorted((grading / "grades").glob("*.json")):
    grades.update(json.loads(f.read_text()))
data = {}
for line in open(data_dir / "proofbench-basic.jsonl", encoding="utf-8"):
    item = json.loads(line)
    data[item["id"]] = item
swarm_runs = {}
for bench in sorted((runs / "swarm").glob("bench-*-proofbench-basic")):
    for line in open(bench / "results.jsonl"):
        r = json.loads(line)
        if "error" not in r:
            swarm_runs[r["id"]] = bench / "runs" / Path(r["run"]).name

by_problem: dict = {}
for label, meta in key.items():
    by_problem.setdefault(meta["pid"], []).append((label, meta, grades[label]))
(out / "proofbench-basic").mkdir(exist_ok=True)
summary = []
for pid in sorted(by_problem):
    entries = by_problem[pid]
    single = sorted((e for e in entries if e[1]["origin"] == "single"), key=lambda e: int(e[1]["sample"][1:]))
    swarm = next((e for e in entries if e[1]["origin"] == "swarm"), None)
    texts = {}
    for _, meta, _ in single:
        t = json.load(gzip.open(runs / "proof-single" / "traces" / "proofbench-basic" / pid / f"{meta['sample']}.json.gz",
                                "rt", encoding="utf-8"))
        texts[meta["sample"]] = (t.get("content") or "").strip() if t.get("finish") == "stop" else ""
    scores_16 = [g["score"] for _, _, g in single]
    row = {"id": pid, "single_call": {
        "scores": scores_16, "mean_score": round(sum(scores_16) / len(scores_16), 3),
        "correct_share": round(sum(s == 7 for s in scores_16) / len(scores_16), 4),
        "samples": [{"agent": m["sample"], "finish": m.get("finish"), "tokens": m.get("tokens"), **g,
                     "category": category(g["score"])}
                    for _, m, g in single]}}
    lines = [f"# {pid}", "", SOURCE, "", "## Problem", "", data[pid]["problem"], ""]
    if swarm:
        _, meta, g = swarm
        result = json.loads((swarm_runs[pid] / "result.json").read_text())
        row["swarm"] = {**g, "category": category(g["score"]), "status": result["status"], "best": result["best"], "self_grades": result["grades"],
                        "tokens": result["tokens"], "calls": result["calls"]}
        lines += [f"## Swarm: {result['status']} (best candidate `{result['best']}`; self-verification grades "
                  f"{result['grades']}; {result['tokens']:,} tokens in {result['calls']} calls)", "",
                  f"**Blind grade: {category(g['score'])} ({g['score']}/7).** {g['reason']}", "",
                  (result.get("proof") or "").strip() or "_(no proof)_", ""]
    lines += [f"## Single calls (16 independent samples, up to 128K tokens each, no forced finish)", "",
              f"Mean blind grade {row['single_call']['mean_score']:.2f}/7; graded Correct: "
              f"{sum(s == 7 for s in scores_16)} of {len(scores_16)}.", "",
              "| sample | finish | tokens | grade | reason |", "|---|---|---:|---|---|"]
    for _, m, g in single:
        reason = str(g.get("reason", "")).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {m['sample']} | {m.get('finish')} | {m.get('tokens') or 0:,} | {category(g['score'])} ({g['score']}/7) "
                     f"| {reason} |")
    lines.append("")
    for _, m, g in single:
        body = texts[m["sample"]] or "_(no write-up: the call reached the 128K-token limit or stopped inside its reasoning)_"
        lines += [f"<details><summary>{m['sample']}: {category(g['score'])} ({g['score']}/7)</summary>", "", body, "",
                  "</details>", ""]
    (out / "proofbench-basic" / f"{pid}.md").write_text("\n".join(lines), encoding="utf-8")
    summary.append(row)
(out / "proofbench-basic.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
(out / "README.md").write_text(README, encoding="utf-8")
print(f"wrote {out}/answers.json, {out}/proofbench-basic.json, {out}/README.md and {len(summary)} problem pages")
