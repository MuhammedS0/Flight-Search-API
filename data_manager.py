import requests
from pprint import pprint
SHEETY_GET_ENDPOINT = "https://api.sheety.co/c02637e16af3bdec611e22b68defce26/flightDeals/prices"
class DataManager:
    def __init__(self):
       self.destination_data = {}

    #This class is responsible for talking to the Google Sheet.

    def get(self):
        response = requests.get(url=SHEETY_GET_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def new_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_GET_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)