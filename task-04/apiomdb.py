import os
import requests

def get_movie_info(movieTitle):
    url = 'http://www.omdbapi.com/?i=tt3896198&apikey=ac4b246d'
    api_key = os.getenv('ac4b246d')
    data = {'apikey': api_key, 't': movieTitle}
    response = requests.get(url, data)

    if response.status_code != 200:
        return None

    data = response.json()

    movie_info = {"title": data["Title"], "year": data["Year"], "plot": data["Plot"],
                  "actors": data["Actors"], "ratings": data["Ratings"],
                  "imdb_rating": data["imdbRating"], "poster": data["Poster"]}

    return movie_info