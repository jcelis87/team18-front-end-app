import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = os.getenv("API_URL")
print(os.getenv("API_URL"))


def get_image_url(id):
    API_URL = os.getenv("API_URL")
    URL = API_URL + "/image/"
    response = URL + id

    return response


def get_all_geonames():
    API_URL = os.getenv("API_URL")
    URL = API_URL + "/geographic-names/"
    response = requests.get(URL)

    return response.json()


def get_all_coordinates(id):
    API_URL = os.getenv("API_URL")
    URL = API_URL + "/coordinates/" + id
    response = requests.get(URL)

    return response.json()


def get_all_boundaries(id):
    API_URL = os.getenv("API_URL")
    URL = API_URL + "/boundaries/" + id
    response = requests.get(URL)

    return response.json()


def get_all_image_boundaries(id):
    API_URL = os.getenv("API_URL")
    URL = API_URL + "/image-boundaries/" + id
    response = requests.get(URL)

    return response.json()


def send_file(my_file_path):
    API_URL = os.getenv("API_URL")
    URL = API_URL + "/uploadfile/"

    data = open(my_file_path, "rb").read()
    r = requests.post(URL, data=data)

    # esponse = requests.post(URL, files=my_file)

    return "file sent"
