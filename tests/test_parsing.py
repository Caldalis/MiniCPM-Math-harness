from minicpm_math.client import looks_like_loop
from minicpm_math.parsing import (
    answers_match,
    boxed_all,
    count_critical,
    extract_code,
    extract_issues,
    last_boxed,
    normalize_answer,
    parse_grade,
    split_reasoning,
    trim_middle,
)


def test_split_reasoning_variants():
    assert split_reasoning("<think>\nabc\n</think>\n\nanswer") == ("abc", "answer")
    assert split_reasoning("abc\n</think>\n\nanswer") == ("abc", "answer")  # template opened <think>
    assert split_reasoning("<think>\nstill thinking") == ("still thinking", "")
    assert split_reasoning("plain answer") == ("", "plain answer")


def test_boxed_nested_and_bare():
    assert last_boxed(r"so \boxed{\frac{1}{2}} and finally \boxed{\{1, 2\}}") == r"\{1, 2\}"
    assert boxed_all(r"\boxed 5 and \fbox{7}") == ["5", "7"]
    assert last_boxed("no box here") is None


def test_normalize_answer():
    assert normalize_answer(r"\dfrac{6}{8}") == "3/4"
    assert normalize_answer("0.75") == "3/4"
    assert normalize_answer("070") == "70"
    assert normalize_answer(r"n = 38") == "38"
    assert normalize_answer(r"1{,}000") != ""  # does not crash on odd LaTeX
    assert normalize_answer("1,000") == "1000"
    assert normalize_answer(r"45^\circ") == "45"
    assert normalize_answer(r"\text{Yes}") == "yes"
    assert normalize_answer(r"\frac12") == "1/2"
    assert answers_match("38", r"\boxed{38}".replace(r"\boxed{", "").rstrip("}"))
    assert not answers_match("28", "38")
    assert not answers_match(None, "1")


def test_parse_grade():
    assert parse_grade(r"Issues ... Final grade: \boxed{6}") == 6
    assert parse_grade(r"\boxed{7/7}") == 7
    assert parse_grade(r"\boxed{12} then \boxed{3}") == 3
    assert parse_grade("I would give this a score of 5/7.") == 5
    assert parse_grade("Grade: 2") == 2
    assert parse_grade("no grade at all") is None


def test_issues():
    report = "\n".join([
        "1. [CRITICAL] The case n = 1 is not handled.",
        "- [GAP]: the bound in step 3 needs justification",
        "[GAP] None",
        "No [CRITICAL] issues besides the above.",
        r"\boxed{2}",
    ])
    issues = extract_issues(report)
    assert issues == ["[CRITICAL] The case n = 1 is not handled.", "[GAP] the bound in step 3 needs justification"]
    assert count_critical(report) == 1


def test_extract_code_prefers_python():
    text = "```text\nnot code\n```\n```python\nprint(1)\n```\n```\nprint(2)\n```"
    assert extract_code(text) == "print(1)"
    assert extract_code("```\nprint(3)\n```") == "print(3)"
    assert extract_code("nothing") is None


def test_trim_middle():
    text = "a" * 100 + "b" * 100
    out = trim_middle(text, 80)
    assert len(out) == 80 and out.startswith("a") and out.endswith("b")
    assert trim_middle("short", 80) == "short"


def test_loop_detector():
    assert looks_like_loop("intro " + "Let me recheck the sum. " * 120)
    assert not looks_like_loop("".join(f"step {i}: compute {i * i}. " for i in range(200)))
    assert not looks_like_loop("short " * 10)


def test_symbolic_equivalence_when_available():
    import pytest

    pytest.importorskip("math_verify")
    assert answers_match(r"\frac{7}{3}\sqrt{3}", r"\frac{7\sqrt{3}}{3}")
    assert answers_match(r"\frac{\sqrt{1740}}{3}", r"\frac{2\sqrt{435}}{3}")
    assert answers_match(r"2 - \frac{\pi}{2}", r"\frac{4-\pi}{2}")
    assert not answers_match(r"3^{2025}", r"3^{2024}")


def test_symbolic_edge_cases():
    import pytest

    pytest.importorskip("math_verify")
    gold = r"50(1 - \frac{1}{2^{101} - 1})"
    assert not answers_match(gold, r"50\left(\frac{1-2^{-99}}{1-2^{-101}}\right)")  # differs by ~4e-29
    assert answers_match(gold, r"\dfrac{100\bigl(2^{100}-1\bigr)}{2^{101}-1}")  # sizing commands
    assert answers_match(r"\sqrt{17} - 1", r"\sqrt{18-2\sqrt{17}}")
    assert answers_match(r"(3+\sqrt{6})^{-1/3}", r"\sqrt[3]{\frac{3-\sqrt6}{3}}")
    assert answers_match(r"\frac{7}{3}\sqrt{3}", r"\displaystyle \frac{7\sqrt3}{3}")
