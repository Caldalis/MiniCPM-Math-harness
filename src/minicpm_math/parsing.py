"""Text utilities: reasoning split, \\boxed{} extraction, answer matching, grades, code blocks."""

from __future__ import annotations

import functools
import re
import threading
from fractions import Fraction
from typing import Any, List, Optional, Tuple

from .template import THINK_CLOSE, THINK_OPEN

try:  # optional symbolic equivalence: pip install math-verify
    from math_verify import parse as _mv_parse, verify as _mv_verify
except ImportError:  # pragma: no cover - exercised only without the extra
    _mv_parse = _mv_verify = None


def split_reasoning(text: str) -> Tuple[str, str]:
    """Split raw model text into ``(reasoning, answer)``."""
    if THINK_CLOSE in text:
        head, _, _ = text.partition(THINK_CLOSE)
        tail = text.rsplit(THINK_CLOSE, 1)[1]
        return head.split(THINK_OPEN)[-1].strip("\n"), tail.lstrip("\n")
    if text.lstrip().startswith(THINK_OPEN):
        return text.lstrip()[len(THINK_OPEN):].lstrip("\n"), ""
    return "", text


def boxed_all(text: str) -> List[str]:
    """Contents of every ``\\boxed{...}`` / ``\\fbox{...}`` in ``text``, in order."""
    found = []
    for m in re.finditer(r"\\(?:boxed|fbox)\s*", text):
        i = m.end()
        if i < len(text) and text[i] == "{":
            depth = 0
            for j in range(i, len(text)):
                if text[j] == "{":
                    depth += 1
                elif text[j] == "}":
                    depth -= 1
                    if depth == 0:
                        found.append(text[i + 1 : j].strip())
                        break
        else:
            bare = re.match(r"([^\s$]+)", text[i:])
            if bare:
                found.append(bare.group(1))
    return found


def last_boxed(text: str) -> Optional[str]:
    found = boxed_all(text)
    return found[-1] if found else None


_FRAC = re.compile(r"^(-?)\\frac\{(-?\d+)\}\{(-?\d+)\}$")
_SLASH = re.compile(r"^(-?\d+)/(-?\d+)$")
_DECIMAL = re.compile(r"^-?(\d+\.?\d*|\.\d+)$")


def _to_number(s: str) -> Optional[Fraction]:
    try:
        if _DECIMAL.match(s):
            return Fraction(s)
        m = _SLASH.match(s)
        if m and int(m.group(2)) != 0:
            return Fraction(int(m.group(1)), int(m.group(2)))
        m = _FRAC.match(s)
        if m and int(m.group(3)) != 0:
            value = Fraction(int(m.group(2)), int(m.group(3)))
            return -value if m.group(1) else value
    except (ValueError, ZeroDivisionError):
        pass
    return None


def normalize_answer(answer: str) -> str:
    """Canonical form used for voting: ``"\\dfrac{6}{8}"``, ``"0.75"`` and ``"3/4"`` all become ``"3/4"``."""
    s = answer.strip().strip("$").strip()
    s = re.sub(r"\\(?:text|textbf|mathrm|mbox|operatorname)\s*\{([^{}]*)\}", r"\1", s)
    s = s.replace("\\left", "").replace("\\right", "")
    s = re.sub(r"\\[dt]frac", r"\\frac", s)
    for token in ("\\!", "\\,", "\\;", "\\:", "\\qquad", "\\quad", "~"):
        s = s.replace(token, "")
    for token in ("^{\\circ}", "^\\circ", "°", "\\%", "%"):
        s = s.replace(token, "")
    s = re.sub(r"\s+", " ", s).strip().rstrip(".").strip()
    s = re.sub(r"^[A-Za-z]\w{0,2}\s*=\s*", "", s)  # "n = 5" -> "5"
    if re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", s):
        s = s.replace(",", "")
    s = re.sub(r"\\frac(\d)(\d)", r"\\frac{\1}{\2}", s)
    number = _to_number(s.replace(" ", ""))
    if number is not None:
        return str(number.numerator) if number.denominator == 1 else f"{number.numerator}/{number.denominator}"
    s = s.replace(" ", "")
    return s.lower() if s.isalpha() else s


def _timeout() -> Optional[int]:
    # math-verify enforces timeouts with signals, which only work in the main thread.
    return 5 if threading.current_thread() is threading.main_thread() else None


_SIZING = re.compile(r"\\(?:[bB]igg?[lrm]?|displaystyle|textstyle|left|right)(?![A-Za-z])|\\[,;:!]")


