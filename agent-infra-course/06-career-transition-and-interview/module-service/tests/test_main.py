from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_story_route() -> None:
    response = client.post("/story", json={"name": "knowledge-agent", "goal": "answer questions", "improvement": "better traceability"})
    assert response.status_code == 200
    assert "knowledge-agent" in response.json()["resume_bullet"]
