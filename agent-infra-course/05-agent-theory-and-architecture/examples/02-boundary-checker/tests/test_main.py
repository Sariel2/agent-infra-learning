from app.main import Scenario, recommend_architecture


def test_recommend_workflow_for_fixed_steps() -> None:
    scenario = Scenario(open_ended=False, steps_fixed=True, tool_variance=False)
    assert recommend_architecture(scenario) == "workflow"
