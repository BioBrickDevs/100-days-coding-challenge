import requests

name = "Jari"
parameters = {
    "name": name
}
gender_response = requests.get("https://api.genderize.io", params=parameters)
gender_data = gender_response.json()
sexuality_prediction = gender_data["gender"]
print(sexuality_prediction)
