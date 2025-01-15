import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')

NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')

NTX_HEADERS = {
    "Content-Type": 'application/json',
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

nat_lang_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

workout = {
    # "query": input("Describe your workout: ")
    "query": 'i rowed for 45 min and swam for 1 mile'
}

ntx_response = requests.post(url=nat_lang_exercise_endpoint, json=workout, headers=NTX_HEADERS)
data = ntx_response.json()
for item in data['exercises']:
    print(item['name'])

# print(data['exercises'][1])

sheety_post_endpoint = os.getenv('SHEETY_POST_ENDPOINT')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

SHEETY_HEADERS = {
    "Authorization": SHEETY_TOKEN,
}


for item in data['exercises']:
    sheety_format_workout = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%I:%M %p"),
            "exercise":item['name'],
            "duration": item['duration_min'],
            "calories": item['nf_calories'],
        }
    }
    print(sheety_format_workout)
    sheety_response = requests.post(url=sheety_post_endpoint, json=sheety_format_workout, headers=SHEETY_HEADERS)
    print(sheety_response.text)
