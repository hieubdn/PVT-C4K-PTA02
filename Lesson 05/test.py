# from PyQt6 import QtWidgets, uic
# from PyQt6.QtWidgets import QMessageBox
# import sys

# class Login_UI(QtWidgets.QMainWindow): # Tao class cho ui
#     def __init__(self):
#         super(Login_UI, self).__init__()
#         pageName = "untitled.ui" # trỏ đến ui tương ứng với đối tượng VD thầy đang tao class lớp Login thì đường dẫn của trỏ đến login-2.ui
#         uic.loadUi(pageName, self) # them thuoc tính load ra UI đó


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     login = Login_UI() #Cần khai báo class login để có thể sử dung nó toàn cục
#     login.show()
#     app.exec()

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
import sys
import os

class Login_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login_UI, self).__init__()
        script_directory = os.path.dirname(os.path.abspath(__file__))
        page_name = "lesson05.ui"
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
