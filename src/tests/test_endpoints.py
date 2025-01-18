# src/tests/test_endpoints.py
import requests

BASE_URL = "http://0.0.0.0:5000"

def test_get_teams():
    response = requests.get(f"{BASE_URL}/teams")
    assert response.status_code == 200

def test_get_players():
    response = requests.get(f"{BASE_URL}/players")
    assert response.status_code == 200
