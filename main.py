from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import random

user = os.getenv("username")
path = os.path.join(f"C:\\Users\\{user}\\Desktop")

class Window(QWidget):

    def __init__(self):

        QWindow.__init__(self)
        super(Window, self).__init__()
        self.setWindowTitle("Dark Mode Notepad")

        self.setStyleSheet("background-color: #1A303A; font-size: 18px; font-family: Ubuntu Mono, Open Sans")

        layout = QGridLayout()
        self.setLayout(layout)

        self.resize(853, 480)

        def save():

            filename = QFileDialog.getSaveFileName(self, "Save File", path, "*.txt")
            try:

                f = open(filename[0], "w")

                data = textarea.toPlainText()

                with f:

                    f.write(data)

            except FileNotFoundError:

                    print("File not found.")

        def open_file():

            filename = QFileDialog.getOpenFileName(self, "Save File", path, "*.txt")

            try:

                f = open(filename[0], "r")

                with f:

                    data = f.read()
                    textarea.setText(data)

                self.setWindowTitle(f"Dark Mode Notepad - {filename[0]}")

            except FileNotFoundError:

                print("File not found.")

        def change_bg():

            red = "background-color: #5E0000"
            orange = "background-color: #5E3100"
            yellow = "background-color: #5E5A00"
            green = "background-color: #005E03"
            blue = "background-color: #00395E"
            purple = "background-color: #42005E"
            pink = "background-color: #550055"

            colors = [red, orange, yellow, green, blue, purple, pink]
            color = random.choice(colors)

            self.setStyleSheet(f"{color}; font-size: 18px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
            savebutton.setStyleSheet(f"{color}; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
            openbutton.setStyleSheet(f"{color}; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
            #colorchange.setStyleSheet(f"{color}; font-size: 14px; font-family: Fira Mono, Open Sans; color: #FFFFFF")
            #resetbgbutton.setStyleSheet(f"{color}; font-size: 14px; font-family: Fira Mono, Open Sans; color: #FFFFFF")

        def reset_bg():

            reset = "background-color: #232323"
            self.setStyleSheet(f"{reset}; font-size: 18px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
            savebutton.setStyleSheet(f"{reset}; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
            openbutton.setStyleSheet(f"{reset}; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
            #colorchange.setStyleSheet(f"{reset}; font-size: 14px; font-family: Fira Mono, Open Sans; color: #FFFFFF")
            #resetbgbutton.setStyleSheet(f"{reset}; font-size: 14px; font-family: Fira Mono, Open Sans; color: #FFFFFF")

        def get_word_count():

            text = textarea.toPlainText()
            count = 0

            for word in text.split(" "):

                word = text.strip()
                if word:
                    count += 1

            wordcount_label.setText(f"Total Words: {count}")



        toolbar = QToolBar()
        savebutton = QToolButton()
        savebutton.setText("Save")
        savebutton.setStyleSheet("background-color: #13232A; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
        savebutton.clicked.connect(save)

        openbutton = QToolButton()
        openbutton.setText("Open")
        openbutton.setStyleSheet("background-color: #13232A; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
        openbutton.clicked.connect(open_file)

        wordcount_button = QToolButton()
        wordcount_button.setText("Get Word Count")
        wordcount_button.setStyleSheet("background-color: #13232A; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
        wordcount_button.clicked.connect(get_word_count)

        wordcount_label = QLabel()
        wordcount_label.setText("")
        wordcount_label.setStyleSheet("font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")

        """colorchange = QToolButton()
        colorchange.setText("Change Background Color")
        colorchange.setStyleSheet("background-color: #232323; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
        colorchange.clicked.connect(change_bg)"""

        """resetbgbutton = QToolButton()
        resetbgbutton.setText("Reset the Background Color")
        resetbgbutton.setStyleSheet("background-color: #232323; font-size: 14px; font-family: Ubuntu Mono, Open Sans; color: #FFFFFF")
        resetbgbutton.clicked.connect(reset_bg)"""

        layout.addWidget(toolbar)
        toolbar.addWidget(savebutton)
        toolbar.addSeparator()
        toolbar.addWidget(openbutton)
        toolbar.addSeparator()
        toolbar.addWidget(wordcount_button)
        toolbar.addSeparator()
        toolbar.addWidget(wordcount_label)
        #toolbar.addWidget(colorchange)
        #toolbar.addWidget(resetbgbutton)

        textarea = QTextEdit(self)
        textarea.setPlaceholderText("Enter text...")
        textarea.setStyleSheet("color: #74A8C1")
        textarea.setFont(QFont("Fira Mono", 14))
        layout.addWidget(textarea)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
