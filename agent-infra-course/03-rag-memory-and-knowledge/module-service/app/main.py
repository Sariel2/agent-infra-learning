from fastapi import FastAPI
from app.service import AskRequest, ask

app = FastAPI(title="knowledge-agent")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask")
def ask_route(payload: AskRequest) -> dict[str, object]:
    return ask(payload.question)
