from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "starter-workspace"
    environment: str = "dev"
    timeout_seconds: int = 30


def build_log_context(settings: Settings) -> dict[str, str | int]:
    return {
        "app": settings.app_name,
        "env": settings.environment,
        "timeout": settings.timeout_seconds,
    }


def main() -> None:
    settings = Settings()
    print(build_log_context(settings))


if __name__ == "__main__":
    main()
