from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):

    def __init__(self):

        QWindow.__init__(self)
        super(Window, self).__init__()
        self.setWindowTitle("Dark Mode Notepad")

        self.setStyleSheet("background-color: #232323")

        layout = QGridLayout()
        self.setLayout(layout)

        self.resize(853, 480)
        
        def save(): # Attempt to write a save func, fix

            name = QFileDialog.getSaveFileName(self, "Save File")
            file = open(name, "w")
            text = self.textarea
            file.write(text)


        self.textarea = QPlainTextEdit(self)
        self.textarea.setPlaceholderText("Enter text...")
        self.textarea.setStyleSheet("color: #FFFFFF")
        self.textarea.setFont(QFont("Open Sans", 14))
        layout.addWidget(self.textarea)

        toolbar = QToolBar()
        savebutton = QToolButton()
        savebutton.setText("Save")
        savebutton.setFixedSize(60, 30)
        savebutton.setStyleSheet("background-color: #565656; font-size: 14px; font-family: Open Sans; color: #FFFFFF")
        savebutton.clicked.connect(save)

        layout.addWidget(toolbar)
        layout.addWidget(savebutton)

        


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())