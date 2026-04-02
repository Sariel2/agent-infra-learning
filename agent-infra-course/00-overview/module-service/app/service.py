from pydantic import BaseModel


class WorkspaceStatus(BaseModel):
    environment_ready: bool = True
    logs_ready: bool = True
    project_defined: bool = True


def summarize_workspace() -> dict[str, object]:
    status = WorkspaceStatus()
    return {
        "status": "ready" if all(status.model_dump().values()) else "needs-work",
        "checks": status.model_dump(),
    }
