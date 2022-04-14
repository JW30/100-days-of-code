import requests
import datetime as dt

# Constants
GENDER: str = "YOUR GENDER"
WEIGHT: float = 0   # Edit your weight
HEIGHT: float = 0   # Edit your height
AGE: int = 0        # Edit your age

NUTRITIONIX_ENDPOINT: str = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID: str = "YOUR APP ID"
NUTRITIONIX_API_KEY: str = "YOUR NUTRITIONIX API KEY"
EXERCISE_HEADERS: dict = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0",
}

SHEETY_ENDPOINT: str = "YOUR SHEETY ENDPOINT"
BEARER_TOKEN: str = "YOUR BEARER TOKEN"
SHEET_HEADERS: dict = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# Get exercise data of the input activity.
exercise_params: dict = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

exercise_response: requests.models.Response = requests.post(url=NUTRITIONIX_ENDPOINT,
                                                            json=exercise_params,
                                                            headers=EXERCISE_HEADERS)
exercises: list = exercise_response.json()["exercises"]

# Append data to spreadsheet.
date_today: str = dt.date.today().strftime("%d/%m/%Y")
time_now: str = dt.datetime.now().strftime("%H:%M:%S")

for exercise in exercises:
    spreadsheet_params: dict = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=spreadsheet_params, headers=SHEET_HEADERS)
    print(sheet_response.status_code)
