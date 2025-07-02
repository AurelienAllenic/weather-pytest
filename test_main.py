import json
from main import get_weather_data

def test_weather_data_structure():
    data = get_weather_data(48.85, 2.35, "2025-07-01", "2025-07-02")
    assert "daily" in data
    assert "temperature_2m_max" in data["daily"]
    assert "temperature_2m_min" in data["daily"]
    assert len(data["daily"]["time"]) > 0
