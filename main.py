import requests
import os
from twilio.rest import Client
# Needed to run the code in Pythonanywhere
from twilio.http.http_client import TwilioHttpClient

# ---------------------------- VARIABLES ------------------------------- #

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = os.environ["OWM_API_KEY"]

parameters = {
    "lat": 53.5488,
    "lon": 9.9872,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
from_number = os.environ["FROM_NUMBER"]
to_number = os.environ["TO_NUMBER"]

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
    # Needed to run the code in Pythonanywhere
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
                    .create(
                         body="Bring umbrella. In the next 12 hours will rain!",
                         from_=from_number,
                         to=to_number
                     )

    print(message.status)
