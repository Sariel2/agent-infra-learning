from pydantic import BaseModel


class StructuredAnswer(BaseModel):
    answer: str
    confidence: float
    reasoning_summary: str


def generate_structured_answer(question: str) -> StructuredAnswer:
    return StructuredAnswer(
        answer=f"Stub answer for: {question}",
        confidence=0.72,
        reasoning_summary="Used a deterministic fake generator for course practice.",
    )


def main() -> None:
    print(generate_structured_answer("What is agent infra?").model_dump())


if __name__ == "__main__":
    main()
