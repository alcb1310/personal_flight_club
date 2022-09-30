from dotenv_config import Config
"""
Reads the environment variables and places them in python variables which we can use later on
"""
config = Config('.env')

sheety_api_url = config('SHEETY_API_END_POINT')
sheety_api_bearer_token = config('SHEETY_API_BEARER_TOKEN')
tequila_flight_search_api_key = config('TEQUILA_FLIGHT_SEARCH_API_KEY')
tequila_api_search_end_point = config('TEQUILA_API_SEARCH_END_POINT')
twilio_account_sid = config('TWILIO_ACCOUNT_SID')
twilio_auth_token = config('TWILIO_AUTH_TOKEN')
twilio_phone_number = config('TWILIO_PHONE_NUMBER')
