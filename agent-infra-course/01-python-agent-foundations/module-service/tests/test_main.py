from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_route() -> None:
    response = client.post("/generate", json={"prompt": "hello"})
    assert response.status_code == 200
    assert response.json()["answer"].startswith("Stub answer")
