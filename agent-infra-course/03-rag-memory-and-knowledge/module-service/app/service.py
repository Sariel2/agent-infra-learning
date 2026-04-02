from collections import deque
from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


DOCS = {
    "agent infra": "Agent infra includes tools, traces, evals, and workflow.",
    "rag": "RAG combines retrieval, citations, and answer synthesis.",
}


class Memory:
    def __init__(self, limit: int = 3) -> None:
        self.entries: deque[str] = deque(maxlen=limit)

    def add(self, item: str) -> None:
        self.entries.append(item)

    def as_list(self) -> list[str]:
        return list(self.entries)


memory = Memory()


def retrieve(question: str) -> tuple[str, str]:
    for key, value in DOCS.items():
        if key in question.lower():
            return value, f"{key}:1"
    return "No direct match found.", "none"


def ask(question: str) -> dict[str, object]:
    answer, citation = retrieve(question)
    memory.add(question)
    return {"answer": answer, "citations": [citation], "memory": memory.as_list()}
