from fastapi.testclient import TestClient
from app.endpoints import app

client = TestClient(app)


def test_app_is_ready():
    response = client.get("/")
    assert response.status_code == 200
