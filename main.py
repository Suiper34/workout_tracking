import os

import requests

APP_ID = os.environ.get('APP_ID')

APP_KEY = os.environ.get('APP_KEY')
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}
parameters = {
    'query': input('What was the workout today?: '),
    'age': int(os.environ.get('age'))
}


workout_response = requests.post(url=URL, headers=headers, json=parameters)
workout_response.raise_for_status()
workout_data = workout_response.json()
print(workout_data)
