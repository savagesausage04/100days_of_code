#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_data()


empty_string = ""
if sheet_data[0]["iataCode"] == empty_string:
    flight_search = FlightSearch()
    for city in sheet_data:
        city["iataCode"] = flight_search.get_iata_code(city["city"])
        flight_search.find_flights(city)


    data_manager.sheet_data = sheet_data
    data_manager.update_sheet_codes()




