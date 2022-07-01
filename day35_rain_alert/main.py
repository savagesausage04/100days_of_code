import requests
from twilio.rest import Client

api_key = "e7b011bd21bd1e0a00a5de4a820b9b08"
longitude = -117.826508
latitude = 33.684566

account_sid = "AC47cefb54da23e053f6131749d8e567ae"
auth_token = "764edbf047cafd5a70adf53756b8be77"

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour in range(0, 12):
    weather_code = data["hourly"][hour]["weather"][0]["id"]
    if int(weather_code) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(from_="+18456608440", to='+19494008938', body="It's going to rain. Bring an umbrella.")

    print(message.sid)