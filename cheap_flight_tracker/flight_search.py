import requests
from datetime import date, timedelta, datetime

AMADEUS_API_KEY = "799lXNaRTryb7dApR2yg69mJFfGMLpXt"
AMADEUS_API_SECRET= "6tGoshCcp8GDIGdw"

AMADEUS_AUTH_TOKEN_HEADER = {
    "content-type": "application/x-www-form-urlencoded"
}

AMADEUS_AUTH_BODY=f"grant_type=client_credentials&client_id={AMADEUS_API_KEY}&client_secret={AMADEUS_API_SECRET}"


auth_response = requests.post(
                          url="https://test.api.amadeus.com/v1/security/oauth2/token",
                          data=AMADEUS_AUTH_BODY,
                          headers=AMADEUS_AUTH_TOKEN_HEADER
                              )
token = auth_response.json()["access_token"]


AMADEUS_HEADER = {
    "authorization": f"Bearer {token}"
}

flight_search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

# params = {
#     "originLocationCode": "SYR",
#     "destinationLocationCode": "PDX",
#     "departureDate": "2025-02-17",
#     "adults": 1,
#     "travelClass": "ECONOMY",
#     "currencyCode": "USD",
#     "maxPrice": 200,
# }
#
# response = requests.get(url=flight_search_endpoint, params=params, headers=AMADEUS_HEADER)
# data = response.json()
# print(data["data"][0]["price"]["total"])
print(datetime.now())
six_month_range = [(date.today()+timedelta(days=num)).strftime("%Y-%m-%d") for num in range(240)]

for day in six_month_range:
    params = {
        "originLocationCode": "SYR",
        "destinationLocationCode": "PDX",
        "departureDate": day,
        "adults": 1,
        "travelClass": "ECONOMY",
        "currencyCode": "USD",
        "excludedAirlineCodes": "F9",
        "maxPrice": 180,
        "max": 1
    }
    response = requests.get(url=flight_search_endpoint, params=params, headers=AMADEUS_HEADER)
    data = response.json()
    if data["meta"]["count"]>0:
        print(f"Date: {day}, Price: {data["data"][0]["price"]["total"]}, carrier: {data["dictionaries"]['carriers']}")
    print(datetime.now())
