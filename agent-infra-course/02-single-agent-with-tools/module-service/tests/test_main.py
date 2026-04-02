from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_run_route_returns_trace() -> None:
    response = client.post("/run", json={"message": "check my order"})
    assert response.status_code == 200
    assert response.json()["trace"][0]["tool"] == "get_order_status"
