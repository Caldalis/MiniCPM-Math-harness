# Blind grading of IMO-ProofBench Basic

The proof results in [docs/results.md](../docs/results.md) were graded by an AI grader, not by people. This page
records exactly how, so the grades can be checked or redone with a different grader.

## Procedure

1. Every problem has 17 proofs: 16 single calls (the harness' proof prompt without a strategy hint, up to the full
   131,072-token context, no forced finish) and the swarm's final proof.
2. `build_grading.py` writes one packet per proof: the problem, the official reference solution, the official
   grading guidelines and the proof under "## Proof". Each packet is named by an opaque id (`PB-Basic-007-3f9a1c`)
   drawn from a seeded generator, and the id-to-origin key goes to `grading-key.json`, which graders never see.
3. A single call that submitted nothing (it reached the 128K-token limit, or stopped without writing a solution) is
   scored Incorrect (0) by the rubric's own rule ("(no proof submitted)" is Incorrect) and gets no packet
   (`auto-grades.json`).
4. The packets of one problem are shuffled and dealt into batches of at most 9 (`batches.json`), so a batch holds 8
   or 9 proofs of the same problem in random order, one of which may be the swarm's.
5. Each batch is graded by a fresh Claude Opus 5.5 agent (a Claude Code subagent). Its instructions, the prompt
   below with the batch's file list, are written to `prompts/<batch>.txt`; the agent was told to read that file and
   follow it, to read only the files it lists, and to write its JSON to `grades/<batch>.json`.
6. `grade_summary.py` un-blinds the grades with the key and prints the tables; `export_results.py` writes the
   per-problem pages in `docs/results/proofbench-basic/`.

Grading started while the runs were still going, problem by problem as soon as all 17 proofs of a problem were
finished. Graders saw no model names, no self-verification grades and no information about how a proof was produced.

## Prompt

```text
You are grading solutions for IMO-ProofBench (Basic set) as a strict, careful olympiad grader. This is a blind evaluation: grade on mathematical merit only.

For each file listed below, read the problem, the official reference solution, the official grading guidelines, and the candidate solution under "## Proof". Grade it as if it were a contest submission, into one category with a 0-7 score:

- Correct (7): complete and rigorous; all cases covered; anything the problem requires is proved (for "find/determine all", both that the answers work and that nothing else does).
- Almost (5-6): right approach and result with only minor gaps or slips, as described under "(Almost)" in the guidelines.
- Partial (1-4): meaningful progress matching the "(Partial)" items in the guidelines, but not a full solution.
- Incorrect (0): wrong, circular, or no meaningful progress. "(no proof submitted)" is Incorrect (0).

Rules:
- The files are different candidate solutions to the same problem. Grade each one on its own against the problem and the guidelines; do not compare them to each other, and do not assume any of them is better or worse.
- A correct final answer with a missing or invalid key step is not Correct.
- Check computations and claimed lemmas yourself when they matter. Small typos that do not affect the logic are not penalized.
- Read only the files listed here. Do not open any other files.

Files:
<one packet path per line>

Write ONLY a JSON object, no other text, in exactly this shape, to the file <grades/<batch>.json>:
{"<first packet id>": {"category": "Correct", "score": 7, "reason": "<one sentence>"}, ...}
with one entry per file above, keyed by the id in the file's first line. Then reply with only the number of solutions you graded.
```

The published category of a proof is derived from its score (7 Correct, 5–6 Almost, 1–4 Partial, 0 Incorrect).

## Limits

- One grader per proof, and the grader is a language model: grades can be wrong, and nobody re-checked them.
- A grader sees up to 9 proofs of the same problem in one context. It is told to grade each on its own, but the
  others may still influence it, in either direction.
- To regrade with people or another model, run `build_grading.py` on the raw runs and use the packets as they are.
