import requests
from datetime import datetime
import os

APP_ID = "587bfa6f"
API_KEY = "b245354b1f684dc4fbba4df27a3f6f3c"
date = datetime.now().strftime("%m/%d/%Y")
time = datetime.now().strftime("%I:%M%p")
sheet_endpoint = "https://api.sheety.co/422f3f32344a6b800351186a92330611/workoutTracking/workouts"
username = "savagesausage04"
password = "Sangjun04!"

user_input = input("What exercises did you do today? ")

parameters = {
    "query": user_input,
    "gender": "male",
    "height_cm": 170
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)

data = response.json()


for exercise in data["exercises"]:

    sheet_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }


    sheet_response = requests.post(
        url=sheet_endpoint,
        json=sheet_params,
        auth=(
            username,
            password,
        )
    )

    print(sheet_response.text)