from PyQt6.QtWidgets import QMainWindow, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QWidget, QApplication
from PyQt6.QtGui import QGuiApplication, QFont
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbital Elements of Exoplanets")
        screen_rect = QGuiApplication.primaryScreen().geometry()
        self.window_height = int(screen_rect.height() * 0.6)
        self.window_width = int(screen_rect.width() * 0.6)
        self.setFixedSize(QSize(self.window_width, self.window_height))

        main_layout = QVBoxLayout()

        self.add_top(main_layout)
        self.add_body1(main_layout)
        self.add_body2(main_layout)
        self.add_incline(main_layout)
        self.add_peri(main_layout)
        self.add_ae(main_layout)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_layout)

        self.setCentralWidget(self.main_widget)

    def add_top(self, layout: QVBoxLayout) -> None:
        self.title = QLabel("Orbital Elements of Exoplanets")
        self.title.setFont(QFont("Arial", 24))
        self.title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.title.setFixedHeight(int(self.window_height * 0.1))
        self.title.setStyleSheet("background-color: lightgreen")

        self.instructions = QLabel("Input the orbital elements and click the button of the method detection you would "
                                   "like to see.")
        self.instructions.setFixedHeight(int(self.window_height * 0.1))
        self.instructions.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.title)
        layout.addWidget(self.instructions)

    def add_body1(self, layout: QVBoxLayout) -> None:
        body1_layout = QHBoxLayout()
        self.mass1_label = QLabel("Mass of Star")
        self.mass1_slider = QSlider(Qt.Orientation.Horizontal)
        self.mass1_unit = QLabel("kgs")
        body1_layout.addWidget(self.mass1_label)
        body1_layout.addWidget(self.mass1_slider)
        body1_layout.addWidget(self.mass1_unit)
        layout.addLayout(body1_layout)

    def add_body2(self, layout: QVBoxLayout) -> None:
        body2_layout = QHBoxLayout()
        self.mass2_label = QLabel("Mass of Planet")
        self.mass2_slider = QSlider(Qt.Orientation.Horizontal)
        self.mass2_unit = QLabel("kgs")
        body2_layout.addWidget(self.mass2_label)
        body2_layout.addWidget(self.mass2_slider)
        body2_layout.addWidget(self.mass2_unit)
        layout.addLayout(body2_layout)

    def add_incline(self, layout: QVBoxLayout) -> None:
        incline_layout = QHBoxLayout()
        self.incline_label = QLabel("Inclination")
        self.incline_slider = QSlider(Qt.Orientation.Horizontal)
        self.incline_slider.setMinimum(0)
        self.incline_slider.setMaximum(180)
        self.incline_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.incline_slider.setTickInterval(10)
        self.incline_unit = QLabel("Degrees")
        incline_layout.addWidget(self.incline_label)
        incline_layout.addWidget(self.incline_slider)
        incline_layout.addWidget(self.incline_unit)
        layout.addLayout(incline_layout)

    def add_peri(self, layout: QVBoxLayout) -> None:
        peri_layout = QHBoxLayout()
        self.peri_label = QLabel("Argument of Periapsis")
        self.peri_slider = QSlider(Qt.Orientation.Horizontal)
        self.peri_unit = QLabel("Degrees")
        peri_layout.addWidget(self.peri_label)
        peri_layout.addWidget(self.peri_slider)
        peri_layout.addWidget(self.peri_unit)
        layout.addLayout(peri_layout)

    def add_ae(self, layout: QVBoxLayout) -> None:
        ae_layout = QHBoxLayout()
        self.semi_major_label = QLabel("Distance of Separation")
        self.semi_major_input = QSlider(Qt.Orientation.Horizontal)
        self.semi_major_unit = QLabel("AU")
        self.spacer1 = QWidget()
        self.spacer1.setFixedWidth(int(self.window_width * 0.05))
        self.ecc_label = QLabel("Eccentricity")
        self.ecc_input = QSlider(Qt.Orientation.Horizontal)
        ae_layout.addWidget(self.semi_major_label)
        ae_layout.addWidget(self.semi_major_input)
        ae_layout.addWidget(self.semi_major_unit)
        ae_layout.addWidget(self.spacer1)
        ae_layout.addWidget(self.ecc_label)
        ae_layout.addWidget(self.ecc_input)
        layout.addLayout(ae_layout)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
