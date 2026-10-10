"""Run directories: every request and response is kept, so any claimed result can be audited."""

from __future__ import annotations

import json
import re
import time
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Optional


def slugify(text: str, width: int = 40) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", text.strip().lower()).strip("-")
    return slug[:width].rstrip("-") or "problem"


def new_run_dir(root: str, problem: str, mode: str) -> Path:
    stamp = time.strftime("%Y%m%d-%H%M%S")
    path = Path(root) / f"{stamp}-{mode}-{slugify(problem)}"
    suffix = 1
    while path.exists():
        suffix += 1
        path = Path(root) / f"{stamp}-{mode}-{slugify(problem)}-{suffix}"
    return path


class Recorder:
    """Appends JSON lines to ``calls.jsonl`` and ``events.jsonl``; a no-op without a directory."""

    def __init__(self, run_dir: Optional[Path] = None):
        self.dir = Path(run_dir) if run_dir else None
        if self.dir:
            self.dir.mkdir(parents=True, exist_ok=True)

    def _append(self, name: str, record: dict) -> None:
        if not self.dir:
            return
        with open(self.dir / name, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False, default=_default) + "\n")

    def call(self, agent: str, role: str, request: dict, generation: Any = None, error: Optional[str] = None) -> None:
        self._append("calls.jsonl", {
            "time": time.time(), "agent": agent, "role": role, "request": request,
            "response": generation, "error": error,
        })

    def event(self, kind: str, **data: Any) -> None:
        self._append("events.jsonl", {"time": time.time(), "kind": kind, **data})

    def write_text(self, name: str, text: str) -> Optional[Path]:
        if not self.dir:
            return None
        path = self.dir / name
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, name: str, obj: Any) -> Optional[Path]:
        return self.write_text(name, json.dumps(obj, ensure_ascii=False, indent=2, default=_default))


def _default(obj: Any) -> Any:
    if is_dataclass(obj):
        return asdict(obj)
    if isinstance(obj, Path):
        return str(obj)
    raise TypeError(f"not JSON serializable: {type(obj).__name__}")
