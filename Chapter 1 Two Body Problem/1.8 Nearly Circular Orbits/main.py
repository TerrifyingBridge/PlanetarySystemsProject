import math
import numpy as np
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
    QSlider,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation


class MainWindow(QMainWindow):
    slider_width = 100

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nearly Circular Orbits Simulation")
        self.setFixedSize(600, 600)
        self.setWindowIcon(QIcon("assets/logo.png"))

        self.stacked = QStackedWidget()
        self.main_page = QWidget()
        self.orbit_page = QWidget()
        self.sim_page = QWidget()

        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.ani = None

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
        orbit_button.clicked.connect(self.title_to_page1)
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
        self.path_button.toggled.connect(self.gen_sim)
        self.orbit_button = QRadioButton("View Change in Orbit")
        self.orbit_button.toggled.connect(self.gen_sim)
        orbit_type_layout.addWidget(self.path_button)
        orbit_type_layout.addWidget(orbit_type_spacer)
        orbit_type_layout.addWidget(self.orbit_button)
        orbit_page_layout.addLayout(orbit_type_layout)

        orbit_body_layout = QHBoxLayout()
        orbit_slider_layout = QVBoxLayout()

        orbit_x0_slider_layout = QHBoxLayout()
        orbit_x0_label = QLabel("Radius Diff.")
        self.orbit_x0_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_x0_slider.setFixedWidth(self.slider_width)
        self.orbit_x0_slider.setMinimum(0)
        self.orbit_x0_slider.setMaximum(100)
        self.orbit_x0_slider.valueChanged.connect(lambda: print(self.orbit_x0_slider.value() / 10))
        self.orbit_x0_slider.sliderReleased.connect(self.gen_sim)
        orbit_x0_slider_layout.addWidget(orbit_x0_label)
        orbit_x0_slider_layout.addWidget(self.orbit_x0_slider)
        orbit_slider_layout.addLayout(orbit_x0_slider_layout)

        orbit_z0_slider_layout = QHBoxLayout()
        orbit_z0_label = QLabel("Altitude Diff.")
        self.orbit_z0_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_z0_slider.setFixedWidth(self.slider_width)
        self.orbit_z0_slider.setMinimum(0)
        self.orbit_z0_slider.setMaximum(100)
        self.orbit_z0_slider.valueChanged.connect(lambda: print(self.orbit_z0_slider.value() / 10))
        self.orbit_z0_slider.sliderReleased.connect(self.gen_sim)
        orbit_z0_slider_layout.addWidget(orbit_z0_label)
        orbit_z0_slider_layout.addWidget(self.orbit_z0_slider)
        orbit_slider_layout.addLayout(orbit_z0_slider_layout)

        orbit_kr_slider_layout = QHBoxLayout()
        orbit_kr_label = QLabel("Radius Period")
        self.orbit_kr_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_kr_slider.setFixedWidth(self.slider_width)
        self.orbit_kr_slider.setMinimum(0)
        self.orbit_kr_slider.setMaximum(50)
        self.orbit_kr_slider.valueChanged.connect(lambda: print((1 + self.orbit_kr_slider.value() / 100)))
        self.orbit_kr_slider.sliderReleased.connect(self.gen_sim)
        orbit_kr_slider_layout.addWidget(orbit_kr_label)
        orbit_kr_slider_layout.addWidget(self.orbit_kr_slider)
        orbit_slider_layout.addLayout(orbit_kr_slider_layout)

        orbit_kz_slider_layout = QHBoxLayout()
        orbit_kz_label = QLabel("Altitude Period")
        self.orbit_kz_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_kz_slider.setFixedWidth(self.slider_width)
        self.orbit_kz_slider.setMinimum(0)
        self.orbit_kz_slider.setMaximum(50)
        self.orbit_kz_slider.valueChanged.connect(lambda: print((1 + self.orbit_kz_slider.value() / 100)))
        self.orbit_kz_slider.sliderReleased.connect(self.gen_sim)
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

    def clear_figure(self) -> None:
        if self.ani is not None:
            self.ani.event_source.stop()
            self.ani = None

        self.fig.clear()
        self.canvas.draw()

    def title_to_page1(self):
        self.stacked.setCurrentIndex(1)
        self.gen_sim()

    def gen_sim(self):
        self.clear_figure()
        ax = self.fig.add_subplot(111, projection="3d")
        ax.view_init(elev=15)
        center_pos, = ax.plot([0], [0], [0], "bo")
        orbit_path, = ax.plot([], [], [], "r")

        radius: float = 75.0

        x0: float = self.orbit_x0_slider.value() / 10
        z0: float = self.orbit_z0_slider.value() / 10
        kappa_phi: float = math.pow(radius ** 3, 1 / 2)
        kappa_r: float = kappa_phi * (1 + self.orbit_kr_slider.value() / 100)
        kappa_z: float = kappa_phi * (1 + self.orbit_kz_slider.value() / 100)
        period: float = 2 * math.pi / kappa_phi

        if (self.path_button.isChecked()):
            time = np.linspace(0, 5 * period, 500)

            x = np.zeros(len(time))
            y = np.zeros(len(time))
            z = np.zeros(len(time))

            for i in range(len(time)):
                phi = kappa_phi * time[i]
                diff_r = x0 * np.cos((kappa_r / kappa_phi) * phi)
                diff_z = z0 * np.cos((kappa_z / kappa_phi) * phi)

                x[i] = (diff_r + radius) * np.cos(phi)
                y[i] = (diff_r + radius) * np.sin(phi)
                z[i] = diff_z

            def init() -> None:
                ax.set(xlim=(-100, 100), ylim=(-100, 100), zlim=(-100, 100))
                ax.set_xlabel("X")
                ax.set_ylabel("Y")
                ax.set_zlabel("Z")

            def update(index):
                orbit_path.set_data_3d(x[:index], y[:index], z[:index])
                return orbit_path, center_pos,

            self.ani = FuncAnimation(self.fig, update, frames=len(time), init_func=init(), interval=15, blit=True)
            self.canvas.draw()
        else:
            orbits = np.linspace(0, 29, 30)

            def init() -> None:
                ax.set(xlim=(-100, 100), ylim=(-100, 100), zlim=(-100, 100))
                ax.set_xlabel("X")
                ax.set_ylabel("Y")
                ax.set_zlabel("Z")

            def update(index):
                phi = np.linspace(2 * np.pi * orbits[index], 2 * np.pi * (orbits[index] + 1), 100)
                x1 = []
                x2 = []
                x3 = []
                for i in range(len(phi)):
                    x = x0 * np.cos(kappa_r * phi[i] / kappa_phi)
                    r = x + radius
                    z = z0 * np.cos(kappa_z * phi[i] / kappa_phi)

                    x1.append(r * np.cos(phi[i]))
                    x2.append(r * np.sin(phi[i]))
                    x3.append(z)

                orbit_path.set_data_3d(x1, x2, x3)
                return center_pos, orbit_path,

            self.ani = FuncAnimation(self.fig, update, frames=len(orbits), init_func=init(), interval=100, blit=True)
            self.canvas.draw()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
