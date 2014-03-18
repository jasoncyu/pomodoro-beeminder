# http://www.saintsal.com/2013/01/forcing-myself-to-take-pomodoro-breaks/
import requests
import sys
import time

pomodoroName = sys.argv[1]
print pomodoroName

url = 'https://www.beeminder.com/api/v1/users/zinbiel/goals/pom/datapoints.json'
data = {}
data["auth_token"] = "GyCzXFnDQNMmBPqSwWDb"
data["timestamp"] = time.time()
data["value"] = 1
data["comment"] = pomodoroName

r = requests.post(url, data=data)
print r.text
