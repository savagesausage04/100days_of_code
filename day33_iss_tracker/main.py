import requests
from datetime import datetime
import time

MY_LAT = 33.685910
MY_LONG = -117.824720

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


def is_dark():
    if sunset < time_now or sunrise < time_now:
        return True


time_now = datetime.now().hour
while True:
    time.sleep(60)
    if (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and (MY_LONG - 5 < iss_longitude < MY_LONG + 5) and is_dark():
        print("The ISS is overhead!")
    # supposed to use smtp to send an email but it doesn't work :(
