import pytest
from fastapi.testclient import TestClient

from . import crud, schemas



def test_health_and_docs(client):
    response = client.get("/docs")
    assert response.status_code == 200


def test_token_login_and_roles(client):
    response = client.post("/token?username=admin&password=admin123")
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    auth = {"Authorization": f"Bearer {data['access_token']}"}
    resp2 = client.get("/transactions", headers=auth)
    assert resp2.status_code == 200


def test_crud_transactions_admin(client):
    # create an admin token
    token_resp = client.post("/token?username=admin&password=admin123")
    token = token_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # create a transaction
    tx = {
        "amount": 1234.5,
        "type": "income",
        "category": "salary",
        "date": "2026-04-01",
        "notes": "April salary",
        "owner_id": 1,
    }
    create_resp = client.post("/transactions", json=tx, headers=headers)
    assert create_resp.status_code == 201
    created = create_resp.json()
    assert created["amount"] == 1234.5

    # fetch by id
    get_resp = client.get(f"/transactions/{created['id']}", headers=headers)
    assert get_resp.status_code == 200

    # update
    update_resp = client.put(f"/transactions/{created['id']}", json={
        "notes": "updated"
    }, headers=headers)
    assert update_resp.status_code == 200
    assert update_resp.json()["notes"] == "updated"

    # delete
    del_resp = client.delete(f"/transactions/{created['id']}", headers=headers)
    assert del_resp.status_code == 204


def test_summary_calculation(client):
    token_resp = client.post("/token?username=admin&password=admin123")
    token = token_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # add two tx
    client.post(
        "/transactions",
        json={"amount": 100.0, "type": "income", "category": "freelance", "date": "2026-04-10", "notes": "", "owner_id": 1},
        headers=headers,
    )
    client.post(
        "/transactions",
        json={"amount": 30.0, "type": "expense", "category": "food", "date": "2026-04-11", "notes": "","owner_id": 1},
        headers=headers,
    )

    summary_resp = client.get("/summary", headers=headers)
    assert summary_resp.status_code == 200
    data = summary_resp.json()
    assert data["total_income"] >= 100
    assert data["total_expense"] >= 30
    assert "balance" in data
