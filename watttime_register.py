import requests
import json

WATTTIME_REGISTER_URL = 'https://api2.watttime.org/v2/register'
"""
params format:
    {"username": "kschen",
    "password": "carbontrackertest",
    "email": "kschen@mit.edu",
    "org": "mit"}
"""
params = json.load(open("watttime_credentials.json"))
print(params)
rsp = requests.post(WATTTIME_REGISTER_URL, json=params)
print(rsp.text)
