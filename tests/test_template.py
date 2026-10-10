"""The raw renderer must reproduce the model's own chat_template.jinja byte for byte."""

from pathlib import Path

import pytest

from minicpm_math.template import forced_finish_prompt, render_chat

jinja2 = pytest.importorskip("jinja2")

TEMPLATE = (Path(__file__).parent / "fixtures" / "chat_template.jinja").read_text(encoding="utf-8")


def reference(messages, add_generation_prompt=True, **kwargs):
    env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, extensions=["jinja2.ext.loopcontrols"])
    env.filters["tojson"] = lambda x, ensure_ascii=False: __import__("json").dumps(x, ensure_ascii=ensure_ascii)
    return env.from_string(TEMPLATE).render(messages=messages, add_generation_prompt=add_generation_prompt,
                                            bos_token="<s>", tools=None, **kwargs)


CASES = [
    [{"role": "user", "content": "Prove that 1 + 1 = 2."}],
    [{"role": "system", "content": "You are a careful mathematician."}, {"role": "user", "content": "Find x."}],
    [
        {"role": "user", "content": "First question"},
        {"role": "assistant", "content": "<think>\nscratch\n</think>\n\nFirst answer"},
        {"role": "user", "content": "Second question"},
    ],
    [
        {"role": "user", "content": "Q"},
        {"role": "assistant", "content": "A", "reasoning_content": "because"},
    ],
]


@pytest.mark.parametrize("messages", CASES)
@pytest.mark.parametrize("thinking", [None, True, False])
def test_matches_jinja(messages, thinking):
    kwargs = {} if thinking is None else {"enable_thinking": thinking}
    assert render_chat(messages, enable_thinking=thinking) == reference(messages, **kwargs)


def test_no_generation_prompt():
    msgs = CASES[2]
    assert render_chat(msgs, add_generation_prompt=False) == reference(msgs, add_generation_prompt=False)


def test_forced_finish_shape():
    prompt = forced_finish_prompt([{"role": "user", "content": "Q"}], "partial reasoning   ")
    assert prompt.startswith("<s><|im_start|>user\nQ<|im_end|>\n<|im_start|>assistant\n<think>\npartial reasoning\n\n")
    assert prompt.endswith("\n</think>\n\n")
