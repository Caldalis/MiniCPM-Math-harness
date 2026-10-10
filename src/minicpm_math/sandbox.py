"""Run model-written Python checks in a subprocess.

This is a convenience sandbox, not a security boundary: the code runs as the current
user with a CPU-time limit, a memory limit (Linux only; macOS does not enforce
``RLIMIT_AS``), a timeout, an empty temporary working directory and no inherited
environment. The script and the processes it starts are killed on timeout and when the
run is cancelled, and at most ``OUTPUT_LIMIT`` bytes of each output stream are kept.
Disable code execution (``--no-exec``) or run the harness in a container when the model
or its inputs are untrusted.
"""

from __future__ import annotations

import asyncio
import importlib.util
import os
import signal
import sys
import tempfile
import time
from dataclasses import dataclass
from typing import List, Optional

MEMORY_LIMIT_MB = 4096  # address space per script; brute-force checks need far less
OUTPUT_LIMIT = 256 * 1024  # bytes kept per stream; the rest is read and dropped, so a print loop cannot fill memory
KILL_GRACE = 5.0  # seconds to wait for the pipes of a killed script to close


@dataclass
class ExecResult:
    stdout: str
    stderr: str
    returncode: Optional[int]
    timed_out: bool
    seconds: float

    @property
    def ok(self) -> bool:
        return self.returncode == 0 and not self.timed_out

    def summary(self, max_chars: int = 4000) -> str:
        """Text handed back to the model: stdout, then the tail of stderr on failure."""
        parts = [self.stdout.strip()]
        if self.timed_out:
            parts.append(f"[timed out after {self.seconds:.0f}s]")
        elif self.returncode not in (0, None):
            parts.append(f"[exit code {self.returncode}]\n{self.stderr.strip()[-1500:]}")
        text = "\n".join(p for p in parts if p).strip() or "[no output]"
        return text if len(text) <= max_chars else text[: max_chars - 40] + "\n[... output truncated ...]"


def available_modules(candidates=("sympy", "numpy", "networkx", "mpmath")) -> List[str]:
    return [name for name in candidates if importlib.util.find_spec(name) is not None]


def _limit_resources(cpu_seconds: int, memory_mb: Optional[int]) -> None:  # pragma: no cover - runs in the child
    try:
        import resource

        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds + 1))
        if memory_mb and sys.platform.startswith("linux"):
            resource.setrlimit(resource.RLIMIT_AS, (memory_mb << 20, memory_mb << 20))
    except (ImportError, ValueError, OSError):
        pass


def _kill(proc: asyncio.subprocess.Process) -> None:
    try:
        if os.name == "posix":
            os.killpg(proc.pid, signal.SIGKILL)  # also reaps anything the script spawned
        else:
            proc.kill()
    except (ProcessLookupError, PermissionError):
        pass


class _Capture:
    """Reads one pipe to the end, keeping its first ``limit`` bytes and counting the rest."""

    def __init__(self, limit: int = OUTPUT_LIMIT):
        self.limit = limit
        self.data = bytearray()
        self.dropped = 0

    async def drain(self, stream: Optional[asyncio.StreamReader]) -> None:
        if stream is None:
            return
        while True:
            chunk = await stream.read(1 << 16)
            if not chunk:
                return
            keep = max(0, min(len(chunk), self.limit - len(self.data)))
            self.data += chunk[:keep]
            self.dropped += len(chunk) - keep

    def text(self) -> str:
        text = self.data.decode("utf-8", errors="replace")
        if self.dropped:
            text += f"\n[... {self.dropped} bytes of output dropped]"
        return text


async def _settle(tasks: List[asyncio.Future], grace: float = KILL_GRACE) -> None:
    """Give a killed script's pipes a moment to close; stop reading if a process outside its group keeps them open."""
    try:
        await asyncio.wait(tasks, timeout=grace)
    finally:
        for task in tasks:
            task.cancel()


async def run_python(code: str, *, timeout: float = 20.0, python: Optional[str] = None,
                     memory_mb: Optional[int] = MEMORY_LIMIT_MB) -> ExecResult:
    start = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="minicpm-math-") as workdir:
        path = os.path.join(workdir, "check.py")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(code)
        kwargs = {}
        if os.name == "posix":
            cpu = max(1, int(timeout) + 1)
            kwargs["preexec_fn"] = lambda: _limit_resources(cpu, memory_mb)
            kwargs["start_new_session"] = True
        env = {"PATH": os.environ.get("PATH", ""), "PYTHONIOENCODING": "utf-8", "PYTHONHASHSEED": "0"}
        # one thread per math library: keeps a script on one core and keeps OpenBLAS within the memory limit
        env.update({name: "1" for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")})
        proc = await asyncio.create_subprocess_exec(
            python or sys.executable, "-I", path,
            cwd=workdir, env=env,
            stdin=asyncio.subprocess.DEVNULL, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
            **kwargs,
        )
        # Both pipes are drained while the script runs: it never blocks on a full pipe, the harness' memory stays
        # bounded, and whatever the script printed before a timeout is kept.
        out, err = _Capture(), _Capture()
        tasks = [asyncio.ensure_future(proc.wait()), asyncio.ensure_future(out.drain(proc.stdout)),
                 asyncio.ensure_future(err.drain(proc.stderr))]
        try:
            _, pending = await asyncio.wait(tasks, timeout=timeout)
        except asyncio.CancelledError:  # early stop or Ctrl+C: the script must not outlive the run
            _kill(proc)
            await _settle(tasks)
            raise
        timed_out = bool(pending)
        if timed_out:
            _kill(proc)
            await _settle(tasks)
    return ExecResult(
        stdout=out.text(),
        stderr=err.text(),
        returncode=None if timed_out else proc.returncode,
        timed_out=timed_out,
        seconds=time.monotonic() - start,
    )
