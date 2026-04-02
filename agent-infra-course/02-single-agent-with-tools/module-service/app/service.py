from pydantic import BaseModel


class AgentRequest(BaseModel):
    message: str


class ToolTrace(BaseModel):
    tool: str
    args: dict[str, str]
    result: str


DOCS = {"agent": "Agent infra uses tools and traces."}
ORDERS = {"42": "shipped"}


def search_docs(query: str) -> str:
    return DOCS.get(query, "not-found")


def get_order_status(order_id: str) -> str:
    return ORDERS.get(order_id, "unknown")


def create_ticket(topic: str) -> str:
    return f"ticket-created:{topic}"


def run_agent(message: str) -> dict[str, object]:
    if "order" in message:
        trace = ToolTrace(tool="get_order_status", args={"order_id": "42"}, result=get_order_status("42"))
        return {"answer": trace.result, "trace": [trace.model_dump()]}
    if "ticket" in message:
        trace = ToolTrace(tool="create_ticket", args={"topic": message}, result=create_ticket(message))
        return {"answer": trace.result, "trace": [trace.model_dump()]}
    trace = ToolTrace(tool="search_docs", args={"query": "agent"}, result=search_docs("agent"))
    return {"answer": trace.result, "trace": [trace.model_dump()]}
