from pydantic import BaseModel


class WorkflowState(BaseModel):
    intent: str
    needs_review: bool = False
    completed: bool = False


def run_workflow(intent: str) -> list[str]:
    state = WorkflowState(intent=intent, needs_review="refund" in intent)
    steps = ["classify"]
    if state.needs_review:
        steps.append("human_review")
    steps.extend(["execute", "respond"])
    state.completed = True
    return steps


def main() -> None:
    print(run_workflow("refund request"))


if __name__ == "__main__":
    main()
