import requests
from datetime import datetime
import os
import dotenv

dotenv.load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER = os.environ.get("BEARER")


header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Give exersizes to add?")
}

url = "https://trackapi.nutritionix.com/v2/natural/exercise"


today_time = datetime.now()
today_time.date

response = requests.post(url, json=parameters, headers=header)
activities = response.json()


header = {
    "Authorization": BEARER,
}


for list in activities["exercises"]:
    sheet_input = {
        "workout": {
            "date": str(today_time.strftime("%d/%m/%Y")),
            "time": str(today_time.strftime("%H:%M")),
            "exercise": list["name"],
            "duration": list["duration_min"],
            "calories": list["nf_calories"],
        },
    }
    sheety_end_point = "https://api.sheety.co/6af4e9db164ab253ab8939625fae7684/myWorkoutsPython/workouts"

    response = requests.post(
        sheety_end_point, json=sheet_input, headers=header)
