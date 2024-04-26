from PySide6 import QtWidgets
import currency_converter

"""
>>> import currency_converter
>>> c=currency_converter.CurrencyConverter()
>>> c.currencies
"""


class App(QtWidgets.QWidget):
    def __init__(self):
        # QtWidgets.QWidget.__init__()
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Currency Converter")
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()

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

    def set_default_values(self):
        # self.ccb_currency_from.addItems(["1", "2", "3"])
        self.ccb_currency_from.addItems(sorted(list(self.c.currencies)))
        self.ccb_currency_to.addItems(sorted(list(self.c.currencies)))

        self.ccb_currency_from.setCurrentText("EUR")
        self.ccb_currency_to.setCurrentText("EUR")

        self.spn_amount.setRange(1, 1000000000)
        self.spn_amount_converted.setRange(1, 1000000000)

        self.spn_amount.setValue(100)
        self.spn_amount_converted.setValue(100)

    def setup_connections(self):
        self.ccb_currency_from.activated.connect(self.compute)
        self.ccb_currency_to.activated.connect(self.compute)

        self.spn_amount.valueChanged.connect(self.compute)
        self.spn_amount_converted.valueChanged.connect(self.compute)

        self.btn_inverse.clicked.connect(self.inverse_currency)

    def compute(self):
        print("compute")

    def inverse_currency(self):
        print("inverse currency")


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    win = App()
    win.show()

    app.exec()
