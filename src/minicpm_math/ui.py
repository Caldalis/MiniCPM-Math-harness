"""Terminal dashboard for a running swarm, plus a plain-text fallback for logs and pipes."""

from __future__ import annotations

import contextlib
import os
import sys
from typing import Iterator, List, Optional

from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .events import FINAL, AgentState, Tracker

ROLE_STYLE = {
    "prover": "bold blue", "solver": "bold blue", "coder": "bold cyan", "scribe": "magenta",
    "lab": "yellow", "verifier": "green", "refiner": "bold magenta",
}
STATUS_STYLE = {
    "queued": ("· queued", "dim"), "think": ("● thinking", "magenta"), "write": ("● writing", "cyan"),
    "exec": ("⚙ running", "yellow"), "done": ("✓ done", "green"), "failed": ("✗ failed", "red"),
    "cancelled": ("– cancelled", "dim"),
}


def fmt_tokens(n: int) -> str:
    return f"{n / 1000:.1f}K" if n >= 1000 else str(n)


def fmt_time(seconds: float) -> str:
    minutes, secs = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}:{minutes:02d}:{secs:02d}" if hours else f"{minutes:02d}:{secs:02d}"


class Dashboard:
    """Renderable for ``rich.live.Live``: header, agent table (active first), status and log."""

    def __init__(self, tracker: Tracker, max_rows: int = 16):
        self.tracker = tracker
        self.max_rows = max_rows

    def _rows(self) -> List[AgentState]:
        agents = list(self.tracker.agents.values())
        active = [a for a in agents if a.status not in FINAL]
        done = sorted((a for a in agents if a.status in FINAL), key=lambda a: a.ended or 0)
        room = max(0, self.max_rows - len(active))
        shown = (done[-room:] if room else []) + active
        return sorted(shown[-self.max_rows:], key=lambda a: (a.started is None, a.started or 0))

    def __rich__(self) -> Panel:
        t = self.tracker
        rate = t.tokens / t.elapsed if t.elapsed > 1 else 0.0
        stats = Text(
            f"elapsed {fmt_time(t.elapsed)}  ·  {fmt_tokens(t.tokens)} tokens  ·  {rate:.0f} tok/s  ·  "
            f"{t.active} active / {len(t.agents)} agents",
            style="dim",
        )
        table = Table(box=None, expand=True, pad_edge=False, header_style="bold dim")
        table.add_column("agent", no_wrap=True, min_width=8)
        table.add_column("role", no_wrap=True)
        table.add_column("status", no_wrap=True)
        table.add_column("tokens", justify="right", no_wrap=True)
        table.add_column("tok/s", justify="right", no_wrap=True)
        table.add_column("note", overflow="ellipsis", no_wrap=True, ratio=1)
        for a in self._rows():
            label, style = STATUS_STYLE.get(a.status, (a.status, ""))
            table.add_row(
                Text(a.id, style="bold"), Text(a.role, style=ROLE_STYLE.get(a.role, "")), Text(label, style=style),
                fmt_tokens(a.tokens), f"{a.rate:.0f}" if a.rate else "", Text(a.note, style="dim"),
            )
        hidden = len(t.agents) - len(self._rows())
        parts = [Text(t.title, style="italic", overflow="ellipsis", no_wrap=True), stats, Text(""), table]
        if hidden > 0:
            parts.append(Text(f"… {hidden} earlier agents finished", style="dim"))
        if t.status:
            parts += [Text(""), Text(t.status, style="bold")]
        if t.log:
            parts.append(Text("\n".join(t.log), style="dim"))
        title = Text.assemble(("MiniCPM-Math ", "bold"), (t.mode, "bold cyan"), ("  ·  ", "dim"), (t.backend, "dim"))
        return Panel(Group(*parts), title=title, title_align="left", border_style="blue")


class PlainLog:
    """One line per finished agent; used when stdout is not a terminal or ``--no-ui`` is given."""

    def __init__(self, tracker: Tracker, stream=None):
        self.tracker = tracker
        self.stream = stream or sys.stderr

    def __call__(self, event: str, state: AgentState) -> None:
        if event != "finish":
            return
        line = (f"[{fmt_time(self.tracker.elapsed)}] {state.status:<9} {state.id:<10} {state.role:<9} "
                f"{fmt_tokens(state.tokens):>7} tok  {state.note}")
        print(line.rstrip(), file=self.stream, flush=True)


def save_snapshot(tracker: Tracker, path: str, width: int = 118) -> None:
    """Write the dashboard's current state as an SVG (for READMEs and posts)."""
    with open(os.devnull, "w") as sink:
        console = Console(record=True, width=width, file=sink, force_terminal=True)
        console.print(Dashboard(tracker, max_rows=24))
        console.save_svg(path, title="minicpm-math")


@contextlib.contextmanager
def live_view(tracker: Tracker, enabled: bool = True, console: Optional[Console] = None,
              snapshot: Optional[str] = None) -> Iterator[None]:
    console = console or Console(stderr=True)
    try:
        if enabled and console.is_terminal:
            with Live(Dashboard(tracker), console=console, refresh_per_second=4, transient=False):
                yield
        else:
            logger = PlainLog(tracker)
            tracker.listeners.append(logger)
            try:
                yield
            finally:
                tracker.listeners.remove(logger)
    finally:
        if snapshot:
            save_snapshot(tracker, snapshot)
