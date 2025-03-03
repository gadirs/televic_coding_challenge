import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_valid_prime(client):
    response = client.get('/prime/10')
    assert response.status_code == 200
    assert response.json == {"n": 10, "nth_prime": 29}

def test_prime_zero(client):
    response = client.get('/prime/0')
    assert response.status_code == 400
    assert response.json == {"error": "n must be greater than 0"}

def test_prime_negative(client):
    response = client.get('/prime/-5')
    assert response.status_code == 400
    assert response.json == {"error": "n must be greater than 0"}

def test_invalid_string(client):
    response = client.get('/prime/abc')
    assert response.status_code == 400
    assert response.json == {"error": "n must be a valid integer"}

def test_prime_large_number(client):
    response = client.get('/prime/1000')
    assert response.status_code == 200
    assert response.json["n"] == 1000
    assert response.json["nth_prime"] == 7919