from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_recommend_route_returns_workflow() -> None:
    response = client.post("/recommend", json={"open_ended": False, "steps_fixed": True, "tool_variance": False})
    assert response.status_code == 200
    assert response.json()["recommendation"] == "workflow"
