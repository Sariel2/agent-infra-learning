from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    name: str
    query: str = Field(min_length=1)


class ToolResult(BaseModel):
    ok: bool
    content: str
    error: str | None = None


def search_docs(call: ToolCall) -> ToolResult:
    return ToolResult(ok=True, content=f"found:{call.query}")


def main() -> None:
    print(search_docs(ToolCall(name="search_docs", query="agent")).model_dump())


if __name__ == "__main__":
    main()
