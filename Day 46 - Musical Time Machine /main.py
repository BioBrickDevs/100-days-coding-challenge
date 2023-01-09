import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import dotenv
import os
dotenv.load_dotenv()


answer = input("What day do you want to travel?(format dd/mm/yyyy): ")
year = answer.split("/")[2]
month = answer.split("/")[1]
day = answer.split("/")[0]

Client_ID = os.environ.get("Client_ID")
Client_Secret = os.environ.get("Client_Secret")

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback/",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"))

user_id = spotify.current_user()["id"]
print("Working")
response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/")
soup = bs4.BeautifulSoup(response.text, "html.parser")


song_name_container = soup.select(selector="h3#title-of-a-story")
counter = 0
song_urls = []
for index in range(6, len(song_name_container), 4):
    song_name = song_name_container[index].getText().strip()
    try:
        result = spotify.search(
            q=f"track:{song_name} year:{year}", type="track")
        url = result["tracks"]["items"][0]["uri"]
        song_urls.append(url)
    except IndexError:
        print("song does not exist on spotify")
    if counter == 100:
        break

playlist = spotify.user_playlist_create(
    user=user_id, name=f"{answer} Billboard 100", public=False)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_urls)
