from app.main import run_workflow


def test_workflow_adds_review_for_refund() -> None:
    assert run_workflow("refund request") == ["classify", "human_review", "execute", "respond"]
