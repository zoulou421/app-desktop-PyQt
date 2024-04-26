import os
import json

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


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


if __name__ == "__main__":
    m = Movie("Formationkilo movie")
    m._write_movies(["Moses movie1", "Court movie 1"])
