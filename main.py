#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
ORIGIN_CITY_IATA = "LON"
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get()
print(sheet_data)
for item in sheet_data:
    if item["iataCode"] == "":
        item["iataCode"] = flight_search.get_destination_code(item["city"])
    print(f"Sheet_data:\n{sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.new_data()
tomorrow = datetime.now() + timedelta(day=1)
six_month_from_now = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], from_time=tomorrow, to_time=six_month_from_now)

if flight.price < destination["lowestPrice"]:
    notification_manager = NotificationManager()
    notification_manager.send_sms(message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city} -- {flight.origin_airport} to {flight.destination_city} -- {flight.destination_airport}, from {flight.out_date} to {flight.return_date}")
