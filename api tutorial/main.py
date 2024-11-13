import requests
from datetime import datetime

MY_LAT = 43.032760
MY_LONG = -76.116980
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# print(response.status_code)
#
# # if response.status_code == 404:
# #     raise Exception("That resource does nto exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorized to access this data.")
#
# # use to get exception for any request that was not successful
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_time = data["results"]['sunrise'].split("T")[1]
sunset_time = data['results']['sunset']

sunrise_hour = sunrise_time.split(":")[0]
sunset_hour = sunset_time.split("T")[1].split(":")[0]

print(data["results"]["sunrise"])
print(sunrise_hour, sunset_hour)

time_now = datetime.now()
now_hour = time_now.hour

print(now_hour)
