from PySide6 import QtWidgets


class App(QtWidgets.QWidget):  # QWidget represent our window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome on movie app")
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle=QtWidgets.QLineEdit()
        self.btn_addMovie=QtWidgets.QPushButton("Add a movie")
        self.lw_movies=QtWidgets.QListWidget()
        self.btn_removeMovies=QtWidgets.QPushButton("Remove movie(s)")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()
