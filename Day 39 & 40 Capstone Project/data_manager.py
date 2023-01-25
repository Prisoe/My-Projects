import requests
from flight_search import FlightSearch

search = FlightSearch()


class DataManager:
    #This class is responsible for talking to the Google Sheet.


    def get_data(self):
        self.sheety_endpoint = "https://api.sheety.co/ebbf7d484406c0881977170c10e6d0cf/copyOfFlightDeals/prices"
        response = requests.get(url=self.sheety_endpoint)
        response.raise_for_status()
        self.sheet_data = response.json()["prices"]
        return self.sheet_data

    def update_data(self):
        for data in range(len(self.sheet_data)):
            city = self.sheet_data[data]["city"]

            iata_code = search.iota_location(city)
            print(iata_code)
            sheety_params = {
                "price": {
                    "iataCode": iata_code
                }
            }
            put_response = requests.put(url=f"{self.sheety_endpoint}/{self.sheet_data[data]['id']}", json=sheety_params)
            put_response.raise_for_status()



    def get_user(self):
        users_endpoint = "https://api.sheety.co/ebbf7d484406c0881977170c10e6d0cf/copyOfFlightDeals/users"
        response = requests.get(url=users_endpoint)
        response.raise_for_status()
        data = response.json()
        self.users = data["users"]
        return self.users
