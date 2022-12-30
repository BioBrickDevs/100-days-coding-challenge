import requests

name = "Jari"
parameters = {
    "name": name
}
agify_response = requests.get("https://api.agify.io/", params=parameters)
agify_data = agify_response.json()
age_prediction = agify_data["age"]
print(age_prediction)
