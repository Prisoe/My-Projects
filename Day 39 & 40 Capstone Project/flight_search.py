import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from flight_data import FlightData
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def iota_location(self, city):
        self.city = city
        flight_serach_endpoint = "https://tequila-api.kiwi.com/locations/query"
        headers = {
            "apikey": "VscB7Fryfmn_k5Yv3Mnt-imZ4_q6mv63"
        }
        query = {
            "term": self.city,
            "location_types": "city"
        }
        self.response = requests.get(url=flight_serach_endpoint, headers=headers, params=query)
        self.response.raise_for_status()
        self.data = self.response.json()
        code = self.data["locations"][0]["code"]
        # self.iata_code = self.data["locations"][0]["iataCode"]
        return code


    def search_flights(self, iata_code, city_code):
        search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        headers = {
            "apikey": "h7xShOSfSgCYsK5mKmOCXujAcLbS7VjI"
        }
        today = datetime.now()
        date = today.strftime("%d/%m/%Y")
        date_6_months = today + timedelta(days=(6*30))
        query = {
            "fly_from": city_code,
            "fly_to": iata_code,
            "date_from": date,
            "date_to": date_6_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "CAD"
        }

        response = requests.get(url=search_endpoint, headers=headers, params=query)
        response.raise_for_status()
        data = response.json()["data"][0]

        flight_data = FlightData(
            price = data["price"],
            departure_airport_code=data["cityCodeFrom"],
            departure_city=data["cityFrom"],
            arrival_airport_code=data["cityCodeTo"],
            arrival_city=data["cityTo"],
            travel_date=data["local_arrival"].split("T")[0],
            return_date=data["local_arrival"].split("T")[0],
            booking_link=data["deep_link"]
        )

        print(f"{flight_data.a_city}: ${flight_data.price} Book Here Now: {flight_data.booking_link}")
        return flight_data



