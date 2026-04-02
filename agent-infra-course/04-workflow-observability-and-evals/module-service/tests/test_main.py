from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_eval_route() -> None:
    response = client.get("/eval")
    assert response.status_code == 200
    assert all(item["matched"] for item in response.json())
