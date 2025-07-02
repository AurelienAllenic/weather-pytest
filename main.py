import requests
import json
import matplotlib.pyplot as plt

def get_weather_data(lat, lon, start_date, end_date):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&"
        f"daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_data(data, filename="meteo.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def plot_weather(data):
    dates = data["daily"]["time"]
    temp_max = data["daily"]["temperature_2m_max"]
    temp_min = data["daily"]["temperature_2m_min"]

    plt.plot(dates, temp_max, label="Temp max", color="red")
    plt.plot(dates, temp_min, label="Temp min", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Température (°C)")
    plt.title("Prévisions météo")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    lat, lon = 48.85, 2.35  # Paris
    start_date = "2025-07-01"
    end_date = "2025-07-07"

    weather = get_weather_data(lat, lon, start_date, end_date)
    save_data(weather)
    plot_weather(weather)
