"""API movies class"""

import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

"""  movies=[]
        my_movies_title=json.load(f)
    for my_movies_title in my_movies_title:
        movies.append(Movie(my_movies_title))
"""


def get_all_movies():
    with open(DATA_FILE, "r") as f:
        my_movies_title = json.load(f)
    movies = [Movie(my_movie_title) for my_movie_title in my_movies_title]
    return movies


class Movie:
    def __init__(self, movie_title):
        self.movie_title = movie_title.title()

    def __str__(self):
        return self.movie_title

    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, list_movies):
        with open(DATA_FILE, "w") as f:
            json.dump(list_movies, f, indent=4)

    def add_to_movies(self):
        # retrieve movies list
        list_movies = self._get_movies()
        # check if movie already in a list or not
        if self.movie_title not in list_movies:
            list_movies.append(self.movie_title)
            self._write_movies(list_movies)
            return True
        else:
            logging.warning(f"movie {self.movie_title} already recorded")
            return False

    def remove_from_movies(self):
        list_movies = self._get_movies()
        if self.movie_title in list_movies:
            list_movies.remove(self.movie_title)
            self._write_movies(list_movies)


if __name__ == "__main__":
    m = Movie("Formationkilo movie")
    m.add_to_movies()
    m1 = Movie("Jean claude vandamme")
    m1.add_to_movies()

    # print(m.remove_from_movies())
    movie = get_all_movies()
    print(movie)
