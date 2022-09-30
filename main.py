# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from environment import *
from twilio.rest import Client
from datetime import datetime, timedelta

data = DataManager()
data.get_all_data()

# print(type(date_time_obj))

flight_search_data = FlightSearch()

for route in data.destination_data:
    if "iataCode" in route:
        response = flight_search_data.get_low_price(
            fly_to=route["iataCode"], low_price=route["lowestPrice"])
        if "price" in response:
            date_str = response['local_departure']
            index = date_str.index("T")
            date_only_str = date_str[:index]

            departure_date = datetime.strptime(date_only_str, "%Y-%m-%d")
            return_date = departure_date + timedelta(days=response["nightsInDest"])
            
            # break
            
            data.update_prices(row_index=route["id"], price=response["price"])
            client = Client(twilio_account_sid, twilio_auth_token)
            
            body_msg = f"Low price alert! Only ${response['price']} from {response['cityFrom']}-{response['cityCodeFrom']} to {response['cityTo']}-{response['cityCodeTo']} from {departure_date.strftime('%Y/%m/%d')} to {return_date.strftime('%Y/%m/%d')}"
            
            message = client.messages.create(
                from_=twilio_phone_number,
                to="+593997014902",
                body = body_msg
            )