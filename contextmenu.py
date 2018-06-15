import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, qApp


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context Menu')
        self.show()

    def contextMenuEvent(self, event):
        pass