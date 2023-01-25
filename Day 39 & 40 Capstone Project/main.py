#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import pyshorteners

departure_city_code = "yto"

flight_search = FlightSearch()
data_manager = DataManager()
notify = NotificationManager()
# get all the cities from the DOcs

sheet_data = data_manager.get_data()

if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flight_search.iota_location(data["city"])
    # print(sheet_data)

    #Update the data
    sheet_data = data_manager.update_data()

# print(sheet_data)

for data in sheet_data:
    # print(sheet_data)
    iata_code = data["iataCode"]
    flight = flight_search.search_flights(iata_code, departure_city_code.upper())


    long_url = flight.booking_link
    tiny = pyshorteners.Shortener()
    short_url = tiny.tinyurl.short(long_url)
    
    try:
        if flight.price < data["lowestPrice"]:
            notify.send_message(
                message=f"Low PRICE ALERT! ${flight.price} to {flight.a_city}, date-{flight.travel_date}\n link:{short_url}"
            )

        if flight.price < data["lowestPrice"]:
            users = data_manager.get_user()
            user_email = [row["email"] for row in users]
            name = [row["firstName"] for row in users]
            message = f"Low Price Alert \n\nLow PRICE ALERT! ${flight.price} to {flight.a_city}, date-{flight.travel_date}\n link:{short_url}"
            notify.send_email(user_email, message)


    except flight == None:
        continue





