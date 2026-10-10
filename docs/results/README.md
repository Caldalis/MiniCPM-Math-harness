# Result files

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
  [google-deepmind/superhuman](https://github.com/google-deepmind/superhuman/tree/80b2527a0b4e4bfc6a8b28825fadbdcfdd6048a1/imobench), Copyright 2025 Google LLC, licensed under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and reproduced unchanged.
- The `gold` answers in `answers.json` come from [opencompass/AIME2025](https://huggingface.co/datasets/opencompass/AIME2025)
  (MIT) for AIME 2025, and from MathArena's [aime_2026](https://huggingface.co/datasets/MathArena/aime_2026) and
  [hmmt_feb_2026](https://huggingface.co/datasets/MathArena/hmmt_feb_2026) datasets (Dekoninck et al., 2026), licensed
  under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

How to cite the benchmarks is in [docs/results.md](../results.md#citing-the-benchmarks).
