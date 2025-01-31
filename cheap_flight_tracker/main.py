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

# q1 = input("Do you want to check flights(CHECK) or add a destination(ADD)?: ").lower()
# if q1 == "add":
#     add_city(AMADEUS_IATA_CODE_ENDPOINT, AMADEUS_HEADER, SHEETY_ENDPOINT, SHEETY_HEADER)
# elif q1 == "check":
#     destination_list = destinations(SHEETY_ENDPOINT, SHEETY_HEADER, "sheet1")
#     price_check(AMADEUS_FLIGHT_SEARCH_ENDPOINT, AMADEUS_HEADER, destination_list)

data = {'meta': {'count': 1, 'links': {'self': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=SYR&destinationLocationCode=PDX&departureDate=2025-03-04&adults=1&travelClass=ECONOMY&currencyCode=USD&excludedAirlineCodes=F9&maxPrice=180&max=1'}}, 'data': [{'type': 'flight-offer', 'id': '1', 'source': 'GDS', 'instantTicketingRequired': False, 'nonHomogeneous': False, 'oneWay': False, 'isUpsellOffer': False, 'lastTicketingDate': '2025-01-30', 'lastTicketingDateTime': '2025-01-30', 'numberOfBookableSeats': 9, 'itineraries': [{'duration': 'PT8H24M', 'segments': [{'departure': {'iataCode': 'SYR', 'at': '2025-03-04T06:30:00'}, 'arrival': {'iataCode': 'ORD', 'terminal': '1', 'at': '2025-03-04T08:05:00'}, 'carrierCode': 'UA', 'number': '660', 'aircraft': {'code': '320'}, 'operating': {'carrierCode': 'UA'}, 'duration': 'PT2H35M', 'id': '1', 'numberOfStops': 0, 'blacklistedInEU': False}, {'departure': {'iataCode': 'ORD', 'terminal': '1', 'at': '2025-03-04T09:11:00'}, 'arrival': {'iataCode': 'PDX', 'at': '2025-03-04T11:54:00'}, 'carrierCode': 'UA', 'number': '1994', 'aircraft': {'code': '739'}, 'operating': {'carrierCode': 'UA'}, 'duration': 'PT4H43M', 'id': '2', 'numberOfStops': 0, 'blacklistedInEU': False}]}], 'price': {'currency': 'USD', 'total': '174.17', 'base': '138.77', 'fees': [{'amount': '0.00', 'type': 'SUPPLIER'}, {'amount': '0.00', 'type': 'TICKETING'}], 'grandTotal': '174.17'}, 'pricingOptions': {'fareType': ['PUBLISHED'], 'includedCheckedBagsOnly': False}, 'validatingAirlineCodes': ['UA'], 'travelerPricings': [{'travelerId': '1', 'fareOption': 'STANDARD', 'travelerType': 'ADULT', 'price': {'currency': 'USD', 'total': '174.17', 'base': '138.77'}, 'fareDetailsBySegment': [{'segmentId': '1', 'cabin': 'ECONOMY', 'fareBasis': 'KAU4AZDS', 'brandedFare': 'ECONOMY', 'brandedFareLabel': 'ECONOMY', 'class': 'K', 'includedCheckedBags': {'quantity': 0}, 'amenities': [{'description': 'CHECKED BAG FIRST', 'isChargeable': True, 'amenityType': 'BAGGAGE', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'SECOND BAG', 'isChargeable': True, 'amenityType': 'BAGGAGE', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'PRE RESERVED SEAT ASSIGNMENT', 'isChargeable': False, 'amenityType': 'PRE_RESERVED_SEAT', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'PRIORITY BOARDING', 'isChargeable': True, 'amenityType': 'TRAVEL_SERVICES', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'ECONOMY TO ECONOMY PLUS', 'isChargeable': True, 'amenityType': 'UPGRADES', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'MILEAGE ACCRUAL', 'isChargeable': False, 'amenityType': 'BRANDED_FARES', 'amenityProvider': {'name': 'BrandedFare'}}]}, {'segmentId': '2', 'cabin': 'ECONOMY', 'fareBasis': 'KAU4AZDS', 'brandedFare': 'ECONOMY', 'brandedFareLabel': 'ECONOMY', 'class': 'K', 'includedCheckedBags': {'quantity': 0}, 'amenities': [{'description': 'CHECKED BAG FIRST', 'isChargeable': True, 'amenityType': 'BAGGAGE', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'SECOND BAG', 'isChargeable': True, 'amenityType': 'BAGGAGE', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'PRE RESERVED SEAT ASSIGNMENT', 'isChargeable': False, 'amenityType': 'PRE_RESERVED_SEAT', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'PRIORITY BOARDING', 'isChargeable': True, 'amenityType': 'TRAVEL_SERVICES', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'ECONOMY TO ECONOMY PLUS', 'isChargeable': True, 'amenityType': 'UPGRADES', 'amenityProvider': {'name': 'BrandedFare'}}, {'description': 'MILEAGE ACCRUAL', 'isChargeable': False, 'amenityType': 'BRANDED_FARES', 'amenityProvider': {'name': 'BrandedFare'}}]}]}]}], 'dictionaries': {'locations': {'ORD': {'cityCode': 'CHI', 'countryCode': 'US'}, 'PDX': {'cityCode': 'PDX', 'countryCode': 'US'}, 'SYR': {'cityCode': 'SYR', 'countryCode': 'US'}}, 'aircraft': {'320': 'AIRBUS A320', '739': 'BOEING 737-900'}, 'currencies': {'USD': 'US DOLLAR'}, 'carriers': {'UA': 'UNITED AIRLINES'}}}

carrier_code = data['data'][0]['itineraries'][0]['segments'][0]['carrierCode']
carrier = data['dictionaries']['carriers'][carrier_code]
print(carrier)




