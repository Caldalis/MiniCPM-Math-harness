"""Raw prompt rendering for MiniCPM5 models.

The harness talks to inference servers through the OpenAI chat API whenever it can.
Raw prompts are needed for one trick only: when a reasoning trace hits its token
limit, we re-open the assistant turn ourselves, close the ``<think>`` block and let
the model write its final answer conditioned on everything it already thought
("forced finish"). That requires producing exactly the string the model's chat
template would have produced, so this module mirrors ``chat_template.jinja`` for
the plain-chat case (system / user / assistant, no tools).
"""

from __future__ import annotations

from typing import Iterable, Mapping, Optional

BOS = "<s>"
IM_START = "<|im_start|>"
IM_END = "<|im_end|>"
THINK_OPEN = "<think>"
THINK_CLOSE = "</think>"

# Appended to a truncated reasoning trace before closing it. Phrased in the model's
# own first-person voice so the transition reads like a natural end of thinking.
FINISH_NUDGE = (
    "I am out of thinking budget. I will stop exploring now and write the final "
    "solution, using only what I have already established above."
)


def render_chat(
    messages: Iterable[Mapping[str, str]],
    *,
    add_generation_prompt: bool = True,
    enable_thinking: Optional[bool] = None,
    bos: str = BOS,
) -> str:
    """Render ``messages`` the way MiniCPM5's chat template does (no tools)."""
    msgs = list(messages)
    out = [bos]
    if msgs and msgs[0]["role"] == "system":
        out.append(f"{IM_START}system\n{msgs[0]['content']}{IM_END}\n")

    last_query = len(msgs) - 1
    for i in range(len(msgs) - 1, -1, -1):
        if msgs[i]["role"] == "user":
            last_query = i
            break

    for i, msg in enumerate(msgs):
        role, content = msg["role"], msg.get("content") or ""
        if role == "user" or (role == "system" and i > 0):
            out.append(f"{IM_START}{role}\n{content}{IM_END}\n")
        elif role == "assistant":
            reasoning = msg.get("reasoning_content")
            if not isinstance(reasoning, str):
                reasoning = ""
                if THINK_CLOSE in content:
                    reasoning = content.split(THINK_CLOSE)[0].rstrip("\n").split(THINK_OPEN)[-1].lstrip("\n")
                    content = content.split(THINK_CLOSE)[-1].lstrip("\n")
            if i > last_query and reasoning:
                out.append(
                    f"{IM_START}assistant\n{THINK_OPEN}\n{reasoning.strip(chr(10))}\n{THINK_CLOSE}\n\n"
                    + content.lstrip("\n")
                )
            else:
                out.append(f"{IM_START}assistant\n{content}")
            out.append(f"{IM_END}\n")

    if add_generation_prompt:
        out.append(f"{IM_START}assistant\n")
        if enable_thinking is False:
            out.append(f"{THINK_OPEN}\n\n{THINK_CLOSE}\n\n")
        elif enable_thinking is True:
            out.append(f"{THINK_OPEN}\n")
    return "".join(out)


def forced_finish_prompt(
    messages: Iterable[Mapping[str, str]],
    reasoning: str,
    *,
    nudge: str = FINISH_NUDGE,
    bos: str = BOS,
) -> str:
    """Prompt that resumes a truncated thinking trace, closes it, and asks for the answer."""
    prefix = render_chat(messages, add_generation_prompt=True, enable_thinking=True, bos=bos)
    return f"{prefix}{reasoning.rstrip()}\n\n{nudge}\n{THINK_CLOSE}\n\n"
