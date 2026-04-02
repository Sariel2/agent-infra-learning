from pydantic import BaseModel


class RunRequest(BaseModel):
    message: str


DATASET = [
    {"message": "check my order", "expected_node": "order_lookup"},
    {"message": "search docs", "expected_node": "doc_search"},
]


def classify_node(message: str) -> str:
    return "order_lookup" if "order" in message else "doc_search"


def run_runtime(message: str) -> dict[str, object]:
    node = classify_node(message)
    trace = [
        {"node": "classify", "message": message},
        {"node": node, "status": "completed"},
        {"node": "respond", "status": "completed"},
    ]
    return {"answer": f"handled by {node}", "trace": trace}


def evaluate() -> list[dict[str, object]]:
    return [
        {
            "message": case["message"],
            "matched": classify_node(case["message"]) == case["expected_node"],
        }
        for case in DATASET
    ]
