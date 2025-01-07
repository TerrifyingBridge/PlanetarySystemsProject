import numpy as np
from PyQt6.QtWidgets import QMainWindow, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QWidget, QApplication, QGridLayout, QPushButton
from PyQt6.QtGui import QGuiApplication, QFont
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = None
        self.instructions = None
        self.mass1_label = None
        self.mass1_slider = None
        self.mass1_unit = None
        self.radius1_slider = None
        self.radius1_unit = None
        self.mass2_label = None
        self.mass2_slider = None
        self.mass2_unit = None
        self.radius2_slider = None
        self.radius2_unit = None
        self.incline_label = None
        self.incline_slider = None
        self.incline_unit = None
        self.peri_label = None
        self.peri_slider = None
        self.peri_unit = None
        self.semi_major_label = None
        self.semi_major_input = None
        self.semi_major_unit = None
        self.spacer1 = None
        self.ecc_label = None
        self.ecc_input = None
        self.ecc_unit = None
        self.rad_button = None
        self.transit_button = None
        self.astrometry_button = None
        self.image_button = None

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
        self.add_buttons(main_layout)

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
        self.instructions.setFixedHeight(int(self.window_height * 0.05))
        self.instructions.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.title)
        layout.addWidget(self.instructions)

    def add_body1(self, layout: QVBoxLayout) -> None:
        body1_layout = QHBoxLayout()
        self.mass1_label = QLabel("Star")
        self.mass1_slider = QSlider(Qt.Orientation.Horizontal)
        self.mass1_slider.setFixedWidth(int(self.window_width * 0.3))
        self.mass1_slider.setMinimum(1)
        self.mass1_slider.setMaximum(100)
        self.mass1_slider.setValue(19)
        self.mass1_slider.valueChanged.connect(self.mass1_update)
        self.mass1_unit = QLabel("1 Solar Mass")
        self.mass1_unit.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.radius1_slider = QSlider(Qt.Orientation.Horizontal)
        self.radius1_slider.setFixedWidth(int(self.window_width * 0.3))
        self.radius1_slider.setMinimum(1)
        self.radius1_slider.setMaximum(100)
        self.radius1_slider.setValue(11)
        self.radius1_slider.valueChanged.connect(self.radius1_update)
        self.radius1_unit = QLabel("1 Solar Radii")
        self.radius1_unit.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        body1_layout.addWidget(self.mass1_label)
        body1_layout.addWidget(self.mass1_slider)
        body1_layout.addWidget(self.mass1_unit)
        body1_layout.addWidget(self.radius1_slider)
        body1_layout.addWidget(self.radius1_unit)
        layout.addLayout(body1_layout)

    def mass1_update(self):
        cur_val = self.mass1_slider.value()
        cur_val = -0.4574 + 0.5604*np.e**(0.05189*cur_val)
        self.mass1_unit.setText(str(round(cur_val, 1)) + " Solar Mass")

    def radius1_update(self):
        cur_val = self.radius1_slider.value()
        cur_val = -0.6383 + 0.7263 * np.e ** (0.07228 * cur_val)
        self.radius1_unit.setText(str(round(cur_val, 1)) + " Solar Radii")

    def add_body2(self, layout: QVBoxLayout) -> None:
        body2_layout = QHBoxLayout()
        self.mass2_label = QLabel("Planet")
        self.mass2_slider = QSlider(Qt.Orientation.Horizontal)
        self.mass2_slider.setFixedWidth(int(self.window_width * 0.3))
        self.mass2_slider.setMinimum(0)
        self.mass2_slider.setMaximum(100)
        self.mass2_slider.setValue(90)
        self.mass2_slider.valueChanged.connect(self.mass2_update)
        self.mass2_unit = QLabel("1 Jupiter Mass")
        self.mass2_unit.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.radius2_slider = QSlider(Qt.Orientation.Horizontal)
        self.radius2_slider.setFixedWidth(int(self.window_width * 0.3))
        self.radius2_slider.setMinimum(1)
        self.radius2_slider.setMaximum(100)
        self.radius2_slider.setValue(10)
        self.radius2_slider.valueChanged.connect(self.radius2_update)
        self.radius2_unit = QLabel("1 Jupiter Radii")
        self.radius2_unit.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        body2_layout.addWidget(self.mass2_label)
        body2_layout.addWidget(self.mass2_slider)
        body2_layout.addWidget(self.mass2_unit)
        body2_layout.addWidget(self.radius2_slider)
        body2_layout.addWidget(self.radius2_unit)
        layout.addLayout(body2_layout)

    def mass2_update(self):
        cur_val = self.mass2_slider.value()
        cur_val = 0.05688 * np.e ** (0.04937 * cur_val)
        if cur_val >= 1:
            self.mass2_unit.setText(str(round(cur_val)) + " Jupiter Masses")
        else:
            self.mass2_unit.setText(str(round(cur_val * 317.906, 1)) + " Earth Masses")

    def radius2_update(self):
        cur_val = self.radius2_slider.value()
        cur_val = -324.21 + 324.18 * np.e ** (0.000305 * cur_val)
        if cur_val >= 1:
            self.radius2_unit.setText(str(round(cur_val, 2)) + " Jupiter Radii")
        else:
            self.radius2_unit.setText(str(round(cur_val * 11.2098, 2)) + " Earth Radii")

    def add_incline(self, layout: QVBoxLayout) -> None:
        incline_layout = QHBoxLayout()
        self.incline_label = QLabel("Inclination")
        self.incline_slider = QSlider(Qt.Orientation.Horizontal)
        self.incline_slider.setFixedWidth(int(self.window_width * 0.75))
        self.incline_slider.setMinimum(0)
        self.incline_slider.setMaximum(180)
        self.incline_slider.valueChanged.connect(self.incline_update)
        self.incline_unit = QLabel("0 Degrees")
        self.incline_unit.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        incline_layout.addWidget(self.incline_label)
        incline_layout.addWidget(self.incline_slider)
        incline_layout.addWidget(self.incline_unit)
        layout.addLayout(incline_layout)

    def incline_update(self):
        cur_val = self.incline_slider.value()
        self.incline_unit.setText(str(cur_val) + " Degrees")

    def add_peri(self, layout: QVBoxLayout) -> None:
        peri_layout = QHBoxLayout()
        self.peri_label = QLabel("Arg. of Periapsis")
        self.peri_slider = QSlider(Qt.Orientation.Horizontal)
        self.peri_slider.setFixedWidth(int(self.window_width * 0.75))
        self.peri_slider.setMinimum(0)
        self.peri_slider.setMaximum(360)
        self.peri_slider.valueChanged.connect(self.peri_update)
        self.peri_unit = QLabel("0 Degrees")
        self.peri_unit.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        peri_layout.addWidget(self.peri_label)
        peri_layout.addWidget(self.peri_slider)
        peri_layout.addWidget(self.peri_unit)
        layout.addLayout(peri_layout)

    def peri_update(self):
        cur_val = self.peri_slider.value()
        self.peri_unit.setText(str(cur_val) + " Degrees")

    def add_ae(self, layout: QVBoxLayout) -> None:
        ae_layout = QHBoxLayout()
        self.semi_major_label = QLabel("Separation Dist.")
        self.semi_major_input = QSlider(Qt.Orientation.Horizontal)
        self.semi_major_input.setMinimum(1)
        self.semi_major_input.setMaximum(100)
        self.semi_major_input.valueChanged.connect(self.semi_major_update)
        self.semi_major_input.setFixedWidth(int(self.window_width * 0.3))
        self.semi_major_unit = QLabel("0.2 AU")
        self.semi_major_unit.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.spacer1 = QWidget()
        self.spacer1.setFixedWidth(int(self.window_width * 0.05))
        self.ecc_label = QLabel("Eccentricity")
        self.ecc_input = QSlider(Qt.Orientation.Horizontal)
        self.ecc_input.setMinimum(0)
        self.ecc_input.setMaximum(99)
        self.ecc_input.valueChanged.connect(self.ecc_update)
        self.ecc_input.setFixedWidth(int(self.window_width * 0.3))
        self.ecc_unit = QLabel("0.0")
        self.ecc_unit.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        ae_layout.addWidget(self.semi_major_label)
        ae_layout.addWidget(self.semi_major_input)
        ae_layout.addWidget(self.semi_major_unit)
        ae_layout.addWidget(self.spacer1)
        ae_layout.addWidget(self.ecc_label)
        ae_layout.addWidget(self.ecc_input)
        ae_layout.addWidget(self.ecc_unit)
        layout.addLayout(ae_layout)

    def semi_major_update(self):
        cur_val = self.semi_major_input.value() / 5
        if cur_val >= 10:
            cur_val = round(cur_val)
        self.semi_major_unit.setText(str(cur_val) + " AU")

    def ecc_update(self):
        cur_val = self.ecc_input.value() / 100
        self.ecc_unit.setText(str(cur_val))

    def add_buttons(self, layout: QVBoxLayout) -> None:
        button_layout = QGridLayout()
        self.rad_button = QPushButton("Radial Velocity")
        self.rad_button.setFixedHeight(int(self.window_height * 0.05))
        self.transit_button = QPushButton("Transit")
        self.transit_button.setFixedHeight(int(self.window_height * 0.05))
        self.astrometry_button = QPushButton("Astrometry")
        self.astrometry_button.setFixedHeight(int(self.window_height * 0.05))
        self.image_button = QPushButton("Direct Imaging")
        self.image_button.setFixedHeight(int(self.window_height * 0.05))

        button_layout.addWidget(self.rad_button, 0, 0)
        button_layout.addWidget(self.transit_button, 0, 1)
        button_layout.addWidget(self.astrometry_button, 1, 0)
        button_layout.addWidget(self.image_button, 1, 1)
        layout.addLayout(button_layout)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
