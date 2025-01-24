import requests


class FlightSearch:

    def get_destination_code(self, city):
        code = "Testing"
        return code

    # location = {
    #     "keyword": city,
    #     "max": 1,
    #     "include": "AIRPORTS"
    # }
    # amadeus_response = requests.get(url=ama_endpoint, params=location, headers=ama_header)
    # data = amadeus_response.json()
    # iata_code = data["data"][0]["iataCode"]