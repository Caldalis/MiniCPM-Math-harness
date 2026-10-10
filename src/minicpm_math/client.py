"""Async client for OpenAI-compatible servers (vLLM, SGLang, llama.cpp, LM Studio, MLX-LM).

Only two endpoints are used: ``/chat/completions`` for normal turns and ``/completions``
for forced finishes (see :mod:`minicpm_math.template`). Responses are always streamed so
that the live dashboard can show progress and so that degenerate repetition loops can be
cut off early instead of burning the whole token budget.
"""

from __future__ import annotations

import asyncio
import json
import re
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Mapping, Optional

import httpx

from .parsing import split_reasoning
from .template import BOS, THINK_CLOSE, THINK_OPEN, render_chat

ProgressFn = Callable[[int, str], None]  # (completion tokens so far, "think" | "write")


@dataclass
class Generation:
    reasoning: str = ""
    content: str = ""
    finish_reason: Optional[str] = None  # "stop" | "length" | "loop" | "forced"
    prompt_tokens: int = 0
    completion_tokens: int = 0
    seconds: float = 0.0

    @property
    def truncated(self) -> bool:
        return self.finish_reason in ("length", "loop")

    @property
    def tokens_per_second(self) -> float:
        return self.completion_tokens / self.seconds if self.seconds > 0 else 0.0


class BackendError(RuntimeError):
    def __init__(self, message: str, status: Optional[int] = None):
        super().__init__(message)
        self.status = status


