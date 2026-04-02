from app.main import answer_question


def test_answer_question_returns_default_for_unknown_topic() -> None:
    assert "goal" in answer_question("unknown")
