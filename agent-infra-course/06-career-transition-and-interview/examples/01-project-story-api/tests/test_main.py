from app.main import ProjectFacts, build_story


def test_build_story_contains_project_name() -> None:
    story = build_story(ProjectFacts(name="x", goal="y", improvement="z"))
    assert "x" in story["business"]
