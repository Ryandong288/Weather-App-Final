from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_weather_with_city():
    response = client.get("/weather?location=Boston")
    assert response.status_code == 200
    assert "Boston" in response.text  # Check if city name is displayed
    assert "Weather in Boston" in response.text