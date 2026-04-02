from app.main import generate_structured_answer


def test_generate_structured_answer() -> None:
    result = generate_structured_answer("hello")
    assert result.answer.startswith("Stub answer")
    assert 0 <= result.confidence <= 1
