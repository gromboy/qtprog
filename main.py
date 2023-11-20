import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setGeometry(100, 100, 500, 500)
        self.paint_ = False
        self.but.clicked.connect(self.paint)

    def paint(self):
        self.paint_ = True
        self.update()

    def paintEvent(self, event):
        if self.paint_:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.paint_ = False

    def draw_circle(self, qp):
        b = randint(30, 150)
        qp.setBrush(QColor(255, 219, 139))
        qp.drawEllipse(randint(0, 500 - b), randint(0, 500 - b), b, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
