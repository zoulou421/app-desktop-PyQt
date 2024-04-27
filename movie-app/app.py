from PySide6 import QtWidgets,QtCore
from movie import get_all_movies


class App(QtWidgets.QWidget):  # QWidget represent our window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome on movie app")
        self.setup_ui()
        self.populate_movies_v2()

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
            lw_item=QtWidgets.QListWidgetItem(movie.movie_title)
            lw_item.setData(QtCore.Qt.UserRole,movie)
            self.lw_movies.addItem(lw_item)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()
