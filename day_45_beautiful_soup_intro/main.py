from bs4 import BeautifulSoup
import requests

URL1: str = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&ref_=adv_prv"
URL2: str = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&view=advanced"


def get_movies(url) -> list:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    movies: list = soup.find_all(name="h3", class_="lister-item-header")
    movies: list = [movie.find("span").getText() + " " + movie.find("a").getText() for movie in movies]
    return movies


top_100_movies: list = get_movies(URL1) + get_movies(URL2)

with open(file="top-100-movies.txt", mode="w") as f:
    for m in top_100_movies:
        f.write(m + "\n")
