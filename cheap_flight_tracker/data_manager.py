from tarfile import data_filter

import requests

SHEETY_TOKEN = "Bearer ghah^((*^DGCHDF61934764agsh&^GH78"
SHEETY_ENDPOINT = "https://api.sheety.co/94449b7ca8b5b8936e9cc0192b70f8f5/flightDeals/sheet1"
SHEETY_HEADER = {"AUTHORIZATION": SHEETY_TOKEN}

def destinations(endpoint, header, sheet):
    response = requests.get(url=endpoint, headers=header)
    data = response.json()[sheet]
    return data
    # destination_list = []
    # for x in range(len(data)):
    #     destination_list.append(data[x]["city"])
    # return destination_list






# def input_cities():
#     city = input("where do you want to travel to?")



