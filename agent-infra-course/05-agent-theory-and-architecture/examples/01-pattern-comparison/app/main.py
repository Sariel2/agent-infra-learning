from pydantic import BaseModel


class PatternOutput(BaseModel):
    pattern: str
    steps: list[str]


def compare_patterns(task: str) -> list[PatternOutput]:
    return [
        PatternOutput(pattern="react", steps=["reason", "act", task]),
        PatternOutput(pattern="router", steps=["classify", f"route:{task}" ]),
        PatternOutput(pattern="plan_execute", steps=["plan", "execute_step_1", task]),
    ]


def main() -> None:
    print([item.model_dump() for item in compare_patterns("answer with tools")])


if __name__ == "__main__":
    main()
