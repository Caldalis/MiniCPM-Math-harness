# Results

All numbers on this page were measured on October 9–10, 2026 with the released MiniCPM5-2B-Math weights
(SHA-256 `b412895e…3006`) and the official MiniCPM5-2B release (SHA-256 `14fb8e7f…402c`, identical to
`openbmb/MiniCPM5-2B` on Hugging Face). Answer samples and single-call proofs were generated with
[`eval/sample_avgk.py`](../eval/sample_avgk.py), swarm proofs with this repository's `minicpm-math bench` (v0.1.1),
and everything was scored and graded with the scripts in [`eval/`](../eval/), which write the files in
[`results/`](results/).

## Answer benchmarks: AIME 2025, AIME 2026, HMMT February 2026

### Protocol

- 16 independent samples per problem (**avg@16**), thinking on. Each sample may use the model's whole
  131,072-token context: `max_tokens` is 131,072 minus the prompt.
- Plain single calls: no forced finish and no loop guard. A sample ends at EOS or at the context limit, and a sample
  that reaches the limit counts as wrong.
- MiniCPM5-2B-Math at temperature 0.9 / top-p 0.95 (the setting it was evaluated with); MiniCPM5-2B at its
  recommended temperature 1.0 / top-p 0.95. `min_p = 0`; seed 20261008 + i for sample i.
- vLLM 0.27.1, BF16 weights and BF16 KV cache, RTX 4090s.
- Problems: AIME 2025 I+II (30, `opencompass/AIME2025` at revision `a6ad95f`, MIT), AIME 2026 (30,
  `MathArena/aime_2026` at `d2de22f`) and HMMT February 2026 (33, `MathArena/hmmt_feb_2026` at `02fba4f`); the two
  MathArena datasets are CC BY-NC-SA 4.0. `bench` loads the MathArena sets through the Hugging Face rows API, which
  serves the latest revision; on October 10, 2026 it served exactly the problems and answers above.
- The answer is the last `\boxed{}` of the final response. It is compared with the gold answer after
  normalization, then with symbolic equivalence (`math-verify`), and every symbolic "equal" is re-checked by exact
  simplification (floating-point comparison alone accepts wrong answers that differ by ~1e-29).
- **maj@16** is the majority answer of the samples that finished, with ties going to the answer that finished first
  (counted separately below); **pass@16** counts problems that at least one sample got right.

### Accuracy (%)

| Benchmark | Metric | MiniCPM5-2B | MiniCPM5-2B-Math |
|---|---|---:|---:|
| AIME 2025 | avg@16 (± s.e.) | 87.1 (± 0.9) | **92.3** (± 1.0) |
| | maj@16 | 93.3 | **100.0** |
| | pass@16 | 96.7 | **100.0** |
| AIME 2026 | avg@16 (± s.e.) | 89.8 (± 0.9) | 89.8 (± 0.8) |
| | maj@16 | 93.3 | 93.3 |
| | pass@16 | 96.7 | 96.7 |
| HMMT Feb 2026 | avg@16 (± s.e.) | 68.4 (± 1.2) | **81.8** (± 1.1) |
| | maj@16 | 75.8 | **90.9** |
| | pass@16 | 90.9 | **93.9** |

The standard error is that of the mean over 16 samples per problem (the problems themselves are fixed). It does not
cover the choice of problems, which matters more with 30 to 33 per test. A paired bootstrap over the problems
(`score_avgk.py`, 10,000 resamples) gives these 95% intervals for MiniCPM5-2B-Math minus MiniCPM5-2B:

| Benchmark | Gap in avg@16 | 95% interval, problems resampled |
|---|---:|---:|
| AIME 2025 | +5.2 | −0.6 to +11.9 |
| AIME 2026 | +0.0 | −6.2 to +4.8 |
| HMMT Feb 2026 | +13.4 | +7.2 to +20.4 |

For reference, the MiniCPM5-2B model card reports 86.5 / 86.5 / 63.8 under its own protocol.

### Details

| | AIME 2025 | | AIME 2026 | | HMMT Feb 2026 | |
|---|---:|---:|---:|---:|---:|---:|
| | base | Math | base | Math | base | Math |
| samples reaching 128K (counted wrong) | 0.0% | 0.8% | 0.0% | 0.2% | 1.5% | 2.8% |
| samples longer than 64K | 11.0% | 9.6% | 4.6% | 16.0% | 19.3% | 25.9% |
| … of which correct | 16 / 53 | 22 / 46 | 12 / 22 | 35 / 77 | 21 / 102 | 52 / 137 |
| avg@16 if capped at 64K | 83.8 | 87.7 | 87.3 | 82.5 | 64.4 | 72.0 |
| mean tokens per sample | 29.3K | 27.2K | 25.6K | 28.6K | 38.5K | 41.6K |
| median tokens per sample | 22.6K | 19.7K | 19.5K | 16.6K | 31.2K | 28.6K |
| tied votes (of which correct) | 0 | 0 | 0 | 1 (0) | 1 (0) | 0 |

