from fastapi.testclient import TestClient

from app.main import app
from app.signals import all_signals, search_signal

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

def test_healthz():
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "mini-ci-cd",
    }

def test_get_signals():
    response = client.get('/signals')

    assert response.status_code == 200
    assert response.json() == all_signals()

def test_get_signal_normal():
    response = client.get('/signals/AAPL')

    assert response.status_code == 200
    assert response.json() == search_signal('AAPL')

def test_get_signal_lowercase():
    response = client.get('/signals/aapl')

    assert response.status_code == 200
    assert response.json() == search_signal('AAPL')

def test_get_signal_unknown_symbol():
    response = client.get('/signals/UNKNOWN')

    assert response.status_code == 404
    assert response.json() == {"detail":"Signal not found for symbol: UNKNOWN"}
