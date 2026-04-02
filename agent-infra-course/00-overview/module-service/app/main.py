from fastapi import FastAPI
from app.service import summarize_workspace

app = FastAPI(title="starter-workspace")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/summary")
def summary() -> dict[str, object]:
    return summarize_workspace()
