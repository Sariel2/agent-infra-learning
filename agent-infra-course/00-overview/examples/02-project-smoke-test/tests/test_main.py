from app.main import ProjectStatus, summarize_status


def test_summarize_status_ready() -> None:
    status = ProjectStatus(environment_ready=True, logs_ready=True, project_defined=True)
    assert summarize_status(status) == "ready"
