from PySide6 import QtWidgets


class App(QtWidgets.QWidget):
    def __init__(self):
        # QtWidgets.QWidget.__init__()
        super().__init__()
        self.setWindowTitle("Currency Converter")


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec()