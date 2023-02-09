import requests
import os
from twilio.rest import Client

# ---------------------------- VARIABLES ------------------------------- #

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "[]"

parameters = {
    "lat": 53.5488,
    "lon": 9.9872,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

account_sid = "[]"
auth_token = "[]"

# ---------------------------- GETTING CURRENT WEATHER DATA USING API ------------------------------- #

response = requests.get(OWM_endpoint, params=parameters)

# Raising errors and exceptions
response.raise_for_status()

# Data to json
weather_data = response.json()

# Extract weather condition id and save to list
weather_data = weather_data["hourly"][:12]
print(weather_data[0]["weather"][0]["id"])

weather_forecast = [weather_data[item]["weather"][0]["id"] for item in range(0, 12)]
min_number_forecast = int(min(weather_forecast))

# Sending SMS
if min_number_forecast < 700:
    print("Bring umbrella. In the next 12 hours will rain!")
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Bring umbrella. In the next 12 hours will rain!",
                         from_='+XXXX',
                         to='+XXXX'
                     )

    print(message.status)