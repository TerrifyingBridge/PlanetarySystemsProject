from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbital Elements of Exoplanets")
        screen_rect = QGuiApplication.primaryScreen().geometry()
        test = QRect(0, 0, 2560, 1440)
        self.setFixedSize(600, 600)

        main_layout = QVBoxLayout()

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_layout)
        self.setCentralWidget(self.main_widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
