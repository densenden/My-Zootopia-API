import requests
import os
from dotenv import load_dotenv

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.api-ninjas.com/v1/animals?name="

load_dotenv()

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  response = requests.get(API_URL + animal_name, headers={"X-Api-Key": API_KEY})
  return response.json() if response.status_code == 200 else []