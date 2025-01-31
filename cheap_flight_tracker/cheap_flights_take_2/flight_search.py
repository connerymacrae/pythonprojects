import requests
import os
from dotenv import load_dotenv
from datetime import date, datetime, timedelta


load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:

    def __init__(self):
        self.api_key = os.getenv('AMADEUS_API_KEY')
        self.api_secret = os.getenv('AMADEUS_API_SECRET')
        self.token = self.get_new_token()

    def get_new_token(self):
        ama_auth_token_header = {
            "content-type": "application/x-www-form-urlencoded"
        }

        ama_auth_body = f"grant_type=client_credentials&client_id={self.api_key}&client_secret={self.api_secret}"

        auth_response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            data=ama_auth_body,
            headers=ama_auth_token_header
        )

        auth_token = auth_response.json()['access_token']
        return {"authorization": f"Bearer {auth_token}"}

    ''' get request from Amadeus takes city name from sheet_data row and returns the IATA code'''
    def get_destination_code(self, city):
        location = {
            "keyword": city,
            "max": 1,
            "include": "AIRPORTS"
        }
        amadeus_response = requests.get(url=IATA_ENDPOINT, params=location, headers=self.token)
        data = amadeus_response.json()
        iata_code = data["data"][0]["iataCode"]
        return iata_code

    ''' 1: for every day in six month range, find the cheapest flight from origin to destination'''
    def check_flights(self, origin_city_code, destination_city_code, price_point):
        flights = []
        six_month_range = [(date.today() + timedelta(days=(num + 30))).strftime("%Y-%m-%d") for num in range(24)]
        for day in six_month_range:
            query = {
                "originLocationCode": origin_city_code,
                "destinationLocationCode": destination_city_code,
                "departureDate": day,
                "adults": 1,
                "travelClass": "ECONOMY",
                "currencyCode": "USD",
                "excludedAirlineCodes": "F9",
                "maxPrice": price_point,
                "max": 1
            }
            response = requests.get(url=FLIGHT_ENDPOINT, params=query, headers=self.token)
            data = response.json()
            if "errors" in data or "warnings" in data:
                continue
            elif data["meta"]["count"] > 0:
                dept_date = day
                itinerary = f"{origin_city_code} - {destination_city_code}"
                price = data['data'][0]['price']['total']
                airline = self.get_airline(data)
                form_data = {"dept_date": dept_date, "itinerary": itinerary, "price": float(price), "carrier":airline}
                flights.append(form_data)
        return flights

    def get_airline(self, flight_info):
        carrier_code = flight_info['data'][0]['itineraries'][0]['segments'][0]['carrierCode']
        return flight_info['dictionaries']['carriers'][carrier_code]

    def check_lowest(self, flight_list):
        cheapest_flight = flight_list[0]
        for flight in flight_list:
            if flight['dept_date']> cheapest_flight['dept_date'] and flight['price']<cheapest_flight['price']:
                cheapest_flight = flight
        return cheapest_flight

