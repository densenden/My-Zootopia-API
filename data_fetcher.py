import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file and connet to the API
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
  """
  Fetches data from an API and returns it in JSON format.
  """
  headers = {
    'X-Api-Key': API_KEY
  }
  response = requests.get(API_URL + animal_name, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    response.raise_for_status()