import requests
from twilio.rest import Client
from datetime import datetime, timedelta
from notification_manager import NotificationManager
notification_manager = NotificationManager()
account_sid = "AC47cefb54da23e053f6131749d8e567ae"
auth_token = "764edbf047cafd5a70adf53756b8be77"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, city_name):
        headers = {"apikey": "0t0Lh5yrMjGTSr-18GkuuWo_LyreSx0r"}
        parameters = {"term": city_name, "location_types": "city"}
        response = requests.get(url="https://tequila-api.kiwi.com/locations/query", headers=headers, params=parameters)
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def find_flights(self, city):
        headers =  {"apikey": "0t0Lh5yrMjGTSr-18GkuuWo_LyreSx0r"}
        today = datetime.now()
        later_date = today + timedelta(days=180)
        parameters = {"fly_from": "LAX",
                      "fly_to": city["iataCode"],
                      "date_from": today.strftime("%d/%m/%Y"),
                      "date_to": later_date.strftime("%d/%m/%Y"),
                      "one_for_city": 1,
                      "curr": "USD"

                      }
        response = requests.get(url="https://tequila-api.kiwi.com/v2/search", headers=headers, params=parameters)
        results = response.json()
        try:
            results["data"][0]
        except IndexError:
            print(f'There are no flights for {city["iataCode"]}')
            return None

        print(f'{results["data"][0]["cityTo"]}: ${results["data"][0]["price"]}')

        if results["data"][0]["price"] < city["lowestPrice"]:
            notification_manager.send_message(message=f'Low price right now! Only ${results["data"][0]["price"]} to fly from {results["data"][0]["cityCodeFrom"]} to {results["data"][0]["cityTo"]}.')


