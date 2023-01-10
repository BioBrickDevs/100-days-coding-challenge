import datetime
import requests
from flight_data import FlightData
import dotenv
import os
dotenv.load_dotenv()
KIVI_API_KEY = os.environ.get("KIVI_API_KEY")

now = datetime.datetime.now()
day = datetime.timedelta(days=1)
six_months = datetime.timedelta(days=180)

tomorrow = now + day
after_six_moths = now + six_months


class FlightSearch:

    def get_IATA_code_for_city(city_name):
        term_search = city_name
        header = {
            "apikey": KIVI_API_KEY,
        }
        parameters = {
            "term": term_search,
        }
        response = requests.get(
            "https://api.tequila.kiwi.com/locations/query", headers=header,
            params=parameters)
        try:
            IATA_code = response.json()["locations"][0]["code"]
        except:
            IATA_code = "Error happened!"
        return IATA_code

    def get_cheap_flight_from_to(fro, to):
        header = {
            "apikey": KIVI_API_KEY,
        }

        parameters = {
            "fly_from": f"city:{fro}",
            "fly_to": to,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": after_six_moths.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "EUR",
            "max_stopovers": 7,
            "one_for_city": 1,
            # "only_weekends": "true",
            # "ret_fly_days": "0",
            # "ret_fly_days_type": "arrival",


        }

        data = FlightData
        response = requests.get(
            "https://api.tequila.kiwi.com/v2/search", headers=header, params=parameters)
        response.raise_for_status()
        try:
            data.ticket_price = response.json()["data"][0]["price"]
            data.link_to_tickets = response.json()["data"][0]["deep_link"]
        except:
            data.ticket_price = "no price"

        return data
