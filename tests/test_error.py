from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_weather_invalid_city():
    response = client.get("/weather?location=InvalidCity")
    assert response.status_code == 404
    assert "City not found" in response.text