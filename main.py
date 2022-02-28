from cProfile import label
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):

    def __init__(self):

        QWindow.__init__(self)
        self.setWindowTitle("Dark Mode Notepad")

        self.setStyleSheet("background-color: #232323")

        layout = QGridLayout()
        self.setLayout(layout)

        self.resize(853, 480)
        
        self.textarea = QPlainTextEdit(self)
        self.textarea.setPlaceholderText("Enter text...")
        self.textarea.setStyleSheet("color: #FFFFFF")
        self.textarea.setFont(QFont("Open Sans", 14))
        layout.addWidget(self.textarea)

        


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())