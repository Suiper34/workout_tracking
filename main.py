import os

import requests

APP_ID = os.environ.get('APP_ID')

APP_KEY = os.environ.get('APP_KEY')
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,

}

workout_response = requests.post(url=URL, headers=headers)
