import requests
from datetime import datetime
from Config import Config

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def ms_to_kmh(ms):
    return round(ms * 3.6, 2)

def get_weather():
    api_key = "abaf891f881f0013ba7df3fa450461b0"
    city = "Lisbon"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()

        temp_k = data.get("main").get("temp")
        feels_k = data.get("main").get("feels_like")

        wind_ms = data.get("wind").get("speed")

        weather = {
            "temp": kelvin_to_celsius(temp_k),
            "feels_like": kelvin_to_celsius(feels_k),
            "name": data.get("name"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),
            "description": data.get("weather")[0].get("description"),
            "wind_speed_kmh": ms_to_kmh(wind_ms),

        }

        return weather
    except Exception as e:
        print(e)



