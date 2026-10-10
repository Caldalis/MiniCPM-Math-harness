# How MiniCPM-Math works

MiniCPM-Math is a test-time harness: it does not change the model, it changes how the model is used. Two modes
share the same machinery.

- `prove` searches for a complete proof: provers → (scribe) → screening verifier → lab → confirming verifiers →
  refiners → selection.
- `solve` finds a final answer: chain-of-thought solvers and program-aided coders vote.

Everything talks to an OpenAI-compatible server, so the same code runs against vLLM on a GPU node or llama.cpp on a
laptop. The concurrency limit (`--concurrency`) is the only thing that has to match the hardware.

## Design principle: fix the failures you have measured

Before writing the harness we went through the single-shot evaluation log of MiniCPM5-2B-Math (8 rounds of tests
on October 6–7, 2026; see the README's Results section). The failures were not random. Each stage below exists
because of a specific observation.

### 1. Provers with diverse strategy hints

`N` provers attack the problem in parallel at temperature 0.9. Prover *i* gets the *i*-th of eight optional
"angles" (none, small cases, invariants, extremal/contradiction, induction, algebraic inequalities, double
counting, construction-first), each phrased as "use it only if it helps".

*Why:* sampling the same small model many times gives correlated errors. A swarm is only useful if its members
fail differently. Strategy hints are a cheap way to decorrelate them.

### 2. Forced finish

When a reasoning trace hits its token limit (or the loop guard fires), the harness re-opens the assistant turn
through the raw `/completions` endpoint, appends a short first-person note ("I am out of thinking budget, I will
write the final solution now"), closes `</think>` and lets the model write its answer conditioned on everything it
already derived. Thanks to prefix caching, this costs little more than the answer itself.

*Why:* at 16–32K tokens, many test problems never reached an answer (AIME 2025 I #10; five AMO problems at 32K;
all three Putnam problems at 24K). Discarding that work wastes most of the compute.

This requires reproducing the model's chat template exactly; `template.py` mirrors `chat_template.jinja`, and a
test checks it byte for byte against the Jinja original. The prompt also has to match token for token: servers that
tokenize with Hugging Face tokenizers put their own BOS in front of a `/completions` prompt (checked with vLLM 0.27.1
and MLX-LM 0.32.0), while llama.cpp does not for this model. The harness sends the same short turn through
`/chat/completions` and `/completions` once per server, and drops its own BOS when the second comes back one token
longer. Before v0.1.1 it did not: on vLLM, forced-finish prompts started with two BOS tokens, and since they no
longer matched the cached turn, prefix caching reused 8% of the prompt instead of 94% in a test on vLLM 0.27.1.
Re-running the forced finishes of an earlier 64K-token evaluation (223 truncated samples) with one BOS instead of
two changed the number of correct answers by less than the spread between repeated draws of the same prompt.

### 3. Scribe

If the final write-up is under 600 characters, or it came from a forced finish, a scribe agent receives the
problem, the trace (head and tail kept when it is long) and the draft, and writes the complete proof that the trace
supports. A rewrite of a thin draft is used only if it is longer than the draft; a rewrite of a forced finish only
has to be substantial (400+ characters).

An earlier version also fired when the write-up was short *relative to the reasoning* (under 5% of its length).
On IMO-ProofBench Basic that rule fired for 11 of 29 attempts, mostly on complete proofs that simply followed long
reasoning, and in one case the rewrite dropped a justification the original had. That rule was removed.

*Why:* this was the most striking pattern in the log. On newly written proof problems the reasoning contained the
key valid argument, but the final answer omitted steps, contained slips, or was cut off. On one AMO problem the
correct proof was only in the reasoning text.

### 4. Lab: brute force as evidence

For every candidate that survives screening (and for every candidate picked for repair), a lab agent writes one
Python program that recomputes the checkable claims (final formula, identities, counts, constructions) on small
cases from the problem's definitions, printing `PASS:` / `FAIL:` lines. The harness executes it in a subprocess
(timeout, CPU-time limit, a memory limit on Linux, empty working directory, clean environment) and shows the output
to the confirming verifiers and the refiners.

*Why:* on two harder new problems the model finished and wrote plausible general formulas that were wrong on
specific values (a frequency of 1363 instead of 1364; 15/30 instead of 17/29). A small model cannot reliably spot
an off-by-one by reading. A loop over small cases spots it immediately.

The lab is evidence, not a veto: the script itself can be buggy, and the verifier prompt says so.

The lab keeps thinking on. We tried writing checks with thinking off to save tokens. This model is trained to
think first, and without thinking it wrote its reasoning into the code block and produced programs that did not
run. A capped thinking budget plus forced finish works better.

### 5. Verifiers: adversarial, independent, staged

Each verifier is a fresh call with a "find mistakes, not praise" prompt. It lists issues as `[CRITICAL]` or `[GAP]`
and ends with a 0–7 olympiad grade in `\boxed{}`, because `\boxed{}` is the output format this model produces most
reliably. Rules applied on top:

- A grade above 4 is capped at 4 if the verifier itself listed a `[CRITICAL]` issue (small models often write a
  damning review and then a high grade).
- An unreadable grade counts as 0.
- A candidate is **accepted** only if all `k` verifiers give at least `--accept-grade` (default 6).
- Verification is staged: one verifier screens each candidate; the lab and the remaining `k-1` verifiers run only
  if it passes. The lab is the most expensive check (a thinking trace plus a program), so it is spent only on
  candidates that already look right.

*Why:* the model is a weak grader on its own (1 of 3 valid labels matched on an IMO-GradingBench sample, and strict
label formatting succeeded only once in four tries). Unanimity across independent samples, structured issue lists,
the consistency cap and computational evidence make false acceptance much less likely, though not impossible.
Measured on IMO-ProofBench Basic with 128K-token provers: of the 28 proofs the swarm accepted, a blind AI grader
(Claude Opus 5.5) graded 23 correct, 2 almost correct and 3 not valid, among them one that rested on citing a theorem of
which the problem is a special case (see [results](results.md#proofs-imo-proofbench-basic-30-problems)). For a
stronger guarantee, use an external verifier (`--verifier-base-url`, `--verifier-model`), e.g. a larger open model
on another server.

### 6. Refiners

After the first wave, the top `--refine-top` unaccepted candidates (ranked by mean grade, then minimum grade) are
sent to refiners together with all verifier reports, the lab output and part of the original reasoning. A refiner
must output a full corrected proof, or start over with a different approach if the current one cannot be repaired.
Refined candidates go through the same scribe → screen → lab → confirm pipeline. This repeats for `--rounds` rounds.

### 7. Selection and stopping

The first wave stops as soon as a candidate is accepted; with `--no-early-stop`, which `bench` uses, it runs to the
end so that every prover is checked. No repair round starts once a candidate is accepted. A run also ends when all
rounds are used, or at the `--budget` cap, which is soft: no new call starts after it, and calls already running
finish. The returned proof is the best-ranked candidate, labeled `accepted`, `unverified`, or `failed`. Ranking:
accepted first; then candidates whose final `\boxed{}` answer agrees with the most common answer among all
candidates; then mean grade, minimum grade, and a clean lab check (at least one `PASS`, no `FAIL`). The middle
tie-breakers matter in practice: a lenient verifier can give every candidate 7/7, and agreement between attempts is a
signal that does not depend on the verifier. The rule has a known weakness: agreement ranks above the mean grade, and
when the candidates' answers form two or more groups, a candidate without a short boxed answer counts as not
agreeing, so a lower-graded proof can win. It is kept in 0.1.x because the published runs used it (see the
CHANGELOG).

## Answer mode

`solve` runs `--solvers` chain-of-thought agents with the prompt the model was trained on ("Please reason step by
step, and put your final answer within `\boxed{}`") and optionally `--coders` program-aided agents, whose programs
are executed and whose printed result is their vote. Answers are normalized (`\dfrac{6}{8}`, `0.75` and `3/4` are
the same vote) and counted. The run stops as soon as the leader cannot be overtaken by the remaining votes. A tie
is broken by finishing order and reported as `tied`; `bench` counts tied wins separately, because they are luck,
not consensus.

For benchmarking, early stopping is off by default so that `pass@1`, `maj@k` and `pass@k` are all unbiased
estimates from the same samples.

## Loop guard

Every 256 streamed chunks the client checks whether the last ~1,500 characters are a single block repeated
verbatim. If so, it closes the stream (the server aborts the request) and the call is force-finished like a
truncated one. This saves a lot of time on laptops, where a looping 32K-token trace can take 15 minutes.

## Run directories

Each run writes `problem.md`, `config.json`, `calls.jsonl` (every request with its full reasoning and answer),
`events.jsonl` (every executed program and its output), `result.json`, and `final.md` (the proof or answer with
grades, candidate table and verifier reports). Nothing is summarized away: a result is only as good as the trail
that supports it.

## Costs, roughly

With the `standard` profile, a problem that is solved in the first wave costs about `8 provers + 8 screening
verifiers + (1 lab + 2 confirming verifiers) per surviving candidate` calls, and the run stops at the first
accepted candidate. Most calls stop well before their budget on easy problems. For throughput: in our tests,
vLLM decoded about 155 tok/s for a single stream on one RTX 4090, and about 900 tok/s in total across five 4090s
with up to 10 concurrent long requests; an Apple M5 laptop with llama.cpp and 4 slots managed about 125 tok/s
in total.
