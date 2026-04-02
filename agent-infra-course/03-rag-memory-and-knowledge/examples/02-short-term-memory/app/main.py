from collections import deque
from pydantic import BaseModel


class MemoryEntry(BaseModel):
    speaker: str
    text: str


class ConversationMemory:
    def __init__(self, limit: int = 3) -> None:
        self.limit = limit
        self.entries: deque[MemoryEntry] = deque(maxlen=limit)

    def add(self, speaker: str, text: str) -> None:
        self.entries.append(MemoryEntry(speaker=speaker, text=text))

    def summary(self) -> list[str]:
        return [f"{entry.speaker}:{entry.text}" for entry in self.entries]


def main() -> None:
    memory = ConversationMemory(limit=2)
    memory.add("user", "hello")
    memory.add("assistant", "hi")
    memory.add("user", "need rag help")
    print(memory.summary())


if __name__ == "__main__":
    main()
