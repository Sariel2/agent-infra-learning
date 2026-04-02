from pydantic import BaseModel


class ProjectFacts(BaseModel):
    name: str
    goal: str
    improvement: str


def build_story(facts: ProjectFacts) -> dict[str, str]:
    return {
        "business": f"Built {facts.name} to {facts.goal}, improving outcomes by {facts.improvement}.",
        "infra": f"Designed {facts.name} as an agent infra system focused on reliability and {facts.improvement}.",
    }


def main() -> None:
    facts = ProjectFacts(name="knowledge-agent", goal="answer support questions", improvement="faster diagnosis")
    print(build_story(facts))


if __name__ == "__main__":
    main()
