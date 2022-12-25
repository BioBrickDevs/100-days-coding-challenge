import requests
import datetime
import dotenv
import os

dotenv.load_dotenv()

info = """This code is not a working project to do any usefull. Only how to create user account, 
        create a new graph and how to update the graph pixels. How to delete and how to update."""



profile_url = "https://pixe.la/@biobrick"


TOKEN = os.getenv("TOKEN")


USER_NAME = "biobrick"
parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post("https://pixe.la/v1/users", json = parameters)

# response.raise_for_status()
# print(response.text)
graph_enpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_enpoint, json=graph_config, headers=headers )
# print(response.text)

date = datetime.datetime.now()
date = date.strftime("%Y%m%d")
print(date)
insert_pixel_config = {
    "date": date,
    "quantity": "100",
}

insert_pixel_endpoint = graph_enpoint + "/graph1"

# response = requests.post(url=insert_pixel_endpoint, json=insert_pixel_config, headers=headers)
# print(response.text)

update_config = {
    "quantity": "50",
}

# response = requests.put(, json=update_config, headers = headers)
# print(response.text)

response = requests.delete(
    pixela_endpoint + f"/{USER_NAME}/graphs/graph1/{date}", headers=headers)
print(response.text)
