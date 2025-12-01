from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_register_and_login():
    # register user
    r = client.post("/users/register", json={"username": "tester", "password": "pass123"})
    assert r.status_code == 201
    data = r.json()
    assert data["username"] == "tester"

    # login
    r2 = client.post("/users/login", json={"username": "tester", "password": "pass123"})
    assert r2.status_code == 200
    token = r2.json().get("access_token")
    assert token is not None

def test_register_duplicate_fails():
    client.post("/users/register", json={"username": "dupuser", "password": "x"})
    r = client.post("/users/register", json={"username": "dupuser", "password": "x"})
    assert r.status_code == 400
