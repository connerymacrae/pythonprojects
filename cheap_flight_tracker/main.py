import requests

# TODO: create list of cities to track and add to spreadsheet
# TODO: create low price point to track
# TODO: create function to read from spreadsheet
# TODO: create function that compiles flight prices to each destination for a given period of time
# TODO: compare flight prices against spreadsheet
# TODO: If flight prices are below low price listed in spreadsheet, send notification via twilio



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

AMADEUS_IATA_CODE_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations"

location = {
    "subType": "AIRPORT",
    "keyword": "london",
    "countryCode": "GB"
}
response = requests.get(url=AMADEUS_IATA_CODE_ENDPOINT, params=location, headers=AMADEUS_HEADER)

data = response.json()

print(data)



SHEETY_TOKEN = "Bearer ghah^((*^DGCHDF61934764agsh&^GH78"
SHEETY_ENDPOINT = "https://api.sheety.co/94449b7ca8b5b8936e9cc0192b70f8f5/flightDeals/sheet1"

# destination = input("Where do you want to travel to?")
# price_point = float(input("what is your max price?"))

