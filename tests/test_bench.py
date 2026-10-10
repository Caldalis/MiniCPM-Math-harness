import json

from minicpm_math.bench import load_items, score_answer_run, summarize_answers
from minicpm_math.swarm import AnswerResult


def test_load_jsonl_and_csv(tmp_path):
    jsonl = tmp_path / "set.jsonl"
    jsonl.write_text("\n".join(json.dumps(r) for r in [{"question": "1+1?", "answer": "2"}, {"problem": "2+2?"}]))
    items = load_items(str(jsonl))
    assert [(i["id"], i["problem"], i["answer"]) for i in items] == [("1", "1+1?", "2"), ("2", "2+2?", None)]

    csv_file = tmp_path / "proofs.csv"
    csv_file.write_text('Problem ID,Problem,Solution,Short Answer\nPB-1,"Prove\nthat x",ref,\n')
    (item,) = load_items(str(csv_file))
    assert item["id"] == "PB-1" and item["problem"] == "Prove\nthat x" and item["reference"] == {"Solution": "ref"}


def _result(answers):
    samples = [{"agent": f"A{i}", "kind": kind, "answer": a, "normalized": a, "finish": "stop"}
               for i, (kind, a) in enumerate(answers)]
    return AnswerResult("p", "38", [("38", 2)], samples, 0, 0.0, 0, False)


def test_scores_separate_single_shot_from_program_aided():
    row = score_answer_run("38", _result([("think", "28"), ("think", "38"), ("code", "38")]))
    assert row["correct"] and row["pass_at_k"]
    assert row["pass_at_1_think"] == 0.5 and row["pass_at_1_code"] == 1.0

    wrong = dict(row, correct=False, pass_at_1_think=0.0, pass_at_1_think_strict=0.0, pass_at_1_code=0.0)
    summary = summarize_answers([row, wrong], k=3)
    assert summary == {"pass@1": 0.25, "pass@1 (no forced finish)": 0.25, "forced finish rate": 0.0,
                       "pass@1 (program-aided)": 0.5, "maj@3": 0.5, "pass@3": 1.0,
                       "tied_votes": 0, "tied_and_correct": 0}


def test_strict_pass_at_1_counts_forced_answers_as_missing():
    samples = [{"agent": "A1", "kind": "think", "answer": "38", "finish": "forced"},
               {"agent": "A2", "kind": "think", "answer": "38", "finish": "stop"}]
    result = AnswerResult("p", "38", [("38", 2)], samples, 0, 0.0, 0, False)
    row = score_answer_run("38", result)
    assert row["pass_at_1_think"] == 1.0 and row["pass_at_1_think_strict"] == 0.5 and row["forced_rate"] == 0.5


def test_strict_pass_at_1_counts_truncated_answers_as_missing():
    # without forced finish, a cut-off sample's answer is read from the tail of its reasoning
    samples = [{"agent": "A1", "kind": "think", "answer": "38", "finish": "length"},
               {"agent": "A2", "kind": "think", "answer": "38", "finish": "loop"},
               {"agent": "A3", "kind": "think", "answer": "38", "finish": "stop"},
               {"agent": "A4", "kind": "think", "answer": "28", "finish": "stop"}]
    row = score_answer_run("38", AnswerResult("p", "38", [("38", 3), ("28", 1)], samples, 0, 0.0, 0, False))
    assert row["pass_at_1_think"] == 0.75 and row["pass_at_1_think_strict"] == 0.25 and row["forced_rate"] == 0.0


def test_gold_answer_is_the_reference(monkeypatch):
    seen = []
    monkeypatch.setattr("minicpm_math.parsing.answers_match", lambda a, b: seen.append(a) or a == b)
    score_answer_run("50", _result([("think", "41+9=50"), ("code", "50")]))
    assert seen and all(a == "50" for a in seen)


def test_gold_first_matters_for_symbolic_matching():
    import pytest

    pytest.importorskip("math_verify")
    row = score_answer_run("50", _result([("think", "41+9=50")]))  # a real sample from AIME 2026
    assert row["pass_at_1_think"] == 1.0


def test_ties_are_reported():
    tied = AnswerResult("p", "588", [("588", 1), ("336", 1), ("1176", 1)], [], 0, 0.0, 0, False)
    assert tied.tied and not _result([]).tied
