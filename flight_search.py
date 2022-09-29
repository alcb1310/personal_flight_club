from datetime import datetime, timedelta
import requests
from datetime import datetime
from environment import tequila_api_search_end_point, tequila_flight_search_api_key
# https://api.tequila.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.headers = {
            "apikey": tequila_flight_search_api_key,
            "Content-Type": "application/json"
        }
        self.params = {
            "fly_from": "city:UIO",
        }
        self.data = []

    def get_from_tequila_api(self):
        self.data.clear()
        response = requests.get(
            url=tequila_api_search_end_point, headers=self.headers, params=self.params)
        response.raise_for_status()
        self.data = response.json()["data"]

    def get_low_price(self, fly_to: str):
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        final_date = tomorrow + timedelta(days=90)

        self.params["fly_to"] = f"city:{fly_to}"
        self.params["dateFrom"]: tomorrow.strftime("%d/%m/%Y")
        self.params["dateTo"]: final_date.strftime("%d/%m/%Y")
        self.get_from_tequila_api()
        min_value = 999999999999999999999999999999999999
        lowest_record = {}
        for record in self.data:
            if record["price"] < min_value:
                min_value = record["price"]
                lowest_record = record

        print(lowest_record)


flight = FlightSearch()
# flight.get_from_tequila_api()
flight.get_low_price("LTN")
