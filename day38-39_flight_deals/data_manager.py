import requests
from pprint import pprint
sheet_endpoint = "https://api.sheety.co/dfcd9751d33f709757494c69f0fca73b/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        self.response = requests.get(sheet_endpoint)
        self.response.raise_for_status()
        self.sheet_data = self.response.json()["prices"]
        return self.sheet_data

    def update_sheet_codes(self):
        for city in self.sheet_data:
            replaced_data = {"price": {"iataCode": city["iataCode"]
            }
                             }
            response = requests.put(url=f'{sheet_endpoint}/{city["id"]}', json=replaced_data)
            #print(response.text)

