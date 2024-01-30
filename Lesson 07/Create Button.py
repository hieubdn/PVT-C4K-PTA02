import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton, QApplication, QMainWindow


class MainWindown(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Click me!!!")
        self.setCentralWidget(button)
        button.setCheckable(True)
        button.clicked.connect(self.the_button__was_clcked)

    def the_button__was_clcked(self):
        print("Clicked")

app = QApplication(sys.argv)

windown = MainWindown()
windown.show()

app.exec()
