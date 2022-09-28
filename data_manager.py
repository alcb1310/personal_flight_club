import requests
from environment import sheety_api_url, sheety_api_bearer_token


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.headers = {
            "Authorization": f"Bearer {sheety_api_bearer_token}"
        }
        self.prices = []

    def get_all_data(self):
        self.prices.clear()
        response = requests.get(url=sheety_api_url, headers=self.headers)
        response.raise_for_status()

        self.prices = response.json()["prices"]
