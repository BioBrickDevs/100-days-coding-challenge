import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")

all_results = soup.findAll(name="h3", class_="title")

all_results = [data.getText() for data in all_results]

all_results = all_results[::-1]

with open("file.txt", "w") as file:
    for results in all_results:
        file.writelines(f"{results}\n")
