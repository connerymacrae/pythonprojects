from flight_search import FlightSearch
from pprint import pprint
from data_manager import DataManager



data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# sheet_data = [{'city': 'Houston', 'iataCode': '', 'pricePoint': 150, 'id': 2},
#               {'city': 'Minneapolis', 'iataCode': '', 'pricePoint': 150, 'id': 3},
#               {'city': 'New York', 'iataCode': '', 'pricePoint': 100, 'id': 4},
#               {'city': 'San Francisco', 'iataCode': '', 'pricePoint': 200, 'id': 5},
#               {'city': 'Chicago', 'iataCode': '', 'pricePoint': 110, 'id': 6}]

for row in sheet_data:
    if row["iataCode"] == "":
       flight_search = FlightSearch()
       row['iataCode'] = flight_search.get_destination_code(row['city'])
    else:
        continue


