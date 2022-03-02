from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os

user = os.getenv("username")
path = os.path.join(f"C:\\Users\\{user}\\Desktop")

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

            filename = QFileDialog.getSaveFileName(self, "Save File", path, "(*.txt)")
            try:
                f = open(filename[0], "w")

                data = textarea.toHtml()

                with f:
                    f.write(data)

            except FileNotFoundError:
                    print("File not found.")

        def open_file():

            filename = QFileDialog.getOpenFileName(self, "Save File", path, "(*.txt)")
            f = open(filename[0], "r")

            with f:
                data = f.read()
                textarea.setText(data)

        toolbar = QToolBar()
        savebutton = QToolButton()
        savebutton.setText("Save")
        savebutton.setStyleSheet("background-color: #434343; font-size: 14px; font-family: Open Sans; color: #FFFFFF")
        savebutton.clicked.connect(save)

        openbutton = QToolButton()
        openbutton.setText("Open")
        openbutton.setStyleSheet("background-color: #434343; font-size: 14px; font-family: Open Sans; color: #FFFFFF")
        openbutton.clicked.connect(open_file)

        layout.addWidget(toolbar)
        toolbar.addWidget(savebutton)
        toolbar.addWidget(openbutton)

        textarea = QTextEdit(self)
        textarea.setPlaceholderText("Enter text...")
        textarea.setStyleSheet("color: #FFFFFF")
        textarea.setFont(QFont("Open Sans", 14))
        layout.addWidget(textarea)

        


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())