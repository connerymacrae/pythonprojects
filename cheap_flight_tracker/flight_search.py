import requests
from datetime import date, timedelta, datetime
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
# AMADEUS_API_SECRET= os.getenv("AMADEUS_API_SECRET")
#
# AMADEUS_AUTH_TOKEN_HEADER = {
#     "content-type": "application/x-www-form-urlencoded"
# }
#
# AMADEUS_AUTH_BODY=f"grant_type=client_credentials&client_id={AMADEUS_API_KEY}&client_secret={AMADEUS_API_SECRET}"
#
#
# auth_response = requests.post(
#                           url="https://test.api.amadeus.com/v1/security/oauth2/token",
#                           data=AMADEUS_AUTH_BODY,
#                           headers=AMADEUS_AUTH_TOKEN_HEADER
#                               )
# token = auth_response.json()["access_token"]
#
#
# AMADEUS_HEADER = {
#     "authorization": f"Bearer {token}"
# }
#
# flight_search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

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

def price_check(endpoint, header, sh_dict):
    for x in range(len(sh_dict)):
        six_month_range = [(date.today()+timedelta(days=(num+30))).strftime("%Y-%m-%d") for num in range(24)]

        for day in six_month_range:
            params = {
                "originLocationCode": "SYR",
                "destinationLocationCode": sh_dict[x][1],
                "departureDate": day,
                "adults": 1,
                "travelClass": "ECONOMY",
                "currencyCode": "USD",
                "excludedAirlineCodes": "F9",
                "maxPrice": sh_dict[x][2],
                "max": 1
            }
            response = requests.get(url=endpoint, params=params, headers=header)
            data = response.json()
            if "errors" in data or "warnings" in data:
                continue
            elif data["meta"]["count"]>0:
                print(f"Cheap {sh_dict[x][0]} flight found! Date: {day}, Price: {data['data'][0]['price']['total']}, "
                      f"carrier: {data['dictionaries']['carriers']}")




