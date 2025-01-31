import requests
import os
from dotenv import load_dotenv


load_dotenv()

SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_HEADER = {"AUTHORIZATION": SHEETY_TOKEN}

class DataManager:

    def __init__(self):
        self.destination_data = {}
    ''' this function  sends a request to sheety and returns the sheet data to the 
    dictionary destination_data
    
    ex: [{'city': 'Houston', 'iataCode': , 'pricePoint': 150, 'id': 2}, 
         {'city': 'Minneapolis', 'iataCode': , 'pricePoint': 150, 'id': 3}]
    '''
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
        data = response.json()
        self.destination_data = data['destinations']
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "destination": {
                    "iataCode": city['iataCode']
                }
            }
            requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, headers=SHEETY_HEADER)

