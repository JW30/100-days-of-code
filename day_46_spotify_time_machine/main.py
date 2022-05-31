from bs4 import BeautifulSoup
import requests
from dateutil import parser
import datetime
import keys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ------------ Get the date from user on which the Spotify playlist will be based on. ------------
my_date = None
day_last_week = datetime.date.today() - datetime.timedelta(7)
date_accepted = False
while not date_accepted:
    try:
        my_date = parser.parse(input("Please input date: ")).date()
    except parser._parser.ParserError:
        print(f"Date was not recognized! Please try again.")
    else:
        if str(my_date) < "1958-08-04":
            answer = input(
                "Date too far in the past! Do you wish to reassign to the earliest possible date 1958-08-04? (y/n) ")
            my_date = datetime.date(year=1958, month=8, day=4)
        elif str(my_date) > str(day_last_week):
            answer = input("No data for given date yet! Do you wish to reassign to current hot 100? (y/n) ")
            my_date = day_last_week
        else:
            answer = input(f"Given date: {my_date}. Do you want to continue with this date? (y/n) ")
        if answer == "y":
            date_accepted = True


# ------------ Scrape for Billboard Hot 100 for the given date and get tracks + artists. ------------
billboard_url: str = "https://www.billboard.com/charts/hot-100/"
url: str = f"{billboard_url}{my_date}/"

response = requests.get(url=url)

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all(name="li", class_="o-chart-results-list__item")
song_names = [song.find("h3") for song in songs]
song_names = [song.getText().strip() for song in song_names if song]
artists = [song.find("span", {"class": ["c-title", "a-no-trucate"]}) for song in songs]
artists = [artist.getText().strip() for artist in artists if artist]


# ------------ Connect to Spotipy, search for songs in Spotify, create new playlist and add songs. ------------
scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope, client_id=keys.SPOTIFY_CLIENT_ID, client_secret=keys.SPOTIFY_CLIENT_SECRET,
                              redirect_uri="http://example.com"))

tracks = []
for i, song_name in enumerate(song_names):
    search_result = sp.search(q=f"{song_name} {artists[i]}", limit=1)['tracks']['items']
    if search_result:
        tracks.append(search_result[0]['id'])

playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=f"{my_date} Billboard Hot 100", public=False)

sp.playlist_add_items(playlist_id=playlist['id'], items=tracks)
