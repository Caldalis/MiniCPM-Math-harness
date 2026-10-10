"""Streaming against fake servers: BOS handling of raw /completions prompts, and errors sent inside a stream."""

import asyncio
import json

import httpx
import pytest

from minicpm_math.client import Backend, BackendError
from minicpm_math.template import forced_finish_prompt, render_chat

MESSAGES = [{"role": "user", "content": "Prove it."}]


def n_tokens(text: str) -> int:
    return len(text.replace("<s>", "<s> ").split())


class FakeServer:
    """vLLM adds a BOS to /completions prompts (``adds_bos=True``); llama.cpp does not for this model."""

    def __init__(self, adds_bos: bool, usage: bool = True):
        self.adds_bos = adds_bos
        self.usage = usage
        self.probes = 0
        self.prompts = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        if not body.get("stream"):  # a probe: count prompt tokens
            self.probes += 1
            if request.url.path.endswith("/chat/completions"):
                thinking = (body.get("chat_template_kwargs") or {}).get("enable_thinking")
                n = n_tokens(render_chat(body["messages"], enable_thinking=thinking))
            else:
                n = n_tokens(body["prompt"]) + self.adds_bos
            return httpx.Response(200, json={"usage": {"prompt_tokens": n} if self.usage else None})
        self.prompts.append(body["prompt"])
        chunk = {"choices": [{"text": "Final proof.", "finish_reason": "stop"}], "usage": {"completion_tokens": 3}}
        return httpx.Response(200, text=f"data: {json.dumps(chunk)}\n\ndata: [DONE]\n\n",
                              headers={"content-type": "text/event-stream"})


def backend_for(server: FakeServer) -> Backend:
    backend = Backend("http://fake/v1", "fake-model")
    backend._client = httpx.AsyncClient(transport=httpx.MockTransport(server))
    backend._sem = asyncio.Semaphore(4)
    backend._probe_lock = asyncio.Lock()
    return backend


async def test_drops_its_bos_when_the_server_adds_one():
    server = FakeServer(adds_bos=True)
    backend = backend_for(server)
    prompt = forced_finish_prompt(MESSAGES, "some reasoning")
    for _ in range(2):
        gen = await backend.complete(prompt, max_tokens=8)
    assert gen.content == "Final proof."
    assert server.prompts == [prompt[len("<s>"):]] * 2
    assert await backend.raw_bos_doubled() and server.probes == 2  # probed once: one chat + one raw request


async def test_keeps_its_bos_when_the_server_adds_none():
    server = FakeServer(adds_bos=False)
    backend = backend_for(server)
    prompt = forced_finish_prompt(MESSAGES, "some reasoning")
    await backend.complete(prompt, max_tokens=8)
    assert server.prompts == [prompt] and not await backend.raw_bos_doubled()


async def test_unknown_token_counts_keep_the_bos_and_ask_again():
    server = FakeServer(adds_bos=True, usage=False)
    backend = backend_for(server)
    prompt = forced_finish_prompt(MESSAGES, "some reasoning")
    await backend.complete(prompt, max_tokens=8)
    await backend.complete(prompt, max_tokens=8)
    assert server.prompts == [prompt, prompt] and server.probes == 4


class ScriptedStream:
    """Answers each streamed request with the next list of server-sent events."""

    def __init__(self, *responses):
        self.responses = list(responses)
        self.bodies = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.bodies.append(json.loads(request.content))
        text = "".join(f"data: {json.dumps(event)}\n\n" for event in self.responses.pop(0)) + "data: [DONE]\n\n"
        return httpx.Response(200, text=text, headers={"content-type": "text/event-stream"})


THINKING = {"choices": [{"delta": {"reasoning_content": "Maybe the answer is \\boxed{12}."}}]}
ANSWER = [{"choices": [{"delta": {"content": "\\boxed{2}"}, "finish_reason": "stop"}]}, {"usage": {"completion_tokens": 5}}]


async def test_error_event_in_a_stream_raises():
    server = ScriptedStream([THINKING, {"error": {"message": "KV cache is full", "code": 503}}])
    backend = backend_for(server)
    backend.retries = 0
    with pytest.raises(BackendError) as info:
        await backend.chat(MESSAGES, max_tokens=64)
    assert info.value.status == 503 and "KV cache is full" in str(info.value)


async def test_error_event_without_a_status_is_retried_as_a_500(monkeypatch):
    sleep = asyncio.sleep

    async def no_backoff(delay, *args, **kwargs):
        await sleep(0)

    monkeypatch.setattr(asyncio, "sleep", no_backoff)
    server = ScriptedStream([THINKING, {"error": {"message": "engine died", "code": "internal_error"}}], ANSWER)
    gen = await backend_for(server).chat(MESSAGES, max_tokens=64)
    assert gen.content == "\\boxed{2}" and len(server.bodies) == 2  # the half-finished stream was not used


async def test_context_error_in_a_stream_retries_with_fewer_tokens():
    message = ("This model's maximum context length is 1000 tokens. However, you requested 1500 tokens "
               "(600 in the messages, 900 in the completion).")
    server = ScriptedStream([{"error": {"message": message, "code": 400}}], ANSWER)
    gen = await backend_for(server).chat(MESSAGES, max_tokens=900)
    assert gen.content == "\\boxed{2}" and [body["max_tokens"] for body in server.bodies] == [900, 336]
