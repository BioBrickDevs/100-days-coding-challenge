import requests
import os

# Raahe longitude and latitude
print(os.environ)
longitude = 24.573818
latitude = 64.690720

text_belt_key = os.environ.get("TEXT_BELT_API_KEY")
api_call = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
open_weather_api_key = os.environ.get("OPEN_WEATHER_API_KEY")

end_point = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": open_weather_api_key,
    "exclude": "daily,minutely,current",
    "units": "metric"
}


response = requests.get(end_point, params=parameters)
response.raise_for_status()
print("----------------")

weather_data = response.json()
raining = False
snowing = False

for num in range(0, 15):
    statuscode = weather_data["hourly"][num]["weather"][0]["id"]
    if statuscode < 700 and statuscode >= 600:
        snowing = True
        viesti = "Pattijoella sataa tänään lunta. Terveisin Jari."
    if statuscode < 600 and statuscode >= 500:
        raining = True
        viesti = "Pattijoella sataa tänään vettä. Terveisin Jari."

    numero = "+358405613608"
if raining or snowing:

    resp = requests.post('https://textbelt.com/text', {
        'phone': numero,
        'message': viesti,
        'key': text_belt_key,
    })
print(resp.json())


