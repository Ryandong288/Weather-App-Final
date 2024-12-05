from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_weather_missing_api_key(monkeypatch):
    response = client.get("/weather?location=NOAPI")
    assert response.status_code == 500
    assert "API key not set" in response.text