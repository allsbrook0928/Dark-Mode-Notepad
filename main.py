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

        def save(self): # Attempt to write a save func, fix later

            name = QFileDialog.getSaveFileName(self, "Save File")
            file = open(name, "w")
            text = self.textarea
            file.write(text)
            file.close()

        saveFile = QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("Save File")
        # saveFile.triggered.connect(save(self)) **This is an attempt to write a save func, fix later

        self.textarea = QPlainTextEdit(self)
        self.textarea.setPlaceholderText("Enter text...")
        self.textarea.setStyleSheet("color: #FFFFFF")
        self.textarea.setFont(QFont("Open Sans", 14))
        layout.addWidget(self.textarea)

        self.toolbar = QToolBar()
        self.toolbutton = QToolButton()
        self.toolbutton.setText("Save")
        self.toolbutton.setFixedSize(60, 30)
        self.toolbutton.setStyleSheet("background-color: #565656; font-size: 14px; font-family: Open Sans; color: #FFFFFF")
        self.toolbutton.addAction(saveFile)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.toolbutton)

        


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())