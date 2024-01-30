import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv) #tạo ứng dụng app
msg_box = QMessageBox() # Tạo khung Message
msg_box.setWindowTitle("Error") # Tiêu đồ cửa sổ
msg_box.setIcon(QMessageBox.Icon.Warning) # Tạo icon
msg_box.setText("Vui lòng nhập Email hoặc Số điện thoại!") # Tạo nội dung bên trong.
msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c") # chỉnh sửa giao diện
sys.exit(msg_box.exec())