What the numbers say:

- MiniCPM5-2B-Math is ahead of MiniCPM5-2B by 13.4 points on HMMT February 2026 and 5.2 points on AIME 2025, and
  level on AIME 2026 (89.8 each). Only the HMMT gap is clearly larger than what a different choice of problems could
  produce. With the vote it reaches 100 / 93.3 / 90.9 against 93.3 / 93.3 / 75.8.
- The long budget matters, and more for MiniCPM5-2B-Math: a quarter of its HMMT samples think past 64K tokens, and
  38% of those still end with the right answer. Capped at 64K (counting longer samples as wrong), its avg@16 would be
  87.7 / 82.5 / 72.0, and it would trail MiniCPM5-2B on AIME 2026. Give it the full context.
- AIME 2025 I-15 is the only AIME 2025 problem where most samples miss: 3 of 16 are right, but the wrong answers
  scatter, so the vote still picks the right one (3 votes against 2). The 100.0 maj@16 rests on such pluralities, not
  on every problem being easy for the model.
- All three tests were public before the model was post-trained, and overlap between its post-training data and
  these problems has not been ruled out.

### Reproduce

```bash
vllm serve Caldalis/MiniCPM5-2B-Math --max-model-len 131072 --port 8000      # one server per GPU
echo http://127.0.0.1:8000/v1 > servers.txt
python eval/sample_avgk.py --servers servers.txt --data aime25,aime26,hmmt26 -n 16 \
  --temperature 0.9 --top-p 0.95 --seed 20261008 --out RUNS16/math
python eval/score_avgk.py RUNS16 data --models math
# MiniCPM5-2B: serve openbmb/MiniCPM5-2B and use --temperature 1.0 --out RUNS16/base
python eval/score_avgk.py RUNS16 data      # both models, plus the gap and its interval
```

`data/` is written as shown in [eval/README.md](../eval/README.md). Expect many GPU-hours: at 30–130K tokens per
sample, decoding is limited by KV-cache memory (a 24 GB card holds about 425K tokens of BF16 KV cache, so only 3–15
long samples run at once). The answer runs behind this page took about 10 hours on 5 to 8 RTX 4090s.

## Proofs: IMO-ProofBench Basic (30 problems)

### Protocol

- All 30 problems of the Basic set of IMO-ProofBench (Luong et al., 2025; `google-deepmind/superhuman` at `80b2527`;
  problem statements Copyright 2025 Google LLC, CC BY 4.0). The paper describes the Basic set as mostly rephrased
  versions of existing problems, so overlap with the training data cannot be ruled out.
- **Single call (avg@16)**: 16 independent calls per problem with the harness' proof prompt without a strategy hint
  (the prompt of the swarm's first prover), up to the full 131,072-token context, no forced finish. A call that
  reaches the limit, or stops without writing a solution, submitted nothing and is graded Incorrect (0).
- **Swarm**: `minicpm-math bench proofbench-basic --mode prove --profile standard --max-tokens 131072`: 8 provers and
  up to 2 repair rounds with up to 128K tokens per call, 3 verifiers. In bench mode the whole first wave is generated
  and checked even after a candidate is accepted. Verifiers, lab and scribe keep the profile's budgets (16K, 8K,
  16K tokens) and the forced finish the harness uses to read their output.
- Same server settings as above (temperature 0.9, top-p 0.95, seed 20261008).
- **Blind grading**: every written proof (the 16 single calls and the swarm's proof per problem; the 5 calls without
  a write-up were scored 0 without grading) was graded on its own by an AI grader (Claude Opus 5.5) against the
  official reference solution and grading guidelines on the 0–7 scale. Each proof got an opaque id, and each grader
  saw up to 9 proofs of one problem in random order, with no information about how a proof was produced. No human
  review. The procedure and prompt are in [`eval/GRADING.md`](../eval/GRADING.md), and every proof, grade and reason
  is published in [`results/proofbench-basic/`](results/proofbench-basic/).
- **Not comparable with the IMO-ProofBench leaderboard.** The paper's results were graded by human experts, one sample
  per problem, and are reported as percentages of points. Ours come from one AI grader with our own prompt, count
  problems with full marks, and for the swarm use about 56 model calls per problem.
