import requests
from datetime import datetime, date, timedelta
import os
from dotenv import load_dotenv
from data_manager import destinations, add_city
from flight_search import price_check

#TODO: on main: run amadeus auth and get "access token"
#TODO: on main: create amadeus header
#TODO: on main: create SHEETY info(endpoint, auth token, header)

#TODO: insert travel destination and price into SHEETY
#TODO: create function: 1. get city from SHEETY,
#                       2. get iata code from AMADEUS,
#                       3. put iata code into SHEETY
#TODO: create function: 1. get iata codes and prices from SHEETY and create list
#                       2. create list of dates for the next six months
#                       3. get data from AMADEUS on flights < price to city for next six months
#                       4: create list of cheap flights
#TODO: create function: 1. send text message if flight in list

load_dotenv()


AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET= os.getenv('AMADEUS_API_SECRET')

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

AMADEUS_IATA_CODE_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_FLIGHT_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_HEADER = {"AUTHORIZATION": SHEETY_TOKEN}

q1 = input("Do you want to check flights(CHECK) or add a destination(ADD)?: ").lower()
if q1 == "add":
    add_city(AMADEUS_IATA_CODE_ENDPOINT, AMADEUS_HEADER, SHEETY_ENDPOINT, SHEETY_HEADER)
elif q1 == "check":
    destination_list = destinations(SHEETY_ENDPOINT, SHEETY_HEADER, "sheet1")
    price_check(AMADEUS_FLIGHT_SEARCH_ENDPOINT, AMADEUS_HEADER, destination_list)





