from pydantic import BaseModel


class StepTrace(BaseModel):
    tool: str
    input: str
    output: str


TOOLS = {
    "search_docs": lambda query: f"docs:{query}",
    "get_order_status": lambda query: "status:shipped",
}


def choose_tool(question: str) -> str:
    if "order" in question:
        return "get_order_status"
    return "search_docs"


def run_agent(question: str) -> list[StepTrace]:
    tool = choose_tool(question)
    return [StepTrace(tool=tool, input=question, output=TOOLS[tool](question))]


def main() -> None:
    print([item.model_dump() for item in run_agent("check my order")])


if __name__ == "__main__":
    main()
