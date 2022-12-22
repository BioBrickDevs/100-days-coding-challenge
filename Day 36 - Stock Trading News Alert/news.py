
import requests
import os

def get_latest_news(querry):

    message = ""
    news_querry = querry
    news_api_key = os.environ.get("news_api_key")

    news_parameters = {
        "apiKey": news_api_key,
        "searchin": "title",
        "q": news_querry
    }

    response = requests.get(
        "https://newsapi.org/v2/everything", params=news_parameters)

    result = response.json()
    for index in range(0, 3):
        message += "Title: " + result["articles"][index]["title"] + "<br>"
        message += "Content: " + \
            result["articles"][index]["description"] + "<br>"
        message += "Url:" + result["articles"][index]["url"]
        message += "<br><br>"

    return message
