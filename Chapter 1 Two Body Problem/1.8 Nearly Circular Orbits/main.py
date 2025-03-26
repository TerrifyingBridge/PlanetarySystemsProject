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
    QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from Helpers import constants as const


class MainWindow(QMainWindow):
    slider_width = 125
    label_height = 20

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
        self.canvas1 = FigureCanvasQTAgg(self.fig)
        self.canvas2 = FigureCanvasQTAgg(self.fig)
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

        self.orbit_x0_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_x0_val = QLabel("0.0")
        self.orbit_x0_val.setFixedHeight(self.label_height)
        self.orbit_x0_slider.setMinimum(0)
        self.orbit_x0_slider.setMaximum(100)
        self.orbit_x0_slider.setFixedWidth(self.slider_width)
        self.orbit_x0_slider.sliderReleased.connect(self.gen_sim)
        self.orbit_x0_slider.valueChanged.connect(lambda: self.orbit_x0_val.setText(str(round(self.orbit_x0_slider.value() / 10, 2))))
        self.create_slider_box(self.orbit_x0_slider, self.orbit_x0_val, "Radius Diff.", orbit_slider_layout)

        self.orbit_z0_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_z0_val = QLabel("0.0")
        self.orbit_z0_val.setFixedHeight(self.label_height)
        self.orbit_z0_slider.setMinimum(0)
        self.orbit_z0_slider.setMaximum(100)
        self.orbit_z0_slider.setFixedWidth(self.slider_width)
        self.orbit_z0_slider.sliderReleased.connect(self.gen_sim)
        self.orbit_z0_slider.valueChanged.connect(lambda: self.orbit_z0_val.setText(str(round(self.orbit_z0_slider.value() / 10, 2))))
        self.create_slider_box(self.orbit_z0_slider, self.orbit_z0_val, "Altitude Diff.", orbit_slider_layout)

        self.orbit_kr_val = QLabel("1.0")
        self.orbit_kr_val.setFixedHeight(self.label_height)
        self.orbit_kr_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_kr_slider.setFixedWidth(self.slider_width)
        self.orbit_kr_slider.setMinimum(0)
        self.orbit_kr_slider.setMaximum(50)
        self.orbit_kr_slider.sliderReleased.connect(self.gen_sim)
        self.orbit_kr_slider.valueChanged.connect(lambda: self.orbit_kr_val.setText(str(round(1 + self.orbit_kr_slider.value() / 100, 2))))
        self.create_slider_box(self.orbit_kr_slider, self.orbit_kr_val, "Radius Freq.", orbit_slider_layout)

        self.orbit_kz_val = QLabel("1.0")
        self.orbit_kz_val.setFixedHeight(self.label_height)
        self.orbit_kz_slider = QSlider(Qt.Orientation.Horizontal)
        self.orbit_kz_slider.setFixedWidth(self.slider_width)
        self.orbit_kz_slider.setMinimum(0)
        self.orbit_kz_slider.setMaximum(50)
        self.orbit_kz_slider.sliderReleased.connect(self.gen_sim)
        self.orbit_kz_slider.valueChanged.connect(lambda: self.orbit_kz_val.setText(str(round(1 + self.orbit_kz_slider.value() / 100, 2))))
        self.create_slider_box(self.orbit_kz_slider, self.orbit_kz_val, "Altitude Freq.", orbit_slider_layout)

        orbit_body_layout.addLayout(orbit_slider_layout)
        orbit_body_layout.addWidget(self.canvas1)
        orbit_page_layout.addLayout(orbit_body_layout)

        orbit_page_back_button = QPushButton("Back to Title Page")
        orbit_page_back_button.setFixedHeight(50)
        orbit_page_back_button.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        orbit_page_layout.addWidget(orbit_page_back_button)
        self.orbit_page.setLayout(orbit_page_layout)

        ###################################
        # Creating Planet Simulation Page #
        ###################################

        sim_page_layout = QVBoxLayout()
        sim_page_title = QLabel("General Nearly Circular Orbit")
        sim_page_title.setFont(title_font)
        sim_page_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        sim_page_title.setFixedHeight(30)
        sim_page_layout.addWidget(orbit_page_title)

        sim_type_layout = QHBoxLayout()
        sim_type_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        sim_type_spacer = QWidget()
        sim_type_spacer.setFixedWidth(100)
        self.path_button2 = QRadioButton("View Change in Body")
        self.path_button2.setChecked(True)
        self.path_button2.toggled.connect(self.gen_sim)
        self.orbit_button2 = QRadioButton("View Change in Orbit")
        self.orbit_button2.toggled.connect(self.gen_sim)
        sim_type_layout.addWidget(self.path_button2)
        sim_type_layout.addWidget(sim_type_spacer)
        sim_type_layout.addWidget(self.orbit_button2)
        sim_page_layout.addLayout(sim_type_layout)

        sim_body_layout = QHBoxLayout()
        sim_slider_layout = QVBoxLayout()

        dropdown_layout = QVBoxLayout()
        planet_label = QLabel("Choose Planet")
        planet_label.setFixedHeight(self.label_height)
        self.planet_dropdown = QComboBox(self)
        self.planet_dropdown.setFixedWidth(self.slider_width)
        self.planet_dropdown.addItem("Sun")
        self.planet_dropdown.addItem("Moon")
        self.planet_dropdown.addItem("Earth")
        self.planet_dropdown.addItem("Jupiter")
        self.planet_dropdown.addItem("Saturn")
        self.planet_dropdown.addItem("Uranus")
        self.planet_dropdown.addItem("Neptune")
        self.planet_dropdown.activated.connect(self.planet_sim)
        dropdown_layout.addWidget(planet_label)
        dropdown_layout.addWidget(self.planet_dropdown)
        sim_slider_layout.addLayout(dropdown_layout)

        self.distance_val = QLabel("0 km")
        self.distance_val.setFixedHeight(self.label_height)
        self.distance_slider = QSlider(Qt.Orientation.Horizontal)
        self.distance_slider.setFixedWidth(self.slider_width)
        self.distance_slider.setMinimum(0)
        self.distance_slider.setMaximum(100)
        self.distance_slider.valueChanged.connect(lambda: self.distance_val.setText(str(round(self.distance_slider.value() * 5)) + " km"))
        self.create_slider_box(self.distance_slider, self.distance_val, "Dist. from Body", sim_slider_layout)

        self.incline_val = QLabel("0 deg")
        self.incline_val.setFixedHeight(self.label_height)
        self.incline_slider = QSlider(Qt.Orientation.Horizontal)
        self.incline_slider.setFixedWidth(self.slider_width)
        self.incline_slider.setMinimum(0)
        self.incline_slider.setMaximum(10)
        self.incline_slider.setValue(5)
        self.incline_slider.valueChanged.connect(lambda: self.incline_val.setText(str(round(self.incline_slider.value() - 5)) + " deg"))
        self.create_slider_box(self.incline_slider, self.incline_val, "Inclination", sim_slider_layout)

        sim_body_layout.addLayout(sim_slider_layout)
        sim_body_layout.addWidget(self.canvas2)
        sim_page_layout.addLayout(sim_body_layout)

        sim_page_back_button = QPushButton("Back to Title Page")
        sim_page_back_button.setFixedHeight(50)
        sim_page_back_button.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        sim_page_layout.addWidget(sim_page_back_button)
        self.sim_page.setLayout(sim_page_layout)

        ##########################
        # Putting Pages Together #
        ##########################

        self.stacked.addWidget(self.main_page)
        self.stacked.addWidget(self.orbit_page)
        self.stacked.addWidget(self.sim_page)
        self.setCentralWidget(self.stacked)

    def create_slider_box(self, slider: QSlider, value_label: QLabel, text: str, orb_layout: QVBoxLayout):
        vert_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        label = QLabel(text)
        label.setFixedHeight(self.label_height)
        top_layout.addWidget(label)
        top_layout.addWidget(value_label)
        vert_layout.addLayout(top_layout)
        vert_layout.addWidget(slider)
        orb_layout.addLayout(vert_layout)

    def clear_figure(self) -> None:
        if self.ani is not None:
            self.ani.event_source.stop()
            self.ani = None

        self.fig.clear()
        self.canvas1.draw()
        self.canvas2.draw()

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
            self.canvas1.draw()
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
            self.canvas1.draw()

    def title_to_page2(self):
        self.stacked.setCurrentIndex(2)
        self.planet_sim()

    def planet_sim(self):
        self.clear_figure()
        ax = self.fig.add_subplot(111, projection="3d")
        ax.init_view(elev=11)
        orbit_path, = ax.plot([], [], [], "r")
        orbit_radius = self.distance_slider.value() * 5
        inclination = self.incline_slider.value() - 5
        center_object = self.planet_dropdown.currentText()
        planet_radius = 0
        J2 = 0
        mass_par = 0
        ref_rad = 0

        if (center_object == "Sun"):
            planet_radius = const.Solar.radius * 1000
            J2 = const.Solar.quadrupole_moment
            mass_par = const.Solar.mass_parameter
            ref_rad = const.Solar.radius * 1000
        elif (center_object == "Earth"):
            planet_radius = const.Earth.equatorial_radius * 1000
            J2 = const.Earth.quadrupole_moment
            mass_par = const.Earth.mass_parameter
            ref_rad = const.Earth.reference_radius * 1000
        elif (center_object == "Moon"):
            planet_radius = const.Moon.mean_radius * 1000
            J2 = const.Moon.quadrupole_moment
            mass_par = const.Moon.mass_parameter
            ref_rad = const.Moon.reference_radius * 1000
        elif (center_object == "Jupiter"):
            planet_radius = const.Jupiter.equatorial_radius * 1000
            J2 = const.Jupiter.quadrupole_moment
            mass_par = const.Jupiter.mass_parameter
            ref_rad = const.Jupiter.reference_radius * 1000
        elif (center_object == "Saturn"):
            planet_radius = const.Saturn.equatorial_radius * 1000
            J2 = const.Saturn.quadrupole_moment
            mass_par = const.Saturn.mass_parameter
            ref_rad = const.Saturn.reference_radius * 1000
        elif (center_object == "Uranus"):
            planet_radius = const.Uranus.equatorial_radius * 1000
            J2 = const.Uranus.quadrupole_moment
            mass_par = const.Uranus.mass_parameter
            ref_rad = const.Uranus.reference_radius * 1000
        elif (center_object == "Neptune"):
            planet_radius = const.Neptune.equatorial_radius * 1000
            J2 = const.Neptune.quadrupole_moment
            mass_par = const.Neptune.mass_parameter
            ref_rad = const.Neptune.reference_radius * 1000
        orbit_radius = planet_radius + orbit_radius * 1000

        kappa_phi = math.sqrt(
            (mass_par / math.pow(orbit_radius, 3)) * (1 + (3 * J2 * ref_rad ** 2) / (2 * orbit_radius ** 2)))
        kappa_r = math.sqrt(
            (mass_par / math.pow(orbit_radius, 3)) * (1 - (3 * J2 * ref_rad ** 2) / (2 * orbit_radius ** 2)))
        kappa_z = math.sqrt(
            (mass_par / math.pow(orbit_radius, 3)) * (1 + (9 * J2 * ref_rad ** 2) / (2 * orbit_radius ** 2)))

        a = orbit_radius / (1 - (3 / 2) * J2 * math.pow(ref_rad / orbit_radius, 2))
        e = 3 * J2 * math.pow(ref_rad, 2) / math.pow(orbit_radius, 2)
        q = a * (1 - e)
        x0 = orbit_radius - q
        z0 = orbit_radius * np.tan(5 * (np.pi / 180))

        polar_angle = np.linspace(0, np.pi, 100)
        azimuth_angle = np.linspace(0, 2 * np.pi, 100)
        theta, phi = np.meshgrid(polar_angle, azimuth_angle)

        object_x = 0.9 * planet_radius * np.sin(theta) * np.cos(phi)
        object_y = 0.9 * planet_radius * np.sin(theta) * np.sin(phi)
        object_z = 0.9 * planet_radius * np.cos(theta)

        if (self.path_button2.isChecked()):
            time = np.linspace(0, 10 * (2 * np.pi / kappa_phi), 300)
            x = np.zeros(len(time))
            y = np.zeros(len(time))
            z = np.zeros(len(time))

            for i in range(len(time)):
                phi = kappa_phi * time[i]
                diff_x = x0 * np.cos(kappa_r * phi / kappa_phi)
                diff_z = z0 * np.cos(kappa_z * phi / kappa_phi)

                x[i] = (diff_x + orbit_radius) * np.cos(phi)
                y[i] = (diff_x + orbit_radius) * np.sin(phi)
                z[i] = diff_z

            def init():
                ax.set(xlim=(-1.1 * orbit_radius, 1.1 * orbit_radius), ylim=(-1.1 * orbit_radius, 1.1 * orbit_radius),
                       zlim=(-1.1 * orbit_radius, 1.1 * orbit_radius))
                ax.set_xlabel("X")
                ax.set_ylabel("Y")
                ax.set_zlabel("Z")

                return orbit_path,

            def update(index):
                orbit_path.set_data_3d(x[:index], y[:index], z[:index])
                return orbit_path,

            ani = FuncAnimation(self.fig, update, frames=len(time), init_func=init, interval=10, blit=True)
            self.canvas2.draw()
        else:
            pass


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
