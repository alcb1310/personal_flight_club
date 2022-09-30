from pprint import pprint
import requests
from environment import sheety_api_url, sheety_api_bearer_token


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.headers = {
            "Authorization": f"Bearer {sheety_api_bearer_token}"
        }
        self.destination_data = []

    def get_all_data(self):
        self.destination_data.clear()
        response = requests.get(url=sheety_api_url, headers=self.headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]

    def update_prices(self, row_index: int, price: int):
        update_url = f"{sheety_api_url}/{row_index}"
        data = {
            "price": {
                "lowestPrice": price
            }
        }
        response = requests.put(
            url=update_url, headers=self.headers, json=data)
        response.raise_for_status()
