import pytest
from fastapi.testclient import TestClient
from app.endpoints.api import app
from app.util.utilities import create_valid_nvda_test_data


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_endpoint_success(client):
    test_data = create_valid_nvda_test_data()
    response = client.post("/predict", json=test_data.to_dict(orient="records")[0])
    assert response.status_code == 200
    json_response = response.json()
    assert "signal" in json_response
    assert "confidence" in json_response

def test_predict_endpoint_empty_input(client):
    response = client.post("/predict", json={})
    assert response.status_code == 400
    json_response = response.json()
    assert "error" in json_response


def test_predict_endpoint_invalid_input(client):
    response = client.post("/predict", json={"invalid": "data"})
    assert response.status_code == 400
    json_response = response.json()
    assert "error" in json_response


def test_unknown_route(client):
    response = client.get("/unknown")
    assert response.status_code == 404
    json_response = response.json()
    assert "error" in json_response

