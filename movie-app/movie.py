class Movie:
    def __init__(self, movie_title):
        self.movie_title = movie_title.title()

    def __str__(self):
        return self.movie_title


if __name__ == "__main__":
    m = Movie("Jean Claude Vandamme")
    print(m)

