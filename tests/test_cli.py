"""Command-line behaviour that needs no model: reading problems, and short errors instead of tracebacks."""

import importlib.util
import json
import socket

import pytest

from minicpm_math import cli
from minicpm_math.client import Backend, BackendError


@pytest.fixture(autouse=True)
def no_proxy(monkeypatch):
    for name in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        monkeypatch.delenv(name, raising=False)


def closed_port_url() -> str:
    with socket.socket() as sock:  # a port that was free a moment ago: nothing listens on it
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    return f"http://127.0.0.1:{port}/v1"


def one_line(text: str) -> str:
    return " ".join(text.split())  # the console wraps long messages


def test_unreachable_server_gives_a_short_error(capsys):
    url = closed_port_url()
    code = cli.main(["solve", "What is 1 + 1?", "--base-url", url, "--no-ui", "--out", ""])
    message = one_line(capsys.readouterr().err)
    assert code == 2 and f"cannot reach the model server at {url}" in message and "--base-url" in message
    assert "Traceback" not in message


def test_bench_stops_before_the_first_problem_when_the_server_is_unreachable(tmp_path, capsys):
    data = tmp_path / "set.jsonl"
    data.write_text("\n".join(json.dumps({"id": str(i), "problem": f"What is {i} + {i}?", "answer": str(2 * i)})
                              for i in range(3)))
    url = closed_port_url()
    code = cli.main(["bench", str(data), "--base-url", url, "--out", str(tmp_path / "runs")])
    message = one_line(capsys.readouterr().err)
    assert code == 2 and message.count(url) == 1
    assert not (tmp_path / "runs").exists()  # no problem was started


def test_server_errors_give_a_short_error(monkeypatch, capsys):
    async def unauthorized(self):
        raise BackendError("401 from http://127.0.0.1:8000/v1/models: invalid API key", 401)

    monkeypatch.setattr(Backend, "model_name", unauthorized)
    code = cli.main(["prove", "Prove that 1 + 1 = 2.", "--no-ui", "--out", ""])
    message = one_line(capsys.readouterr().err)
    assert code == 1 and "invalid API key" in message and "Traceback" not in message


def test_long_problem_text_is_not_mistaken_for_a_path(tmp_path):
    english = "Let n be a positive integer, and prove the statement below in full detail. " * 4  # no "/"
    chinese = "设正整数满足下列条件" * 10  # 100 characters, 300 bytes in UTF-8
    assert len(english.encode()) > 255 and cli.read_problem(english) == english.strip()
    assert len(chinese) == 100 and cli.read_problem(chinese) == chinese
    path = tmp_path / "problem.md"
    path.write_text("Prove that 1 + 1 = 2.\n", encoding="utf-8")
    assert cli.read_problem(str(path)) == "Prove that 1 + 1 = 2."


def test_check_warns_without_the_math_extra(monkeypatch, capsys):
    find_spec = importlib.util.find_spec
    monkeypatch.setattr(importlib.util, "find_spec",
                        lambda name, *args: None if name == "sympy" else find_spec(name, *args))
    assert "sympy" in cli.missing_math_modules()
    code = cli.main(["check", "--base-url", closed_port_url()])
    message = one_line(capsys.readouterr().err)
    assert code == 2 and "math extra is not installed (missing sympy" in message and cli.MATH_EXTRA in message
