"""Prompts for every role in the swarm.

They are written for a 2B model: short, explicit, one task per prompt, and with final
outputs in ``\\boxed{}`` wherever a machine has to read them, because that is the format
MiniCPM5-2B-Math was trained to produce reliably.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

Messages = List[Dict[str, str]]

# One approach suggestion per prover, cycled. Diversity matters more for a swarm of
# identical small models than raw sample count: without it, many provers make the same
# mistake for the same reason.
STRATEGIES = [
    "",
    "One possible angle (use it only if it helps): work out small cases first, guess the pattern, then prove it in general.",
    "One possible angle (use it only if it helps): look for an invariant, a monovariant, or a clever coloring or weighting.",
    "One possible angle (use it only if it helps): consider an extremal object (smallest, largest, first counterexample) or argue by contradiction.",
    "One possible angle (use it only if it helps): try induction, possibly on a stronger statement than the one asked.",
    "One possible angle (use it only if it helps): use algebraic manipulation, such as substitutions, factorizations and classical inequalities (AM-GM, Cauchy-Schwarz, Jensen).",
    "One possible angle (use it only if it helps): count something in two ways, or find a bijection.",
    "One possible angle (use it only if it helps): if an extremal value or an existence claim is involved, find the construction first, then prove that nothing better is possible.",
]


def _user(text: str) -> Messages:
    return [{"role": "user", "content": text.strip()}]


def _modules_note(modules: Sequence[str]) -> str:
    return "the Python standard library" + (", " + ", ".join(modules) if modules else "")


def solver(problem: str) -> Messages:
    return _user(f"{problem}\n\nPlease reason step by step, and put your final answer within \\boxed{{}}.")


def coder(problem: str, modules: Sequence[str], timeout: float) -> Messages:
    return _user(
        f"""{problem}

Solve this problem with the help of a computer. Think about the mathematics first, then write ONE self-contained Python 3 program that computes the final answer exactly (prefer integers and fractions over floats; brute force is fine when it is fast enough). The program must finish in under {timeout:.0f} seconds and print only the final answer on its last line. Available: {_modules_note(modules)}.

Put the program in a single ```python code block."""
    )


def prover(problem: str, hint: str = "") -> Messages:
    hint_line = f"\n{hint}\n" if hint else ""
    return _user(
        f"""{problem}

Write a complete and rigorous proof.
- Justify every step. Do not skip "routine" verifications, and do not cite results beyond standard textbook theorems without proving them.
- If the problem asks you to find or determine something, prove both that your answer works and that nothing else does.
- Before writing up, check your argument for gaps and missing cases.
{hint_line}
After thinking, present the final solution in full: a self-contained proof that a grader can check line by line, not a summary of your reasoning."""
    )


def scribe(problem: str, notes: str, draft: str) -> Messages:
    draft_part = draft.strip() or "(none)"
    return _user(
        f"""Below is a math problem and the scratch work of a strong student who attempted it. The scratch work is long and messy, may be cut off, and may contain false starts, but it may also contain a correct argument.

## Problem
{problem}

## Scratch work
{notes}

## The student's own write-up (may be incomplete)
{draft_part}

## Your task
Write the final solution supported by the scratch work, as a complete and rigorous proof.
- Keep every essential step: key lemmas, case analyses, bounds, constructions, and the verification of the final answer.
- Fix small slips and supply missing steps. If the scratch work is wrong or incomplete, complete the argument yourself.
- Output only the final solution."""
    )


def lab(problem: str, proof: str, modules: Sequence[str], timeout: float) -> Messages:
    return _user(
        f"""## Problem
{problem}

## Proposed solution
{proof}

## Your task
Write ONE self-contained Python 3 program that tests this solution by brute force on small cases. Recompute everything independently from the definitions in the problem; do not merely re-evaluate the solution's own formulas. Test whatever can be tested: the final answer or formula, key identities and inequalities, counts, and any construction.

Keep it short: a few targeted checks are enough. For every check, print one line that starts with "PASS:" or "FAIL:" followed by a short description and the values involved. The program must finish in under {timeout:.0f} seconds. Available: {_modules_note(modules)}. Put the program in a single ```python code block."""
    )


def _lab_section(lab_output: Optional[str]) -> str:
    if not lab_output:
        return ""
    return f"""
## Computational evidence
A brute-force script was written to test this solution on small cases. Its output is below (the script itself may contain bugs):
```
{lab_output}
```
"""


def verifier(problem: str, proof: str, lab_output: Optional[str] = None) -> Messages:
    return _user(
        f"""You are a strict grader for a mathematical olympiad. Your job is to find mistakes, not to praise. Assume the solution may be wrong until you have checked every step.

## Problem
{problem}

## Solution to grade
{proof}
{_lab_section(lab_output)}
## Instructions
1. Check the solution line by line. Re-derive every computation and test every claim on a small case.
2. List each issue on its own line, starting with
   [CRITICAL] for an error that breaks the proof (a false claim, an invalid step, a missing non-trivial case, circular reasoning, or a wrong final answer), or
   [GAP] for a step that may be true but is not adequately justified.
   If there are no issues, write "No issues found."
3. Grade on the olympiad scale: 7 = complete and rigorous; 5-6 = correct with minor gaps; 1-4 = substantial progress but a serious gap or error; 0 = wrong or no real progress.
4. End with the grade in the form \\boxed{{grade}}, for example \\boxed{{3}}."""
    )


def refiner(problem: str, proof: str, reports: Sequence[str], lab_output: Optional[str], notes: str = "") -> Messages:
    report_text = "\n\n".join(f"### Reviewer {i + 1}\n{r.strip()}" for i, r in enumerate(reports)) or "(none)"
    notes_part = f"\n## Your earlier scratch work (for reference)\n{notes}\n" if notes else ""
    return _user(
        f"""## Problem
{problem}

## Previous solution
{proof}

## Reviewer reports
{report_text}
{_lab_section(lab_output)}{notes_part}
## Your task
Write an improved solution that is complete and rigorous. Fix every valid issue raised by the reviewers; if a reviewer is wrong about something, keep that part and justify it more carefully. If the approach cannot be repaired, start over with a different approach. Output the full corrected solution, not a list of changes."""
    )
