import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(1000, 1000, 2500, 2500)
        self.setWindowTitle("Пример QLabel")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создайте QLabel для отображения в главном окне."""
        hello_label = QLabel(self)
        hello_label.setText("Hello, World!")
        hello_label.move(600, 150)
        image = '11383065.png'
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(0, 0)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())