from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Canonical Orbital Elements")

        main_layout = QVBoxLayout()

        top_layout = QVBoxLayout()

        title = QLabel("Canonical Orbital Element Converter")
        title.setFont(QFont("Arial", 24))
        title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        title.setFixedHeight(50)

        instructions = QLabel("Input a position (m), velocity (m/s), and mass (kg)")
        instructions.setFont(QFont("Arial", 12))
        instructions.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        instructions.setFixedHeight(50)

        top_layout.addWidget(title)
        top_layout.addWidget(instructions)
        main_layout.addLayout(top_layout)

        middle_layout = QHBoxLayout()
        left_layout = QVBoxLayout()

        rad_label = QLabel("Position")
        vel_label = QLabel("Velocity")
        mass_label = QLabel("Mass")
        left_layout.addWidget(rad_label)
        left_layout.addWidget(vel_label)
        left_layout.addWidget(mass_label)
        middle_layout.addLayout(left_layout)

        center_layout = QVBoxLayout()
        for i in range(3):
            row_layout = QHBoxLayout()
            for j in range(3):
                row_layout.addWidget(QLabel("QLabel"))
                row_layout.addWidget(QLineEdit())
            center_layout.addLayout(row_layout)
        middle_layout.addLayout(center_layout)

        main_layout.addLayout(middle_layout)

        bottom_layout = QHBoxLayout()
        for i in range(2):
            col_layout = QVBoxLayout()
            for _ in range(3):
                col_layout.addWidget(QLabel("QLabel"))
            bottom_layout.addLayout(col_layout)

        main_layout.addLayout(bottom_layout)

        # Bottom button
        button = QPushButton("QButton")
        main_layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.setFixedSize(QSize(600, 600))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
