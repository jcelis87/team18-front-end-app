import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.getenv("API_URL")
print(os.getenv("API_URL"))


def get_all_geonames():
    API_URL = os.getenv("API_URL")
    URL = API_URL + "/geographic-names/"
    response = requests.get(URL)

    # print(response.json())
    return response.json()
