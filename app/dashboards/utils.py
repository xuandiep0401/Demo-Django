import os
import requests


def get_weather(city: str) -> str:
    """Fetch weather information for a city using OpenWeather API."""
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    if not api_key:
        return "Missing OPENWEATHER_API_KEY"
    url = (
        "http://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric"
    )
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if 'main' not in data:
            return f"Unable to fetch weather for {city}"
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Weather in {city}: {desc}, {temp}°C"
    except Exception as exc:
        return f"Error fetching weather: {exc}"


def send_to_slack(message: str) -> None:
    """Send a message to Slack using an incoming webhook."""
    webhook = os.environ.get('SLACK_WEBHOOK_URL')
    if not webhook:
        return
    try:
        requests.post(webhook, json={"text": message}, timeout=10)
    except Exception:
        pass
