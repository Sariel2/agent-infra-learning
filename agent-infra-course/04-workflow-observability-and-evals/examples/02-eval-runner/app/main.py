from pydantic import BaseModel


class EvalCase(BaseModel):
    prompt: str
    expected_tool: str


class EvalResult(BaseModel):
    prompt: str
    matched: bool


DATASET = [
    EvalCase(prompt="check order", expected_tool="get_order_status"),
    EvalCase(prompt="search docs", expected_tool="search_docs"),
]


def choose_tool(prompt: str) -> str:
    return "get_order_status" if "order" in prompt else "search_docs"


def run_eval() -> list[EvalResult]:
    return [EvalResult(prompt=item.prompt, matched=choose_tool(item.prompt) == item.expected_tool) for item in DATASET]


def main() -> None:
    print([item.model_dump() for item in run_eval()])


if __name__ == "__main__":
    main()
