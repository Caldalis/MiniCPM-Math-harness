# eval: from raw runs to the published numbers

[docs/results.md](../docs/results.md) reports numbers that were computed from raw runs with the scripts in this
directory. They need the harness with the math extra (`pip install -e ".[math]"`). The raw runs themselves (the full
text of every sample) are too large for the repository.

| Step | Command | Output |
|---|---|---|
| 1. Serve the model | `vllm serve <model> --max-model-len 131072` (BF16 weights and KV cache), one server per GPU | |
| 2. Answer samples | `python eval/sample_avgk.py --servers servers.txt --data aime25,aime26,hmmt26 -n 16 --temperature 0.9 --top-p 0.95 --seed 20261008 --out RUNS16/math` (MiniCPM5-2B: `--temperature 1.0 --out RUNS16/base`) | `samples.jsonl`, `traces/` |
| 3. Score them | `python eval/score_avgk.py RUNS16 data` | avg@16, maj@16, pass@16, hit-128K rate and lengths per model and benchmark, and the gap between the two models with a 95% interval from a paired bootstrap over the problems |
| 4. Single-call proofs | `python eval/sample_avgk.py --servers servers.txt --data proofbench-basic --prompt prover -n 16 --temperature 0.9 --top-p 0.95 --seed 20261008 --out RUNS16/proof-single` | `samples.jsonl`, `traces/` |
| 5. Swarm proofs | `minicpm-math bench data/proofbench-basic.jsonl --mode prove --profile standard --max-tokens 131072 --seed 20261008 --out RUNS16/swarm` | `bench-*-proofbench-basic/` |
| 6. Blind packets | `python eval/build_grading.py RUNS16/proof-single RUNS16/swarm data/proofbench-basic.jsonl GRADING` | `packets/`, `batches.json`, `grading-key.json`, `auto-grades.json` |
| 7. Grade | one AI grader per batch, with the prompt in [GRADING.md](GRADING.md) | `GRADING/grades/*.json` |
| 8. Un-blind and summarize | `python eval/grade_summary.py GRADING` | the proof tables |
| 9. Write the public files | `python eval/export_results.py RUNS16 GRADING data docs/results` | `docs/results/` |

`data/<name>.jsonl` holds one benchmark as loaded by `minicpm_math.bench.load_items(name)`, one JSON object per line:

```bash
mkdir -p data
for b in aime25 aime26 hmmt26 proofbench-basic; do
  python -c "import json, sys; from minicpm_math.bench import load_items
for item in load_items(sys.argv[1]): print(json.dumps(item, ensure_ascii=False))" $b > data/$b.jsonl
done
```

`servers.txt` lists one OpenAI-compatible base URL per line (`http://host:port/v1`).

## What `sample_avgk.py` measures

Each sample is one plain chat request: the harness' solver prompt (or, with `--prompt prover`, its proof prompt
without a strategy hint), thinking on, `min_p = 0`, seed `20261008 + i` for sample `A{i+1}`, and `max_tokens` set to
the whole remaining context (131,072 minus the prompt). There is no forced finish and no loop guard: a sample ends at
EOS or at the context limit. `score_avgk.py` counts a sample as correct only if it ended on its own and its
`\boxed{}` answer matches the gold one (normalized strings, then symbolic equivalence with `math-verify`, re-checked
by exact simplification), so a sample that reaches the limit counts as unanswered, as it would for one API call.

The sampler spreads the samples of every problem over all servers and gives a server new work only while vLLM's
queue on it is short, so the KV cache stays full; `--order` (a JSON map from `dataset/id` to a priority) only decides
which problems start first. None of this changes what a sample is: the same 16 requests sent one at a time to one
server are the same measurement.

The swarm (step 5) is the harness itself, unchanged except for `--max-tokens 131072`, which raises the budget of
provers and refiners to the full context. Its verifiers, lab and scribe keep the `standard` profile's budgets and
the forced finish that the harness uses to read their output.