- **Complete proofs (single call)** is the sum over problems of the share of the 16 calls graded Correct (7), i.e. how
  many of the 30 problems one plain call solves on average.

### Results

| | Correct (7) | Almost (5–6) | Partial (1–4) | Incorrect (0) | Mean score |
|---|---:|---:|---:|---:|---:|
| single call (avg@16) | 21.0 | 2.2 | 2.9 | 3.9 | 5.48 / 7 |
| swarm | **23** | 2 | 2 | 3 | **5.83 / 7** |

For the single call, each column is the number of problems in that category for an average call (the mean over the
16 calls).

- With the full context a plain call is already strong on this set: on average it writes a complete proof for 21 of
  the 30 problems, and at least one of the 16 calls does so on 27 problems (pass@16). Only 5 of the 480 calls (1.0%)
  reached the 128K limit without a write-up. The hard problems are PB-Basic-006, 007, 009, 021, 023, 029 and 030,
  where at most 4 of the 16 calls are correct.
- The swarm returns one proof per problem, graded Correct on 23. Against the average single call it is better on 12
  problems and worse on 4 (PB-Basic-007, 009, 021, 029). It helps most where single calls are unreliable:
  PB-Basic-023 (2 of 16 calls correct; the swarm's proof Correct), PB-Basic-015 (7 of 16), PB-Basic-026 (9 of 16)
  and PB-Basic-022 (10 of 16).
- It does not reach every problem that some single call solves: on PB-Basic-007 and 009 it picked a wrong proof
  although 2 and 4 of the 16 calls were correct, and on PB-Basic-021 none of its candidates passed its own checks.
- **Self-verification**: the swarm marked 28 proofs `accepted`. 23 were graded Correct, 2 Almost (PB-Basic-011: a
  bound stated without justification; PB-Basic-030: the case AB ∥ CD left out) and 3 were not valid proofs
  (PB-Basic-007: the key step asserted as "a standard divisor-chain argument"; PB-Basic-009: the lower bound taken
  from the Manickam–Miklós–Singhi theorem, of which the problem is a special case; PB-Basic-029: a wrong answer). The
  two proofs it did not accept (PB-Basic-006, 021) were indeed wrong. A 2B model checking its own proofs is the weak
  point of the swarm; [how-it-works](how-it-works.md#5-verifiers-adversarial-independent-staged) shows how to plug in
  a stronger verifier.

### Cost

The swarm used 749K completion tokens and 56 model calls per problem on average (median 747K, at most 1.48M), about
16 times a single call (48.1K tokens on average, median 36.8K). Run as 6 problems per RTX 4090, sharing the GPUs with
the single-call runs, the median problem took 3.4 hours (at most 5.7). Interactive use is cheaper, because `prove`
stops at the first accepted candidate by default.

### Reproduce

```bash
python eval/sample_avgk.py --servers servers.txt --data proofbench-basic --prompt prover -n 16 \
  --temperature 0.9 --top-p 0.95 --seed 20261008 --out RUNS16/proof-single
minicpm-math bench data/proofbench-basic.jsonl --mode prove --profile standard --max-tokens 131072 \
  --seed 20261008 --jobs 6 --concurrency 48 --no-ui --out RUNS16/swarm
```

Then build the blind packets, grade them and write the result files as described in
[eval/README.md](../eval/README.md) and [eval/GRADING.md](../eval/GRADING.md).

## Citing the benchmarks

The licenses of the benchmark material in `results/` are listed in [results/README.md](results/README.md). If you use
these results, please cite the benchmarks:

```bibtex
@inproceedings{luong-etal-2025-towards,
    title = "Towards Robust Mathematical Reasoning",
    author  = {Thang Luong and Dawsen Hwang and Hoang H. Nguyen and Golnaz Ghiasi and Yuri Chervonyi and Insuk Seo and Junsu Kim and Garrett Bingham and Jonathan Lee and Swaroop Mishra and Alex Zhai and Clara Huiyi Hu and Henryk Michalewski and Jimin Kim and Jeonghyun Ahn and Junhwi Bae and Xingyou Song and Trieu H. Trinh and Quoc V. Le and Junehyuk Jung},
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    year = "2025",
    url = "https://aclanthology.org/2025.emnlp-main.1794/",
}

@article{dekoninck2026matharena,
      title={Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs},
      author={Jasper Dekoninck and Nikola Jovanović and Tim Gehrunger and Kári Rögnvaldsson and Ivo Petrov and Chenhao Sun and Martin Vechev},
      year={2026},
      eprint={2605.00674},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.00674},
}
```
