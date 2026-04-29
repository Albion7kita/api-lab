import requests
import json

def get_data(url, params=None):
    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        print("Request failed:", e)
        return None


url = "https://api.open-meteo.com/v1/forecast"

# Call 1: Chicago
params = {
    "latitude": 41.88,
    "longitude": -87.63,
    "current_weather": True
}

data = get_data(url, params)

if data:
    weather = data["current_weather"]
    print("\nChicago Weather:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind Speed: {weather['windspeed']} km/h")


# Call 2: Forecast
params = {
    "latitude": 41.88,
    "longitude": -87.63,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto"
}

data = get_data(url, params)

if data:
    print("\nForecast:")
    print(json.dumps(data["daily"], indent=2))


# Call 3: New York
params = {
    "latitude": 40.71,
    "longitude": -74.00,
    "current_weather": True
}

data = get_data(url, params)

if data:
    weather = data["current_weather"]
    print("\nNew York Weather:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind Speed: {weather['windspeed']} km/h")