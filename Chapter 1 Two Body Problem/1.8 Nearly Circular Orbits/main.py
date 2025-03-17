from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QStackedWidget,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QRadioButton,
    QSlider
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    slider_width = 100

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nearly Circular Orbits Simulation")
        self.setFixedSize(600, 600)

        self.stacked = QStackedWidget()
        self.main_page = QWidget()
        self.orbit_page = QWidget()
        self.sim_page = QWidget()

        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)

        #######################
        # Creating First Page #
        #######################

        main_page_layout = QVBoxLayout()
        main_page_title = QLabel("Nearly Circular Orbits")
        title_font = QFont("Arial", 20)
        title_font.setBold(True)
        title_font.setUnderline(True)
        main_page_title.setFont(title_font)
        main_page_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_page_title.setFixedHeight(70)
        main_page_instructions = QLabel("Welcome to my simulation of nearly circular orbits! \n"
                                             "\n"
                                             "This program will give you the option of picking between two different \n"
                                             "types of simulations. The first button (on the left) will show you a \n"
                                             "simulation of an orbit given a radius, azimuth, and height timescale. \n"
                                             "The second button (on the right) will show you a simulation of an "
                                             "object\n"
                                             " in the orbit around various planets.")
        main_page_instructions.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_page_instructions.setFont(QFont("Arial", 12))

        main_page_button_layout = QHBoxLayout()
        main_page_buttons = QWidget()
        orbit_button = QPushButton("Orbit Page")
        orbit_button.setFixedHeight(300)
        orbit_button.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
        sim_button = QPushButton("Simulation Page")
        sim_button.setFixedHeight(300)
        sim_button.clicked.connect(lambda: self.stacked.setCurrentIndex(2))
        main_page_button_layout.addWidget(orbit_button)
        main_page_button_layout.addWidget(sim_button)
        main_page_buttons.setLayout(main_page_button_layout)

        main_page_layout.addWidget(main_page_title)
        main_page_layout.addWidget(main_page_instructions)
        main_page_layout.addWidget(main_page_buttons)
        self.main_page.setLayout(main_page_layout)

        #######################
        # Creating Orbit Page #
        #######################

        orbit_page_layout = QVBoxLayout()
        orbit_page_title = QLabel("General Nearly Circular Orbit")
        orbit_page_title.setFont(title_font)
        orbit_page_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        orbit_page_title.setFixedHeight(30)
        orbit_page_layout.addWidget(orbit_page_title)

        orbit_type_layout = QHBoxLayout()
        orbit_type_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        orbit_type_spacer = QWidget()
        orbit_type_spacer.setFixedWidth(100)
        self.path_button = QRadioButton("View Change in Body")
        self.path_button.setChecked(True)
        self.orbit_button = QRadioButton("View Change in Orbit")
        orbit_type_layout.addWidget(self.path_button)
        orbit_type_layout.addWidget(orbit_type_spacer)
        orbit_type_layout.addWidget(self.orbit_button)
        orbit_page_layout.addLayout(orbit_type_layout)

        orbit_body_layout = QHBoxLayout()
        orbit_slider_layout = QVBoxLayout()

        orbit_x0_slider_layout = QHBoxLayout()
        orbit_x0_label = QLabel("x0")
        self.orbit_x0_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_x0_slider.setFixedWidth(self.slider_width)
        self.orbit_x0_slider.setMinimum(0)
        self.orbit_x0_slider.setMaximum(10)
        orbit_x0_slider_layout.addWidget(orbit_x0_label)
        orbit_x0_slider_layout.addWidget(self.orbit_x0_slider)
        orbit_slider_layout.addLayout(orbit_x0_slider_layout)

        orbit_z0_slider_layout = QHBoxLayout()
        orbit_z0_label = QLabel("z0")
        self.orbit_z0_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_z0_slider.setFixedWidth(self.slider_width)
        self.orbit_z0_slider.setMinimum(0)
        self.orbit_z0_slider.setMaximum(10)
        orbit_z0_slider_layout.addWidget(orbit_z0_label)
        orbit_z0_slider_layout.addWidget(self.orbit_z0_slider)
        orbit_slider_layout.addLayout(orbit_z0_slider_layout)

        orbit_kr_slider_layout = QHBoxLayout()
        orbit_kr_label = QLabel("Kr")
        self.orbit_kr_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_kr_slider.setFixedWidth(self.slider_width)
        self.orbit_kr_slider.setMinimum(0)
        self.orbit_kr_slider.setMaximum(10)
        orbit_kr_slider_layout.addWidget(orbit_kr_label)
        orbit_kr_slider_layout.addWidget(self.orbit_kr_slider)
        orbit_slider_layout.addLayout(orbit_kr_slider_layout)

        orbit_kp_slider_layout = QHBoxLayout()
        orbit_kp_label = QLabel("Kp")
        self.orbit_kp_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_kp_slider.setFixedWidth(self.slider_width)
        self.orbit_kp_slider.setMinimum(0)
        self.orbit_kp_slider.setMaximum(10)
        orbit_kp_slider_layout.addWidget(orbit_kp_label)
        orbit_kp_slider_layout.addWidget(self.orbit_kp_slider)
        orbit_slider_layout.addLayout(orbit_kp_slider_layout)

        orbit_kz_slider_layout = QHBoxLayout()
        orbit_kz_label = QLabel("Kz")
        self.orbit_kz_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_kz_slider.setFixedWidth(self.slider_width)
        self.orbit_kz_slider.setMinimum(0)
        self.orbit_kz_slider.setMaximum(10)
        orbit_kz_slider_layout.addWidget(orbit_kz_label)
        orbit_kz_slider_layout.addWidget(self.orbit_kz_slider)
        orbit_slider_layout.addLayout(orbit_kz_slider_layout)

        orbit_body_layout.addLayout(orbit_slider_layout)
        orbit_body_layout.addWidget(self.canvas)
        orbit_page_layout.addLayout(orbit_body_layout)

        orbit_page_back_button = QPushButton("Back to Title Page")
        orbit_page_back_button.setFixedHeight(50)
        orbit_page_back_button.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        orbit_page_layout.addWidget(orbit_page_back_button)
        self.orbit_page.setLayout(orbit_page_layout)

        ###################################
        # Creating Planet Simulation Page #
        ###################################

        ##########################
        # Putting Pages Together #
        ##########################

        self.stacked.addWidget(self.main_page)
        self.stacked.addWidget(self.orbit_page)
        self.stacked.addWidget(self.sim_page)
        self.setCentralWidget(self.stacked)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
