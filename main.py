import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawflag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawflag(self, qp):
        color = [random.randint(0, 255) for _ in range(3)]
        a = random.randint(10, 100)
        qp.setBrush(QColor(*color))
        qp.drawEllipse(random.randint(0, 500), random.randint(0, 500), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())