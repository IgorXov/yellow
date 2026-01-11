import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor, QPen


class Circle:

    def __init__(self, center, diameter):
        self.center = center
        self.diameter = diameter


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi('UI.ui', self)

        self.addCircleButton.clicked.connect(self.add_circle)

        self.circles = []

        self.setMinimumSize(400, 300)

    def add_circle(self):
        diameter = random.randint(20, 100)

        max_x = self.width() - diameter
        max_y = self.height() - diameter

        if max_x > 0 and max_y > 0:
            x = random.randint(diameter // 2, max_x - diameter // 2)
            y = random.randint(diameter // 2, max_y - diameter // 2)

            self.circles.append(Circle(QPoint(x, y), diameter))

            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        pen = QPen(QColor(255, 255, 0))
        pen.setWidth(2)
        painter.setPen(pen)

        for circle in self.circles:
            x = circle.center.x() - circle.diameter // 2
            y = circle.center.y() - circle.diameter // 2

            painter.drawEllipse(x, y, circle.diameter, circle.diameter)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Окружности")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
