import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        label_01 = QLabel('Zetcode', self)
        label_01.move(15, 10)

        label_02 = QLabel('tutorials', self)
        label_02.move(35, 40)

        label_03 = QLabel('for programmers', self)
        label_03.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
