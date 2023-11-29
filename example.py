from carbontracker.tracker import CarbonTracker, CarbonTrackerManual
from requests.auth import HTTPBasicAuth
import json
import time
import requests


WATTTIME_LOGIN_URL = 'https://api2.watttime.org/v2/login'
params = json.load(open("watttime_credentials.json"))
username, password = params["username"], params["password"]
print(username, password)
rsp = requests.get(WATTTIME_LOGIN_URL, auth=HTTPBasicAuth(username, password))
watttime_token = rsp.json()['token']

tracker = CarbonTracker(epochs=1, monitor_epochs=1, update_interval=1,
        components='all', epochs_before_pred=1, log_dir='logs', verbose=2, api_keys={"watttime": watttime_token})
# tracker.tracker.pue_manual=1.59
# tracker.intensity_updater.ci_manual = 294

max_epochs = 1
for epoch in range(max_epochs):
    tracker.epoch_start()

    time.sleep(10)

    tracker.epoch_end('test')