def looks_like_loop(tail: str, min_span: int = 1500, max_period: int = 800) -> bool:
    """True if the end of ``tail`` is one block repeated verbatim over ``min_span`` chars."""
    n = len(tail)
    if n < min_span:
        return False
    for period in range(8, min(max_period, n // 3) + 1):
        reps = max(3, -(-min_span // period))
        if reps * period > n:
            continue
        block = tail[-period:]
        if all(tail[-(k + 1) * period : -k * period] == block for k in range(1, reps)):
            return True
    return False


class Backend:
    """One model behind one OpenAI-compatible endpoint.

    ``thinking_kwarg`` sends ``chat_template_kwargs={"enable_thinking": ...}`` (understood by
    vLLM, SGLang and llama.cpp) and ``min_p`` is sent because llama.cpp's default of 0.05
    makes MiniCPM5 more prone to repetition. Turn both off for strict APIs that reject
    unknown fields.

    Raw prompts start with ``raw_bos``, as the chat template does. Servers that tokenize with
    Hugging Face tokenizers (vLLM and MLX-LM, for example) add a BOS of their own to ``/completions``
    prompts, so :meth:`complete` drops ours when :meth:`raw_bos_doubled` detects that.
    """

    def __init__(
        self,
        base_url: str,
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        *,
        concurrency: int = 8,
        timeout: float = 7200.0,
        thinking_kwarg: bool = True,
        min_p: Optional[float] = 0.0,
        extra_body: Optional[Mapping[str, Any]] = None,
        raw_bos: str = BOS,
        loop_guard: bool = True,
        retries: int = 2,
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.api_key = api_key
        self.concurrency = concurrency
        self.timeout = timeout
        self.thinking_kwarg = thinking_kwarg
        self.min_p = min_p
        self.extra_body = dict(extra_body or {})
        self.raw_bos = raw_bos
        self.loop_guard = loop_guard
        self.retries = retries
        self._client: Optional[httpx.AsyncClient] = None
        self._sem: Optional[asyncio.Semaphore] = None
        self._probe_lock: Optional[asyncio.Lock] = None
        self._bos_doubled: Optional[bool] = None

    # -- plumbing -----------------------------------------------------------------

    def _ensure(self) -> httpx.AsyncClient:
        if self._client is None:
            limits = httpx.Limits(max_connections=self.concurrency + 4, max_keepalive_connections=self.concurrency)
            self._client = httpx.AsyncClient(timeout=httpx.Timeout(self.timeout, connect=30.0), limits=limits)
            self._sem = asyncio.Semaphore(self.concurrency)
            self._probe_lock = asyncio.Lock()
        return self._client

    def _headers(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}

    async def aclose(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def model_name(self) -> str:
        if self.model:
            return self.model
        models = await self.list_models()
        if not models:
            raise BackendError(f"{self.base_url}/models returned no models; pass --model explicitly")
        self.model = models[0]
        return self.model

    async def list_models(self) -> List[str]:
        resp = await self._ensure().get(f"{self.base_url}/models", headers=self._headers())
        if resp.status_code >= 400:
            raise BackendError(f"{resp.status_code} from {self.base_url}/models: {resp.text[:300]}", resp.status_code)
        try:
            return [m["id"] for m in resp.json().get("data", [])]
        except (ValueError, KeyError, TypeError, AttributeError):  # e.g. a web page: not an OpenAI-compatible server
            raise BackendError(f"{self.base_url}/models returned no model list: {resp.text[:300]}",
                               resp.status_code) from None

    def _sampling(self, max_tokens: int, temperature: float, top_p: float, seed: Optional[int]) -> Dict[str, Any]:
        body: Dict[str, Any] = {
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "stream": True,
            "stream_options": {"include_usage": True},
        }
        if self.min_p is not None:
            body["min_p"] = self.min_p
        if seed is not None:
            body["seed"] = seed
        return body

    # -- public API ---------------------------------------------------------------

    async def chat(
        self,
        messages: List[Dict[str, str]],
        *,
        max_tokens: int,
        temperature: float = 0.9,
        top_p: float = 0.95,
        thinking: bool = True,
        seed: Optional[int] = None,
        on_progress: Optional[ProgressFn] = None,
    ) -> Generation:
        body = {"model": await self.model_name(), "messages": messages}
        body.update(self._sampling(max_tokens, temperature, top_p, seed))
        if self.thinking_kwarg:
            body["chat_template_kwargs"] = {"enable_thinking": thinking}
        body.update(self.extra_body)
        return await self._request("/chat/completions", body, thinking, on_progress)

    async def complete(
        self,
        prompt: str,
        *,
        max_tokens: int,
        temperature: float = 0.9,
        top_p: float = 0.95,
        seed: Optional[int] = None,
        on_progress: Optional[ProgressFn] = None,
    ) -> Generation:
        if self.raw_bos and prompt.startswith(self.raw_bos) and await self.raw_bos_doubled():
            prompt = prompt[len(self.raw_bos):]  # the server adds the BOS itself
        body = {"model": await self.model_name(), "prompt": prompt}
        body.update(self._sampling(max_tokens, temperature, top_p, seed))
        body.update(self.extra_body)
        return await self._request("/completions", body, False, on_progress)

    async def raw_bos_doubled(self) -> bool:
        """True if ``/completions`` adds its own BOS in front of a raw prompt that already starts with one.

        The same turn is sent through ``/chat/completions``, rendered by the server's template, and through
        ``/completions``, rendered by :func:`render_chat`: one extra prompt token means a second BOS. A doubled
        BOS also breaks prefix caching, because the forced-finish prompt no longer matches the cached turn.
        """
        self._ensure()
        assert self._probe_lock is not None
        async with self._probe_lock:
            if self._bos_doubled is None and self.raw_bos:
                messages = [{"role": "user", "content": "What is 1 + 1?"}]
                chat: Dict[str, Any] = {"messages": messages}
                if self.thinking_kwarg:
                    chat["chat_template_kwargs"] = {"enable_thinking": True}
                raw = render_chat(messages, enable_thinking=True if self.thinking_kwarg else None, bos=self.raw_bos)
                n_chat = await self._prompt_tokens("/chat/completions", chat)
                n_raw = await self._prompt_tokens("/completions", {"prompt": raw})
                if n_chat and n_raw:  # otherwise ask again next time
                    self._bos_doubled = n_raw == n_chat + 1
        return bool(self._bos_doubled)

    # -- internals ----------------------------------------------------------------

    async def _prompt_tokens(self, path: str, body: Dict[str, Any]) -> Optional[int]:
        body = dict(body, model=await self.model_name(), max_tokens=1, temperature=0.0, stream=False)
        try:
            resp = await self._ensure().post(f"{self.base_url}{path}", json=body, headers=self._headers())
            return int(resp.json()["usage"]["prompt_tokens"]) if resp.status_code < 400 else None
        except (httpx.HTTPError, ValueError, KeyError, TypeError):
            return None

    async def _request(self, path: str, body: Dict[str, Any], thinking: bool, on_progress: Optional[ProgressFn]) -> Generation:
        self._ensure()
        assert self._sem is not None
        async with self._sem:
            attempt = 0
            while True:
                try:
                    return await self._stream(path, body, thinking, on_progress)
                except BackendError as err:
                    shrunk = _shrink_for_context(err, body)
                    if shrunk is not None:
                        body = shrunk
                        continue
                    if err.status not in (429, 500, 502, 503, 504) or attempt >= self.retries:
                        raise
                except (httpx.TransportError, json.JSONDecodeError):
                    if attempt >= self.retries:
                        raise
                attempt += 1
                await asyncio.sleep(2.0 * attempt)

    async def _stream(self, path: str, body: Dict[str, Any], thinking: bool, on_progress: Optional[ProgressFn]) -> Generation:
        url = f"{self.base_url}{path}"
        reasoning_parts: List[str] = []
        content_parts: List[str] = []
        tail = ""
        chunks = 0
        usage: Dict[str, Any] = {}
        finish: Optional[str] = None
        start = time.monotonic()
        if on_progress:
            on_progress(0, "think" if thinking else "write")
        async with self._ensure().stream("POST", url, json=body, headers=self._headers()) as resp:
            if resp.status_code >= 400:
                text = (await resp.aread()).decode("utf-8", errors="replace")
                raise BackendError(f"{resp.status_code} from {url}: {text[:600]}", resp.status_code)
            async for line in resp.aiter_lines():
                if not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                if not data:
                    continue
                event = json.loads(data)
                if event.get("error"):
                    # a request that fails after streaming has started (e.g. llama.cpp with a full KV cache) ends here
                    raise _stream_error(url, event["error"])
                if event.get("usage"):
                    usage = event["usage"]
                for choice in event.get("choices") or []:
                    delta = choice.get("delta") or {}
                    think_piece = delta.get("reasoning_content") or delta.get("reasoning") or ""
                    text_piece = delta.get("content") or choice.get("text") or ""
                    if think_piece:
                        reasoning_parts.append(think_piece)
                    if text_piece:
                        content_parts.append(text_piece)
                    if think_piece or text_piece:
                        chunks += 1
                        tail = (tail + think_piece + text_piece)[-6000:]
                    if choice.get("finish_reason"):
                        finish = choice["finish_reason"]
                if on_progress and chunks and chunks % 16 == 0:
                    in_answer = bool(content_parts) and (bool(reasoning_parts) or not thinking or THINK_CLOSE in tail)
                    on_progress(chunks, "write" if in_answer else "think")
                if self.loop_guard and chunks and chunks % 256 == 0 and looks_like_loop(tail):
                    finish = "loop"
                    break

        reasoning, content = "".join(reasoning_parts), "".join(content_parts)
        if not reasoning and (THINK_CLOSE in content or content.lstrip().startswith(THINK_OPEN)):
            reasoning, content = split_reasoning(content)
        elif not reasoning and thinking and finish in ("length", "loop", None):
            # The template opened <think> for the model and it never closed it.
            reasoning, content = content, ""
        return Generation(
            reasoning=reasoning,
            content=content,
            finish_reason=finish,
            prompt_tokens=int(usage.get("prompt_tokens") or 0),
            completion_tokens=int(usage.get("completion_tokens") or chunks),
            seconds=time.monotonic() - start,
        )


def _stream_error(url: str, error: Any) -> BackendError:
    """The ``{"error": ...}`` event a server streams instead of more tokens; its ``code`` is the status (else 500)."""
    code = error.get("code") if isinstance(error, dict) else None
    status = code if isinstance(code, int) and not isinstance(code, bool) else 500
    message = error.get("message", error) if isinstance(error, dict) else error
    return BackendError(f"{status} from {url} (in the stream): {str(message)[:600]}", status)


def _shrink_for_context(err: BackendError, body: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """If the server rejected the request for exceeding its context, retry with fewer max_tokens."""
    if err.status != 400 or "context" not in str(err).lower():
        return None
    message = str(err)
    current = int(body.get("max_tokens") or 0)
    limit = re.search(r"maximum context length is (\d+)", message)
    used = re.search(r"\((\d+) in the messages", message) or re.search(r"(\d+) input tokens", message)
    if limit and used:
        target = int(limit.group(1)) - int(used.group(1)) - 64
    else:
        target = current // 2
    if target < 256 or target >= current:
        return None
    return dict(body, max_tokens=target)
