import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def ensure_user_and_get_token(username="calcuser", password="pwd123"):
    client.post("/users/register", json={"username": username, "password": password})
    r = client.post("/users/login", json={"username": username, "password": password})
    return r.json()["access_token"]

def test_bread_workflow():
    token = ensure_user_and_get_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Create
    r = client.post("/calculations/", json={"a": 10, "b": 5, "type": "Add"}, headers=headers)
    assert r.status_code == 200
    calc = r.json()
    assert calc["result"] == 15
    calc_id = calc["id"]

    # Read
    r2 = client.get(f"/calculations/{calc_id}", headers=headers)
    assert r2.status_code == 200
    assert r2.json()["id"] == calc_id

    # Browse
    r3 = client.get("/calculations", headers=headers)
    assert r3.status_code == 200
    assert isinstance(r3.json(), list)

    # Update -> multiply
    r4 = client.put(f"/calculations/{calc_id}", json={"type": "Multiply"}, headers=headers)
    assert r4.status_code == 200
    assert abs(r4.json()["result"] - 50) < 1e-6

    # Delete
    r5 = client.delete(f"/calculations/{calc_id}", headers=headers)
    assert r5.status_code == 204

    # Confirm deletion
    r6 = client.get(f"/calculations/{calc_id}", headers=headers)
    assert r6.status_code == 404

def test_invalid_calculation_creation():
    token = ensure_user_and_get_token("u2", "p2")
    headers = {"Authorization": f"Bearer {token}"}
    # divide by zero should be rejected by Pydantic schema (422) or by our code (400)
    r = client.post("/calculations/", json={"a": 5, "b": 0, "type": "Divide"}, headers=headers)
    assert r.status_code in (422, 400)
