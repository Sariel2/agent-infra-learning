from pydantic import BaseModel


class CompareRequest(BaseModel):
    task: str


class RecommendRequest(BaseModel):
    open_ended: bool
    steps_fixed: bool
    tool_variance: bool


def compare(task: str) -> dict[str, list[str]]:
    return {
        "react": ["reason", "act", task],
        "router": ["classify", task],
        "plan_execute": ["plan", "execute", task],
    }


def recommend(open_ended: bool, steps_fixed: bool, tool_variance: bool) -> str:
    if steps_fixed and not open_ended:
        return "workflow"
    if open_ended or tool_variance:
        return "agent"
    return "hybrid"
