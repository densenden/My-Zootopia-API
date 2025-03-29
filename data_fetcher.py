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
  Returns None if the animal doesn't exist or if there's an API error.
  """
  headers = {'X-Api-Key': API_KEY}
  try:
    response = requests.get(API_URL + animal_name, headers=headers, timeout=5)
    if response.status_code == 200:
      data = response.json()
      # If API returns empty list, animal doesn't exist
      if data:
        return data
      else:
        return None
    else:
      print(f"Error: API responded with status code {response.status_code}")
      return None
  except requests.exceptions.Timeout:
    print("Request timed out. The server took too long to respond.")
    return None
  except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API request: {e}")
    return None