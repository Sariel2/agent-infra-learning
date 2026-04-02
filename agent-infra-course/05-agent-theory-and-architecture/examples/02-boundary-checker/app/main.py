from pydantic import BaseModel


class Scenario(BaseModel):
    open_ended: bool
    steps_fixed: bool
    tool_variance: bool


def recommend_architecture(scenario: Scenario) -> str:
    if scenario.steps_fixed and not scenario.open_ended:
        return "workflow"
    if scenario.open_ended or scenario.tool_variance:
        return "agent"
    return "hybrid"


def main() -> None:
    print(recommend_architecture(Scenario(open_ended=False, steps_fixed=True, tool_variance=False)))


if __name__ == "__main__":
    main()
