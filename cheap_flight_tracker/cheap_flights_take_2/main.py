from select import select
from datetime import datetime
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager




data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

ORIGIN_CITY_IATA = 'SYR'

# # UPDATE AIRPORT CODES IN GOOGLE SHEET

# for row in sheet_data:
#     if row['iataCode'] == "":
#         row['iataCode'] = flight_search.get_destination_code(row['city'])
#
# '''updates sheet_data'''
# data_manager.destination_data = sheet_data
# '''uses put request to insert IATA code into google sheet'''
# data_manager.update_destination_data()



# SEARCH FOR FLIGHTS
select_cities = []
for city in sheet_data:
    flights = flight_search.check_flights(ORIGIN_CITY_IATA, city['iataCode'], city['pricePoint'])
    cheapest_flight = flight_search.check_lowest(flights)
    select_cities.append(cheapest_flight)



notification_manager = NotificationManager(sheet_data, select_cities)
notification_manager.create_message()

