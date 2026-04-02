from app.main import run_eval


def test_run_eval_all_match() -> None:
    assert all(result.matched for result in run_eval())
