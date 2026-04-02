import pytest
from pydantic import ValidationError
from app.main import ToolCall, search_docs


def test_tool_call_validation() -> None:
    with pytest.raises(ValidationError):
        ToolCall(name="search_docs", query="")


def test_search_docs() -> None:
    result = search_docs(ToolCall(name="search_docs", query="agent"))
    assert result.ok is True
    assert result.content == "found:agent"
