import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
