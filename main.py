# This script logs workout data to a Google Sheet using the Sheety API and Nutritionix API
import os
from datetime import datetime

import requests

from credentials import authorization

date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%H:%M:%S')

APP_ID = os.environ.get('APP_ID')

APP_KEY = os.environ.get('APP_KEY')
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}
parameters = {
    'query': input('What was the workout today?: '),
    'age': int(os.environ.get('age'))
}


workout_response = requests.post(
    url=URL, headers=nutritionix_headers, json=parameters)
workout_response.raise_for_status()
workout_data = workout_response.json()
# print(workout_data)
# print(workout_response.text)


sheety_header = {'Authorization': authorization}

username = os.environ.get('sheety_username')

url = f'https://api.sheety.co/{username}/myWorkoutsTracking/workouts'

json_parameters = {'workout': {
    'date': date,
    'time': time,
    'exercise': workout_data['exercises'][0]['name'].title(),
    'duration': workout_data['exercises'][0]['duration_min'],
    'calories': workout_data['exercises'][0]['nf_calories'],
}
}

sheety_response = requests.post(
    url=url, headers=sheety_header, json=json_parameters)
sheety_response.raise_for_status()
