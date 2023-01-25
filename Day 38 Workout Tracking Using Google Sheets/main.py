import requests
from datetime import datetime
# used for basic authentication
from requests.auth import HTTPBasicAuth
import os
print(os.environ)

nutritionix_APP_ID = os.environ.get("APP_ID")
nutritionix_api_key = os.environ["API_KEY"]

nutritionix_exercise_endpoint = os.environ.get("NUTRITIONIX_ENDPOINT")
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]

query = input("Tell me what exercises you did today?: ")

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

username = os.environ["USERNAME"]
password = os.environ.get("PASSWORD")

headers = {
    "x-app-id": nutritionix_APP_ID,
    "x-app-key": nutritionix_api_key,
    "Content-Type": "application/json"
}

parameters = {
    "query": query
}
# response = {
#     "query":"ran 3 miles",
#     "gender":"female",
#     "weight_kg":72.5,
#     "height_cm":167.64,
#     "age":30
# }
"""When using inputs, use json not params"""
response = requests.post(url=nutritionix_exercise_endpoint, headers=headers, json=parameters)
response.raise_for_status()
data = response.json()
exercises = len(data["exercises"])
for exercise in range(exercises):
    exercise_type = data["exercises"][exercise]["name"].title()
    duration = data["exercises"][exercise]["duration_min"]
    calories = data["exercises"][exercise]["nf_calories"]

    print(exercise_type, duration, calories)

    sheety_headers = {
        "api_key": os.environ.get("SHEETY_API_KEY"),
        "Authorization": os.environ["TOKEN"]
    }

    basic = HTTPBasicAuth(username, password)

    sheety_params = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise_type,
            "duration": duration,
            "calories": calories,
    }
}

    response_2 = requests.post(url=sheety_endpoint, json=sheety_params, auth=basic)
    response_2.raise_for_status()
    sheety_data = response_2.json()
    print(sheety_data)
    print(response_2.text)