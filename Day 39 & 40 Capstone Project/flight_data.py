class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price, departure_airport_code, departure_city, arrival_airport_code, arrival_city,
                 travel_date, return_date, booking_link):
        self.price = price
        self.d_airport = departure_airport_code
        self.d_city = departure_city
        self.a_airport = arrival_airport_code
        self.a_city = arrival_city
        self.travel_date = travel_date
        self.return_date = return_date
        self.booking_link = booking_link
