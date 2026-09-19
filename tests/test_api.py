from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_status():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "mini-ci-cd is running"}

def test_get_addition():
    response = client.get("/add?a=1&b=1")

    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_get_subtraction():
    response = client.get("/subtract?a=1&b=1")

    assert response.status_code == 200
    assert response.json() == {"result": 0}
