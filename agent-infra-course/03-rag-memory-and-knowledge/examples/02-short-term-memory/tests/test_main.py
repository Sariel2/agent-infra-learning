from app.main import ConversationMemory


def test_memory_keeps_recent_entries() -> None:
    memory = ConversationMemory(limit=2)
    memory.add("user", "1")
    memory.add("assistant", "2")
    memory.add("user", "3")
    assert memory.summary() == ["assistant:2", "user:3"]
