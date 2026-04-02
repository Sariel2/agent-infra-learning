from fastapi import FastAPI
from app.service import CompareRequest, RecommendRequest, compare, recommend

app = FastAPI(title="architecture-lab")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/compare")
def compare_route(payload: CompareRequest) -> dict[str, list[str]]:
    return compare(payload.task)


@app.post("/recommend")
def recommend_route(payload: RecommendRequest) -> dict[str, str]:
    return {"recommendation": recommend(payload.open_ended, payload.steps_fixed, payload.tool_variance)}
