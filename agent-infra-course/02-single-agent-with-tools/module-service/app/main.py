from fastapi import FastAPI
from app.service import AgentRequest, run_agent

app = FastAPI(title="support-agent")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/run")
def run_route(payload: AgentRequest) -> dict[str, object]:
    return run_agent(payload.message)
