from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import base64

with open("tupac-shakur.jpeg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

date = input("Which year do you want to travel to? Type your answer in this format: YYYY-MM-DD ")

billboard_url = 'https://www.billboard.com/charts/hot-100/'

request_endpoint = f'https://www.billboard.com/charts/hot-100/{date}'
print(request_endpoint)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
}
response = requests.get(url=request_endpoint, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

top_100_songs = soup.find_all("h3", class_="a-no-trucate")
top_songs_list = []
for song in top_100_songs:
    top_songs_list.append(song.getText(strip=True))

print(top_songs_list)
spotify_ID = '85f481c209e8481eacf5221746cfb3be'
spotify_Secret = 'e776d83a39384a099abd14ada4b85250'

scope = "user-library-read playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri='https://example.com/callback',
                                               scope=scope))

playlist_name = f'Playlist from {date}'
new_playlist = sp.user_playlist_create(user=os.getenv('SPOTIFY_USER_ID'), name=playlist_name, public=False)
new_playlist_id = new_playlist['id']

top_songs_uri = []
for songs in top_songs_list:
    result = sp.search(q=songs, type="track")
    track_uri = result['tracks']['items'][0]['uri']
    top_songs_uri.append(track_uri)

sp.playlist_add_items(playlist_id=new_playlist_id, items=top_songs_uri)

