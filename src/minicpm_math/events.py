"""Live state of a run, shared by the dashboard, the plain-text logger and API users."""

from __future__ import annotations

import time
from collections import deque
from dataclasses import dataclass
from typing import Callable, Deque, Dict, List, Optional

ROLES = ("prover", "scribe", "lab", "verifier", "refiner", "solver", "coder")
FINAL = ("done", "failed", "cancelled")


@dataclass
class AgentState:
    id: str
    role: str
    status: str = "queued"  # queued | think | write | exec | done | failed | cancelled
    tokens: int = 0
    started: Optional[float] = None
    ended: Optional[float] = None
    note: str = ""

    @property
    def elapsed(self) -> float:
        if self.started is None:
            return 0.0
        return (self.ended or time.monotonic()) - self.started

    @property
    def rate(self) -> float:
        return self.tokens / self.elapsed if self.elapsed > 0.5 else 0.0


Listener = Callable[[str, AgentState], None]  # (event, state) with event in {"start", "finish"}


class Tracker:
    def __init__(self, title: str = "", mode: str = "", backend: str = ""):
        self.title = title
        self.mode = mode
        self.backend = backend
        self.agents: Dict[str, AgentState] = {}
        self.log: Deque[str] = deque(maxlen=6)
        self.status = ""
        self.started = time.monotonic()
        self.listeners: List[Listener] = []
        self._finished_tokens = 0

    def add(self, agent_id: str, role: str) -> AgentState:
        state = AgentState(agent_id, role)
        self.agents[agent_id] = state
        return state

    def update(self, agent_id: str, *, status: Optional[str] = None, tokens: Optional[int] = None, note: Optional[str] = None) -> None:
        state = self.agents.get(agent_id)
        if state is None or state.status in FINAL:
            return
        if status is not None and status != state.status:
            if state.started is None and status != "queued":
                state.started = time.monotonic()
                self._emit("start", state)
            state.status = status
        if tokens is not None:
            state.tokens = max(state.tokens, tokens)
        if note is not None:
            state.note = note

    def finish(self, agent_id: str, status: str = "done", note: Optional[str] = None) -> None:
        state = self.agents.get(agent_id)
        if state is None:
            return
        if note is not None:
            state.note = note
        if state.status in FINAL:
            return
        state.status = status
        state.ended = time.monotonic()
        if state.started is None:
            state.started = state.ended
        self._finished_tokens += state.tokens
        self._emit("finish", state)

    def note(self, message: str) -> None:
        self.log.append(message)

    @property
    def elapsed(self) -> float:
        return time.monotonic() - self.started

    @property
    def tokens(self) -> int:
        live = sum(a.tokens for a in self.agents.values() if a.status not in FINAL)
        return self._finished_tokens + live

    @property
    def active(self) -> int:
        return sum(1 for a in self.agents.values() if a.status in ("think", "write", "exec"))

    def _emit(self, event: str, state: AgentState) -> None:
        for listener in self.listeners:
            listener(event, state)
