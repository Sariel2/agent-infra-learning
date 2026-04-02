from app.main import run_agent


def test_run_agent_order_path() -> None:
    trace = run_agent("check order 42")
    assert trace[0].tool == "get_order_status"
