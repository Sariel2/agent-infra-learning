from fastapi import FastAPI
from app.service import QARequest, StoryRequest, answer, build_story

app = FastAPI(title="showcase-pack")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/story")
def story_route(payload: StoryRequest) -> dict[str, str]:
    return build_story(payload.name, payload.goal, payload.improvement)


@app.post("/qa")
def qa_route(payload: QARequest) -> dict[str, str]:
    return {"answer": answer(payload.topic)}