@functools.lru_cache(maxsize=4096)
def _symbolic(answer: str) -> Any:
    if _mv_parse is None:
        return None
    try:
        # sizing and spacing commands (\bigl( ... \bigr), \displaystyle, \,) only confuse the parser
        return _mv_parse(f"${_SIZING.sub('', answer)}$", parsing_timeout=_timeout()) or None
    except Exception:
        return None


def _exactly_different(gold: Any, pred: Any) -> bool:
    """True if exact simplification proves the first parsed expressions differ.

    math-verify falls back to floating-point comparison, which calls numbers equal when they differ by less
    than ~1e-15 relatively (e.g. 50(2^101-2)/(2^101-1) and 50(2^101-4)/(2^101-1)).
    """
    try:
        import sympy

        g, p = gold[0], pred[0]
        if not (isinstance(g, sympy.Basic) and isinstance(p, sympy.Basic)):
            return False
        return sympy.simplify(g - p).is_zero is False
    except Exception:
        return False


def answers_match(a: Optional[str], b: Optional[str]) -> bool:
    """Same answer? Normalized strings first, then symbolic equivalence when math-verify is installed.

    ``a`` is treated as the reference: ``\\frac{7}{3}\\sqrt{3}`` matches ``\\frac{7\\sqrt{3}}{3}``.
    """
    if a is None or b is None:
        return False
    if normalize_answer(a) == normalize_answer(b):
        return True
    gold, pred = _symbolic(a), _symbolic(b)
    if not gold or not pred:
        return False
    try:
        same = bool(_mv_verify(gold, pred, timeout_seconds=_timeout()))
    except Exception:
        return False
    return same and not _exactly_different(gold, pred)


def parse_grade(report: str, low: int = 0, high: int = 7) -> Optional[int]:
    """Read a 0-7 grade from a verifier report; ``\\boxed{}`` first, then common phrasings."""
    for box in reversed(boxed_all(report)):
        m = re.search(r"-?\d+(?:\.\d+)?", box)
        if m and low <= float(m.group(0)) <= high:
            return int(round(float(m.group(0))))
    tail = report[-2000:]
    hits = list(re.finditer(r"(?:grade|score)\s*(?:is|=|:)?\s*\**\s*(\d)(?:\s*/\s*7)?\b", tail, re.I))
    if not hits:
        hits = list(re.finditer(r"\b(\d)\s*/\s*7\b", tail))
    for hit in reversed(hits):
        if low <= int(hit.group(1)) <= high:
            return int(hit.group(1))
    return None


_ISSUE = re.compile(r"^\s*(?:[-*•]|\d+[.)])?\s*\**\[(CRITICAL|GAP)\]\**\s*[:.\-–]?\s*(.*)$", re.I)
_NO_ISSUE = {"", "none", "n/a", "no issues", "no issues found", "none found"}


def extract_issues(report: str, limit: int = 12) -> List[str]:
    """One line per ``[CRITICAL]`` / ``[GAP]`` finding in a verifier report (``"[GAP] None"`` is skipped)."""
    issues = []
    for line in report.splitlines():
        m = _ISSUE.match(line)
        if m and m.group(2).strip().lower().rstrip(".") not in _NO_ISSUE:
            issues.append(f"[{m.group(1).upper()}] {m.group(2).strip()}")
    return issues[:limit]


def count_critical(report: str) -> int:
    return sum(1 for issue in extract_issues(report, limit=1000) if "critical" in issue.lower())


_CODE = re.compile(r"```([A-Za-z0-9_+-]*)[^\n]*\n(.*?)```", re.S)


def extract_code(text: str) -> Optional[str]:
    """The last ```python block in ``text`` (or the last fenced block if none is labeled)."""
    blocks = _CODE.findall(text)
    python = [body for lang, body in blocks if lang.lower() in ("python", "py", "python3")]
    chosen = python or [body for _, body in blocks]
    return chosen[-1].strip() if chosen else None


def last_line(text: str) -> Optional[str]:
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    return lines[-1] if lines else None


def trim_middle(text: str, max_chars: int, marker: str = "\n\n[... middle omitted ...]\n\n") -> str:
    """Keep the head and (mostly) the tail of ``text`` within ``max_chars``."""
    if len(text) <= max_chars:
        return text
    head = max_chars // 4
    tail = max_chars - head - len(marker)
    return text[:head] + marker + text[-tail:]


def first_line(text: str, width: int = 80) -> str:
    line = next((l.strip() for l in text.strip().splitlines() if l.strip()), "")
    return line if len(line) <= width else line[: width - 1] + "…"
