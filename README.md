# Demo Django Project

This project demonstrates a simple Django setup. It now includes a basic weather
endpoint that can also send information to Slack using an incoming webhook.

## Weather Endpoint

The `/weather/` URL accepts an optional `city` query parameter. It fetches data
from the OpenWeather API using the `OPENWEATHER_API_KEY` environment variable
and posts the result to Slack if `SLACK_WEBHOOK_URL` is configured.

Example:

```
http://localhost:8000/weather/?city=Hanoi
```

## Requirements

```
Django==3.0.6
requests
```
