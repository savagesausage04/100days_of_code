from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

CLIENT_ID = "8ee95dce257f4ae1b01f95fb3e3f1a3a"
CLIENT_SECRET = "a8d3dce18bfd4c768da5ad13c1834fd6"
REDIRECT_URI = "https://example.com/callback"

date_input = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date_input}/"
response = requests.get(URL)
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

rankings = soup.find_all(name="h3", class_="a-no-trucate")
song_list = []
for song in rankings:
    song_title = song.getText()
    replace_one = song_title.replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t", "")
    # there's this weird stuff before and after the song title, using replace to just get rid of them
    replace_two = replace_one.replace("\t\t\n\t\n", "")
    song_list.append(replace_two)

#print(song_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

year = date_input.split("-")[0]

uri_list = []
for song in song_list:
    search_result = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = search_result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skip.")

#print(uri_list)

playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)