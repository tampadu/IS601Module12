from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_calculation():
    response = client.post("/calculations/", json={"a":5,"b":3,"type":"Add"})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 8
