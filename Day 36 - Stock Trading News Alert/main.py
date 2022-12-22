import requests
import news
import send_message
import dotenv
import os

dotenv.load_dotenv()


STOCK = "MRNA"
COMPANY_NAME = "Moderna Inc"


alpha_vantage_key = os.environ.get("alpha_vantage_key")

parameters = {
    "apikey": alpha_vantage_key,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,

}


response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()
data = dict(list(data["Time Series (Daily)"].items())[:2])

data = [float(value["4. close"]) for key, value in data.items()]

difference = abs(data[1] - data[0])
average = (data[1] + data[0]) / 2

difference_percentage = difference / data[1] * 100


if difference_percentage > 3:
    # if change over 5 % send message

    message = news.get_latest_news(COMPANY_NAME)
    stats = ""
    round(difference_percentage, 2)
    round(difference, 2)
    if data[0] >= data[1]:
        stats += "+" + str(round(difference_percentage, 2)) + \
            " %, " + str(round(difference, 2)) + " $" + "<br>"
    else:
        stats += "+" + str(round(difference_percentage, 2)) + \
            " %, " + str(round(difference, 2)) + " $" + "<br>"
    message = stats + message
    send_message.send_message(message)
