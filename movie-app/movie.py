import os
import json
import logging

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



if __name__ == "__main__":
    m = Movie("Formationkilo movie")
    m.add_to_movies()
    print(m.add_to_movies())