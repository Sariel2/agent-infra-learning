from app.main import Settings, build_log_context


def test_build_log_context() -> None:
    settings = Settings(app_name="course", environment="test", timeout_seconds=15)
    assert build_log_context(settings) == {"app": "course", "env": "test", "timeout": 15}
