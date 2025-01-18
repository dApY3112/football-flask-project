import pytest
from src.app import app  # Import your Flask app

@pytest.fixture
def client():
    # This will set up a test client that doesn't require the Flask server to be running
    with app.test_client() as client:
        yield client

def test_get_teams(client):
    response = client.get('/teams/')  # Add the trailing slash here to match the route
    assert response.status_code == 200


def test_get_players(client):
    response = client.get('/players/')
    assert response.status_code == 200
