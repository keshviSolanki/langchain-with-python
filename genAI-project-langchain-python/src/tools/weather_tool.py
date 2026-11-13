
import json
import os

import requests
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


@tool
def get_weather_data(city: str) -> str:
    """Get current weather information for a given city."""

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "OPENWEATHER_API_KEY is missing from the .env file."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        result = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature_c": data["main"]["temp"],
            "feels_like_c": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed_mps": data["wind"]["speed"],
            "condition": data["weather"][0]["description"],
            "weather_main": data["weather"][0]["main"]
        }

        return json.dumps(result)

    except requests.HTTPError as error:
        return f"Weather API error: {error.response.status_code} - {error.response.text}"

    except requests.RequestException as error:
        return f"Weather API request failed: {error}"

    except (KeyError, IndexError, ValueError, TypeError) as error:
        return f"Could not process weather data: {error}"
