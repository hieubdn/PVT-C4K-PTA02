import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.resize(800, 600)
    window.setWindowTitle("Cửa sổ đầu tiên")
    # Tạo nút
    button = QPushButton('Click me', window)
    # Đặt nút vào giữa màn hình
    w, h = 100, 30
    x, y = int((800-w)/2), int((600-h)/2)
    button.setGeometry(x, y, w, h)
    window.show()


    sys.exit(app.exec())