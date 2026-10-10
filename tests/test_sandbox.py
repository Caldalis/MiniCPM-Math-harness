import asyncio
import os
import sys

import pytest

from minicpm_math.sandbox import OUTPUT_LIMIT, run_python

BEAT = "import time\nwhile True:\n    open({path!r}, 'a').write('.')\n    time.sleep(0.05)\n"


async def test_runs_and_captures_output():
    result = await run_python("print(sum(range(10)))")
    assert result.ok and result.stdout.strip() == "45"


async def test_reports_errors():
    result = await run_python("raise ValueError('boom')")
    assert not result.ok and "ValueError" in result.summary()


async def test_timeout_kills_process():
    result = await run_python("while True:\n    pass", timeout=1.0)
    assert result.timed_out and not result.ok
    assert result.seconds < 10


async def test_timeout_keeps_what_was_printed():
    result = await run_python("print('PASS: n = 1..5 agree', flush=True)\nimport time\ntime.sleep(60)", timeout=1.5)
    assert result.timed_out and "PASS: n = 1..5 agree" in result.stdout
    assert "PASS: n = 1..5 agree" in result.summary() and result.seconds < 10


@pytest.mark.skipif(os.name != "posix", reason="the script's process group is killed on posix only")
async def test_cancelled_run_stops_the_script_and_what_it_started(tmp_path):
    script, child = tmp_path / "script", tmp_path / "child"
    code = (f"import subprocess, sys\nsubprocess.Popen([sys.executable, '-c', {BEAT.format(path=str(child))!r}])\n"
            + BEAT.format(path=str(script)))
    task = asyncio.ensure_future(run_python(code, timeout=60))
    for _ in range(200):
        if script.exists() and child.exists():
            break
        await asyncio.sleep(0.05)
    task.cancel()  # what early stopping does to a lab check that is still running
    with pytest.raises(asyncio.CancelledError):
        await task
    sizes = script.stat().st_size, child.stat().st_size
    await asyncio.sleep(0.5)
    assert sizes[0] > 0 and (script.stat().st_size, child.stat().st_size) == sizes


async def test_output_is_capped():
    result = await run_python("import sys\nsys.stdout.write('x' * 1000000)")
    assert result.ok and result.stdout.startswith("x" * OUTPUT_LIMIT)
    assert result.stdout.endswith(f"[... {1000000 - OUTPUT_LIMIT} bytes of output dropped]")


async def test_isolated_environment():
    result = await run_python("import os; print(sorted(k for k in os.environ if k.startswith('HF') or 'KEY' in k))")
    assert result.ok and result.stdout.strip() == "[]"


async def test_math_libraries_get_one_thread():
    result = await run_python("import os; print(os.environ['OPENBLAS_NUM_THREADS'], os.environ['OMP_NUM_THREADS'])")
    assert result.ok and result.stdout.split() == ["1", "1"]


@pytest.mark.skipif(not sys.platform.startswith("linux"), reason="RLIMIT_AS is enforced on Linux only")
async def test_memory_limit():
    result = await run_python("x = bytearray(8 * 1024**3)", memory_mb=1024)
    assert not result.ok and "MemoryError" in result.summary()
    small = await run_python("x = bytearray(64 * 1024**2); print(len(x))", memory_mb=1024)
    assert small.ok
