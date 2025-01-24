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

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
        data = response.json()
        self.destination_data = data['destinations']
        return self.destination_data

# response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
# data = response.json()
# # print(data)
#
# for x in range(len(data)):
#      update = {'destinations': {'iataCode': f"{data['destinations'][x]['iataCode']}"}}
#      response = requests.put(url=f"{SHEETY_ENDPOINT}/{data['destinations'][x]['id']}", json=update, headers=SHEETY_HEADER)
#
