import requests

SHEETY_TOKEN = "Bearer ghah^((*^DGCHDF61934764agsh&^GH78"
SHEETY_ENDPOINT = "https://api.sheety.co/94449b7ca8b5b8936e9cc0192b70f8f5/flightDeals/sheet1"
SHEETY_HEADER = {"AUTHORIZATION": SHEETY_TOKEN}

def destinations(endpoint, header, sheet):
    response = requests.get(url=endpoint, headers=header)
    data = response.json()[sheet]
    return [[data[x]["city"], data[x]["iataCode"], data[x]['maximumPrice']] for x in range(len(data))]


def add_city(ama_endpoint, ama_header, sh_endpoint, sh_header):
    city = input("Where to do you want to visit?: ").title()
    cost = input("What's the max price you want to pay, one way?: ")
    location = {
        "keyword": city,
        "max": 1,
        "include": "AIRPORTS"
    }
    amadeus_response = requests.get(url=ama_endpoint, params=location, headers=ama_header)
    data = amadeus_response.json()
    iata_code = data["data"][0]["iataCode"]
    sheety_add_row = {
        "sheet1": {
            "city": city,
            "iataCode": iata_code,
            "maximumPrice": cost
        }
    }
    requests.post(url=f"{sh_endpoint}", json=sheety_add_row, headers=sh_header)
    print(f"{city}({iata_code}) for max price ${cost} was added successfully")






