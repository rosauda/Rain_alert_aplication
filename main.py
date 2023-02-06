import requests

# ---------------------------- VARIABLES ------------------------------- #

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "[]"

parameters = {
    "lat": 53.5488,
    "lon": 9.9872,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

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

for id in weather_forecast:
    if id < 800:
        print("Will rain, please take your umbrella")
    else:
        pass

