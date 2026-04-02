from fastapi import FastAPI
from app.service import RunRequest, evaluate, run_runtime

app = FastAPI(title="agent-runtime")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/run")
def run_route(payload: RunRequest) -> dict[str, object]:
    return run_runtime(payload.message)


@app.get("/eval")
def eval_route() -> list[dict[str, object]]:
    return evaluate()
