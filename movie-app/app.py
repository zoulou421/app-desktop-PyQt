from PySide6 import QtWidgets, QtCore
from movie import get_all_movies

from movie import Movie


class App(QtWidgets.QWidget):  # QWidget represent our window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome on movie app")
        self.setup_ui()
        self.populate_movies_v2()
        self.setup_connections()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Add a movie")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_removeMovies = QtWidgets.QPushButton("Remove movie(s)")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)

    def populate_movies(self):
        movies = get_all_movies()
        for movie in movies:
            self.lw_movies.addItem(movie.movie_title)

    def populate_movies_v2(self):
        movies = get_all_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.movie_title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_Movie)
        self.btn_removeMovies.clicked.connect(self.remove_Movie)
        self.le_movieTitle.returnPressed.connect(self.add_Movie)

    def add_Movie(self):
        # retrieve text in linedit
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False
        # create a Movie instance
        my_movie = Movie(movie_title)
        # add movie in json file
        result = my_movie.add_to_movies()
        if result:
            lw_item = QtWidgets.QListWidgetItem(my_movie.movie_title)
            lw_item.setData(QtCore.Qt.UserRole, my_movie)
            self.lw_movies.addItem(lw_item)
        self.le_movieTitle.setText("")



    def remove_Movie(self):
        print("remove movie or movies")


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()
