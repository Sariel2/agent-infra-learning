from pydantic import BaseModel


class StoryRequest(BaseModel):
    name: str
    goal: str
    improvement: str


class QARequest(BaseModel):
    topic: str


FAQ = {
    "workflow-vs-agent": "Start from task determinism. Fixed steps prefer workflow; open-ended tool choice may justify an agent.",
    "rag-failures": "Classify failures into retrieval miss, citation mismatch, and synthesis drift.",
}


def build_story(name: str, goal: str, improvement: str) -> dict[str, str]:
    return {
        "resume_bullet": f"Built {name} to {goal}, improving reliability through {improvement}.",
        "pitch": f"{name} was designed as an agent infra project focused on {goal} and {improvement}.",
    }


def answer(topic: str) -> str:
    return FAQ.get(topic, "Answer with goal, design, failures, trade-offs, and outcomes.")
