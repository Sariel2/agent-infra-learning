FAQ = {
    "workflow-vs-agent": "Start from task determinism. Fixed steps prefer workflow; open-ended tool choice may justify an agent.",
    "rag-failures": "Classify failures into retrieval miss, citation mismatch, and answer synthesis drift.",
}


def answer_question(topic: str) -> str:
    return FAQ.get(topic, "Use goal, design, failure, and trade-off to structure your answer.")


def main() -> None:
    print(answer_question("workflow-vs-agent"))


if __name__ == "__main__":
    main()
