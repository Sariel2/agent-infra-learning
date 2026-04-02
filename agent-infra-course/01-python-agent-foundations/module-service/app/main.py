from fastapi import FastAPI
from app.service import GenerateRequest, generate

app = FastAPI(title="llm-gateway")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/generate")
def generate_route(payload: GenerateRequest) -> dict[str, object]:
    return generate(payload).model_dump()
