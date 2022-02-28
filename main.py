from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):

    def __init__(self):

        QWindow.__init__(self)
        self.setWindowTitle("Testing")

        layout = QGridLayout()
        self.setLayout(layout)

        self.resize(300, 200)

        label = QLabel("This is a test of PyQt5")
        layout.addWidget(label, 0, 0)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())