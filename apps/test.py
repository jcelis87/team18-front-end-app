import requests
import os

print(os.getenv("API_URL"))
path = requests.get(os.getenv("API_URL") + "/get_abspath").json()["path"]
print(type(path))
print(path)