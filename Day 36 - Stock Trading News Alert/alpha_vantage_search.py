import requests
import json
import dotenv
import os
# simple command line program for searching different symbols on alphavantage
dotenv.load_dotenv()
alpha_vantage_key = os.environ.get("alpha_vantage_key")


def on_going_search():
    search_keywords = input("Anna hakusana: ")
    parameters = {
        "apikey": alpha_vantage_key,
        "function": "SYMBOL_SEARCH",
        "keywords": search_keywords

    }

    response = requests.get(
        "https://www.alphavantage.co/query", params=parameters)

    response.raise_for_status()
    json_data = response.json()
    json_data = json.dumps(json_data, indent=4)
    print(json_data)

    print(response)

    on_going_search()
    
on_going_search()
