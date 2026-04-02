from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ask_route_returns_citations() -> None:
    response = client.post("/ask", json={"question": "What is rag?"})
    assert response.status_code == 200
    assert "citations" in response.json()
