import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")

account_sid = os.getenv("TWIL_ACCT_SID")
auth_token = os.getenv("TWIL_AUTH_TOKEN")


weather_params = {
"lat": 49.234669,
"lon": -124.807587,
"cnt": 5,
"appid": api_key,
}

response = requests.get(OWM_Endpoint, weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_= "whatsapp:+14155238886",
        body="You will want an Umbrella today!",
        to = "whatsapp:+17735805744",
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="No Umbrella needed Today!",
        to="whatsapp:+17735805744",
    )
    print(message.status)

#     print("Sunglasses are in order!")

# def rain_warning(data):
#     for num in range(4):
#         if data["list"][num]["weather"][0]["id"] < 700:
#             return True
#         else:
#             return False
#
# if rain_warning(weather_data):
#     print("Bring an Umbrella today!")
# else:
#     print("Make sure you have your sunglasses!")


