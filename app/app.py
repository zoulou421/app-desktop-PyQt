from PySide6 import QtWidgets


class App(QtWidgets.QWidget):
    def __init__(self):
        # QtWidgets.QWidget.__init__()
        super().__init__()
        self.setWindowTitle("Currency Converter")
        self.setup_ui()

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.ccb_currency_from = QtWidgets.QComboBox()
        self.spn_amount = QtWidgets.QSpinBox()
        self.ccb_currency_to = QtWidgets.QComboBox()
        self.spn_amount_converted = QtWidgets.QSpinBox()
        self.btn_inverse = QtWidgets.QPushButton("Inverse Currency")

        self.layout.addWidget(self.ccb_currency_from)
        self.layout.addWidget(self.spn_amount)
        self.layout.addWidget(self.ccb_currency_to)
        self.layout.addWidget(self.spn_amount_converted)
        self.layout.addWidget(self.btn_inverse)


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec()
