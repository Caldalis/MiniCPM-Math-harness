#!/usr/bin/env python3
"""Plain avg@k sampling for answer benchmarks, spread over several vLLM servers.

Every sample is one chat request with the harness' solver prompt, sampling settings and seed scheme (seed + i for
sample A{i+1}), i.e. what `minicpm-math bench -n K --no-force-finish` sends, with three differences that make it a
plain single-call measurement at the model's full context:

  * no forced finish and no loop guard: a sample ends at EOS or at the context limit, nothing else;
  * max_tokens is the whole remaining context (max_model_len minus the prompt);
  * samples are dispatched one at a time to whichever server has room, hardest problems first, so the samples of
    one problem are spread over all GPUs instead of queueing on one.

A server gets a new sample while it has fewer than --max-inflight in flight and at most --max-waiting requests
waiting in vLLM's queue (from /metrics), which keeps its KV cache full without piling up preempted requests.
The server list is re-read every poll, so servers can be added or drained while it runs. Finished samples are
appended to OUT/samples.jsonl (the run resumes from it) and full texts go to OUT/traces/.

Run it from a directory with data/<dataset>.jsonl ({"id", "problem", "answer"} per line, as written by
`minicpm_math.bench.load_items`).

usage: python eval/sample_avgk.py --servers FILE --data aime25,aime26,hmmt26 --order FILE -n 16 \
                                  --temperature 0.9 --top-p 0.95 --seed 20261008 --out runs16/math
"""
from __future__ import annotations

import argparse
import asyncio
import gzip
import json
import re
import time
from pathlib import Path

import httpx

from minicpm_math import __version__, prompts
from minicpm_math.client import Backend
from minicpm_math.parsing import last_boxed

METRIC = re.compile(r"^(vllm:[a-z_]+)(\{[^}]*\})?\s+(\S+)$")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--servers", required=True, help="file with one base URL (http://host:port/v1) per line")
    p.add_argument("--data", default="aime25,aime26,hmmt26", help="datasets under data/<name>.jsonl")
    p.add_argument("--order", help="JSON {\"ds/id\": priority}; higher runs first")
    p.add_argument("--prompt", choices=["solver", "prover"], default="solver",
                   help="solver: answer prompt; prover: proof prompt without a strategy hint (the swarm's P1)")
    p.add_argument("-n", type=int, default=16)
    p.add_argument("--temperature", type=float, default=0.9)
    p.add_argument("--top-p", type=float, default=0.95)
    p.add_argument("--seed", type=int, default=20261008)
    p.add_argument("--max-model-len", type=int, default=131072)
    p.add_argument("--max-inflight", type=int, default=48, help="per server")
    p.add_argument("--max-waiting", type=int, default=1, help="dispatch only while vLLM's queue is this short")
    p.add_argument("--burst", type=int, default=4, help="max new samples per server per poll")
    p.add_argument("--poll", type=float, default=2.0)
    p.add_argument("--out", required=True)
    return p.parse_args()


async def server_load(client: httpx.AsyncClient, url: str):
    """(running, waiting, kv usage) from vLLM's Prometheus endpoint, or None if it does not answer."""
    try:
        resp = await client.get(url.rsplit("/v1", 1)[0] + "/metrics", timeout=10)
    except httpx.HTTPError:
        return None
    vals: dict = {}
    for line in resp.text.splitlines():
        m = METRIC.match(line)
        if m:
            try:
                vals[m.group(1)] = vals.get(m.group(1), 0.0) + float(m.group(3))
            except ValueError:
                pass
    return (vals.get("vllm:num_requests_running", 0.0), vals.get("vllm:num_requests_waiting", 0.0),
            vals.get("vllm:kv_cache_usage_perc", vals.get("vllm:gpu_cache_usage_perc", 0.0)))


async def main() -> None:
    args = parse_args()
    out = Path(args.out)
    (out / "traces").mkdir(parents=True, exist_ok=True)
    samples_path = out / "samples.jsonl"
    done = set()
    if samples_path.exists():
        for line in open(samples_path):
            r = json.loads(line)
            if "error" not in r:
                done.add((r["ds"], r["id"], r["i"]))
    problems = {}
    for ds in args.data.split(","):
        for line in open(f"data/{ds}.jsonl"):
            item = json.loads(line)
            problems[(ds, item["id"])] = item
    order = json.load(open(args.order)) if args.order else {}
    queue = [(ds, pid, i) for (ds, pid) in problems for i in range(args.n) if (ds, pid, i) not in done]
    queue.sort(key=lambda x: (-order.get(f"{x[0]}/{x[1]}", 0.0), x[0], x[1], x[2]))
    queue.reverse()  # pop() from the end
    (out / "config.json").write_text(json.dumps({k: v for k, v in vars(args).items()} | {
        "harness_version": __version__, "force_finish": False, "loop_guard": False,
        "prompt": f"minicpm_math.prompts.{args.prompt}", "started": time.strftime("%Y-%m-%d %H:%M:%S")}, indent=2))
    print(f"{len(done)} samples already done, {len(queue)} to go", flush=True)

    backends: dict = {}
    inflight: dict = {}
    prompt_tokens: dict = {}
    retries: dict = {}
    tasks: set = set()
    write_lock = asyncio.Lock()
    stats = {"done": len(done), "tokens": 0, "errors": 0, "t0": time.time()}
    metrics_client = httpx.AsyncClient()

    def backend(url: str) -> Backend:
        if url not in backends:
            backends[url] = Backend(url, concurrency=args.max_inflight + 8, timeout=6 * 3600.0, min_p=0.0,
                                    raw_bos=None, loop_guard=False, retries=0)
            inflight[url] = 0
        return backends[url]

    async def run(url: str, key) -> None:
        ds, pid, i = key
        item = problems[(ds, pid)]
        messages = prompts.solver(item["problem"]) if args.prompt == "solver" else prompts.prover(item["problem"])
        b = backend(url)
        t_start = time.time()
        row = {"ds": ds, "id": pid, "i": i, "agent": f"A{i + 1}", "seed": args.seed + i, "server": url}
        try:
            if (ds, pid) not in prompt_tokens:
                n = await b._prompt_tokens("/chat/completions",
                                           {"messages": messages, "chat_template_kwargs": {"enable_thinking": True}})
                if not n:
                    raise RuntimeError("could not count prompt tokens")
                prompt_tokens[(ds, pid)] = n
            max_tokens = args.max_model_len - prompt_tokens[(ds, pid)]
            gen = await b.chat(messages, max_tokens=max_tokens, temperature=args.temperature, top_p=args.top_p,
                               thinking=True, seed=args.seed + i)
        except Exception as exc:  # requeue on another poll; the sample restarts from scratch
            row["error"] = repr(exc)[:500]
            stats["errors"] += 1
            retries[key] = retries.get(key, 0) + 1
            if retries[key] <= 3:
                queue.append(key)
        else:
            answer = last_boxed(gen.content) if gen.content else last_boxed(gen.reasoning[-2000:])
            row.update(answer=answer, finish=gen.finish_reason, completion_tokens=gen.completion_tokens,
                       prompt_tokens=gen.prompt_tokens, max_tokens=max_tokens, has_content=bool(gen.content.strip()),
                       seconds=round(gen.seconds, 1))
            trace = out / "traces" / ds / str(pid)
            trace.mkdir(parents=True, exist_ok=True)
            with gzip.open(trace / f"A{i + 1}.json.gz", "wt", encoding="utf-8") as fh:
                json.dump({**row, "reasoning": gen.reasoning, "content": gen.content}, fh, ensure_ascii=False)
            stats["done"] += 1
            stats["tokens"] += gen.completion_tokens
        finally:
            inflight[url] -= 1
        row.update(t_start=round(t_start, 1), t_end=round(time.time(), 1))
        async with write_lock:
            with open(samples_path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    last_status = 0.0
    while queue or tasks:
        servers = [s.strip() for s in open(args.servers) if s.strip() and not s.startswith("#")]
        loads = await asyncio.gather(*(server_load(metrics_client, s) for s in servers))
        for url, load in zip(servers, loads):
            backend(url)
            if load is None:
                continue
            running, waiting, kv = load
            room = min(args.burst, args.max_inflight - inflight[url])
            if waiting > args.max_waiting:
                room = 0
            for _ in range(max(0, room)):
                if not queue:
                    break
                key = queue.pop()
                inflight[url] += 1
                task = asyncio.create_task(run(url, key))
                tasks.add(task)
                task.add_done_callback(tasks.discard)
        now = time.time()
        if now - last_status > 30:
            last_status = now
            status = {"time": time.strftime("%H:%M:%S"), "queued": len(queue), "inflight": sum(inflight.values()),
                      "done": stats["done"], "errors": stats["errors"], "tokens": stats["tokens"],
                      "tok_per_s": round(stats["tokens"] / max(1.0, now - stats["t0"])),
                      "servers": {u: {"inflight": inflight.get(u, 0),
                                      "load": None if l is None else [int(l[0]), int(l[1]), round(l[2], 3)]}
                                  for u, l in zip(servers, loads)}}
            (out / "status.json").write_text(json.dumps(status, indent=1))
            print(json.dumps({k: status[k] for k in ("time", "queued", "inflight", "done", "errors", "tok_per_s")}),
                  flush=True)
        await asyncio.sleep(args.poll)
    for b in backends.values():
        await b.aclose()
    await metrics_client.aclose()
    print("all samples done", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
