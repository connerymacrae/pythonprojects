import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL = "crypticactuarial@gmail.com"
PASSWORD = 'dtnhrafldzsivkhu'

MY_LAT = 43.032760
MY_LONG = -76.116980

def is_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_lng = float(iss_data["iss_position"]["longitude"])
    iss_lat = float(iss_data["iss_position"]["latitude"])

    if (MY_LONG - 5) < iss_lng < (MY_LONG + 5) and (MY_LAT - 5) < iss_lat < (MY_LAT + 5):
        return True


def dark_outside():
    now_hour = datetime.now().hour
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

    if now_hour >= sunset_hour or now_hour <= sunrise_hour:
        return True


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # email security layer
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Look UP!!\n\nThe International Space Station should be visible in the sky right now. Look Up!"
        )


while is_overhead() and dark_outside():
    send_email()
    time.sleep(60)
