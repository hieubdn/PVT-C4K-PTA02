from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
import sys
import os

class Login_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login_UI, self).__init__()
        script_directory = os.path.dirname(os.path.abspath(__file__))
        page_name = "Lesson07.ui" # Thay đổi tên file .ui
        ui_file_path = os.path.join(script_directory, page_name)

        try:
            uic.loadUi(ui_file_path, self)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"UI file '{page_name}' not found.")
            sys.exit(1)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login = Login_UI()
    login.show()
    sys.exit(app.exec())
