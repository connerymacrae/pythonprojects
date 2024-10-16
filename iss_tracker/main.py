import requests
from datetime import datetime

MY_LAT = 43.032760
MY_LONG = -76.116980

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()

iss_lng = float(iss_data["iss_position"]["longitude"])
iss_lat = float(iss_data["iss_position"]["latitude"])

iss_position = (iss_lng, iss_lat)

print(f'iss pos is: {iss_position}')


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "America/New_York"

}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_time = data["results"]['sunrise'].split("T")[1]
sunset_time = data['results']['sunset']

sunrise_hour = int(sunrise_time.split(":")[0])
sunset_hour = int(sunset_time.split("T")[1].split(":")[0])

print(f'it is dark between {sunset_hour} and {sunrise_hour}')

now_hour = datetime.now().hour

print(f"it is currently {now_hour}")

# is it between the hours of sunset and sunrise:
dark_outside = False
if now_hour >= sunset_hour or now_hour <= sunrise_hour:
    dark_outside = True

is_overhead = False
if (MY_LONG-5) < iss_lng < (MY_LONG+5) and (MY_LAT-5) < iss_lat < (MY_LAT+5):
    is_overhead = True

if is_overhead and dark_outside:
