from app.main import compare_patterns


def test_compare_patterns_returns_three_patterns() -> None:
    assert len(compare_patterns("x")) == 3
