from pydantic import BaseModel


class ProjectStatus(BaseModel):
    environment_ready: bool
    logs_ready: bool
    project_defined: bool


def summarize_status(status: ProjectStatus) -> str:
    if all(status.model_dump().values()):
        return "ready"
    return "needs-work"


def main() -> None:
    status = ProjectStatus(environment_ready=True, logs_ready=True, project_defined=False)
    print(summarize_status(status))


if __name__ == "__main__":
    main()
