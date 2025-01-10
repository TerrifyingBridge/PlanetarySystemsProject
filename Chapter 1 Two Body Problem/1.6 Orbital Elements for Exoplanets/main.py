import numpy as np
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QSlider,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QApplication,
    QGridLayout,
    QPushButton,
    QStackedWidget
)
from PyQt6.QtGui import QGuiApplication, QFont
from PyQt6.QtCore import Qt, QSize
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from Helpers import two_body_system as tbs
from Helpers import constants as c


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
        self.canvas = None
        self.ani = None

        self.setWindowTitle("Orbital Elements of Exoplanets")
        screen_rect = QGuiApplication.primaryScreen().geometry()
        self.window_height = int(screen_rect.height() * 0.6)
        self.window_width = int(screen_rect.width() * 0.6)
        self.setFixedSize(QSize(self.window_width, self.window_height))
        self.stacked = QStackedWidget()

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

        self.page2_layout = QVBoxLayout()
        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.page2_layout.addWidget(self.canvas)

        self.page1_button = QPushButton("Back to Settings")
        self.page1_button.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        self.page1_button.setFixedHeight(int(self.window_height * 0.05))
        self.page2_layout.addWidget(self.page1_button)

        self.page2 = QWidget()
        self.page2.setLayout(self.page2_layout)

        self.stacked.addWidget(self.main_widget)
        self.stacked.addWidget(self.page2)

        self.setCentralWidget(self.stacked)

    def add_top(self, layout: QVBoxLayout) -> None:
        self.title = QLabel("Orbital Elements of Exoplanets")
        self.title.setFont(QFont("Arial", 24))
        self.title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.title.setFixedHeight(int(self.window_height * 0.1))

        self.instructions = QLabel("Input the orbital elements and click the button of the method detection you would "
                                   "like to see.")
        self.instructions.setFont(QFont("Arial", 16))
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
        cur_val = -0.4574 + 0.5604 * np.e ** (0.05189 * cur_val)
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
        self.rad_button.clicked.connect(self.radial_vel)
        self.transit_button = QPushButton("Transit")
        self.transit_button.setFixedHeight(int(self.window_height * 0.05))
        self.astrometry_button = QPushButton("Astrometry")
        self.astrometry_button.setFixedHeight(int(self.window_height * 0.05))
        self.astrometry_button.clicked.connect(self.astrometry)
        self.image_button = QPushButton("Direct Imaging")
        self.image_button.setFixedHeight(int(self.window_height * 0.05))

        button_layout.addWidget(self.rad_button, 0, 0)
        button_layout.addWidget(self.transit_button, 0, 1)
        button_layout.addWidget(self.astrometry_button, 1, 0)
        button_layout.addWidget(self.image_button, 1, 1)
        layout.addLayout(button_layout)

    def clear_figure(self):
        if self.ani is not None:
            self.ani.event_source.stop()
            self.ani = None

        self.fig.clear()
        self.canvas.draw()

    def radial_vel(self):
        self.clear_figure()
        self.stacked.setCurrentIndex(1)

        mass1 = self.mass1_slider.value()
        mass1 = -0.4574 + 0.5604 * np.e ** (0.05189 * mass1)
        radius1 = self.radius1_slider.value()
        radius1 = -0.6383 + 0.7263 * np.e ** (0.07228 * radius1)
        mass2 = self.mass2_slider.value()
        mass2 = 0.05688 * np.e ** (0.04937 * mass2)
        radius2 = self.radius2_slider.value()
        radius2 = -324.21 + 324.18 * np.e ** (0.000305 * radius2)

        init_sep_dist = self.semi_major_input.value() / 5
        eccentricity = self.ecc_input.value() / 100
        incline = self.incline_slider.value() * (np.pi / 180)
        arg_of_peri = self.peri_slider.value() * (np.pi / 180)

        body1 = tbs.AstroBody(mass1 * c.Solar.mass, radius1 * c.Solar.radius)
        body2 = tbs.AstroBody(mass2 * c.Jupiter.mass, radius2 * c.Jupiter.reference_radius)

        system = tbs.TwoBodySystem(body1, body2, init_sep_dist, eccentricity, incline, arg_of_peri)
        time = np.linspace(0, system.period, 500)
        system.fill_path_list(time)
        system.fill_los_vel()
        max_vel = max(np.abs(system.los_vel))

        ax = self.fig.add_subplot(1, 2, 1, projection="3d")
        line1, = ax.plot([], [], [])
        line2, = ax.plot([], [], [])
        line3, = ax.plot([], [], [], "bo")
        line4, = ax.plot([], [], [], "r.")
        max_val = 0.25 + system.semi_major_axis * (1 + system.eccentricity) / c.PhysicalConstants.au

        ax2 = self.fig.add_subplot(1, 2, 2)
        ax2.grid(True)
        line5, = ax2.plot([], [])
        line6, = ax2.plot([], [], "b.")

        def init():
            ax.set(xlim=(-max_val, max_val), ylim=(-max_val, max_val), zlim=(-max_val, max_val))
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")

            ax2.set_xlim((-10, time[-1]))
            if not (max_vel == 0.0):
                ax2.set_ylim((-max_vel - max_vel * 0.1, max_vel + max_vel * 0.1))
            else:
                ax2.set_ylim((-0.5, 0.5))
            ax2.set_xlabel("Time (s)")
            ax2.set_ylabel("Line of Sight Velocity (m/s)")
            return line1, line2, line3, line4, line5, line6,

        def update(step):
            index = step + 1
            current_time = time[:index]

            temp1 = system.body1_pos_x[:index]
            temp2 = system.body1_pos_y[:index]
            temp3 = system.body1_pos_z[:index]
            temp4 = system.body2_pos_x[:index]
            temp5 = system.body2_pos_y[:index]
            temp6 = system.body2_pos_z[:index]

            line1.set_data_3d(temp1, temp2, temp3)
            line2.set_data_3d(temp4, temp5, temp6)
            line3.set_data_3d([temp1[-1]], [temp2[-1]], [temp3[-1]])
            line4.set_data_3d([temp4[-1]], [temp5[-1]], [temp6[-1]])

            temp_los_vel = system.los_vel[:index]
            line5.set_data(current_time, temp_los_vel)
            line6.set_data([current_time[-1]], [temp_los_vel[-1]])

            return line1, line2, line3, line4, line5, line6,

        self.ani = FuncAnimation(self.fig, update, frames=len(time), init_func=init, interval=15, blit=True)
        self.canvas.draw()

    def astrometry(self):
        self.clear_figure()
        self.stacked.setCurrentIndex(1)

        mass1 = self.mass1_slider.value()
        mass1 = -0.4574 + 0.5604 * np.e ** (0.05189 * mass1)
        radius1 = self.radius1_slider.value()
        radius1 = -0.6383 + 0.7263 * np.e ** (0.07228 * radius1)
        mass2 = self.mass2_slider.value()
        mass2 = 0.05688 * np.e ** (0.04937 * mass2)
        radius2 = self.radius2_slider.value()
        radius2 = -324.21 + 324.18 * np.e ** (0.000305 * radius2)

        init_sep_dist = self.semi_major_input.value() / 5
        eccentricity = self.ecc_input.value() / 100
        incline = self.incline_slider.value() * (np.pi / 180)
        arg_of_peri = self.peri_slider.value() * (np.pi / 180)

        body1 = tbs.AstroBody(mass1 * c.Solar.mass, radius1 * c.Solar.radius)
        body2 = tbs.AstroBody(mass2 * c.Jupiter.mass, radius2 * c.Jupiter.reference_radius)

        system = tbs.TwoBodySystem(body1, body2, init_sep_dist, eccentricity, incline, arg_of_peri)

        time = np.linspace(0, system.period, 500)
        system.fill_path_list(time)
        system.fill_astrometry()
        max_astrometry = np.abs(max(max(system.astrometry_x), max(system.astrometry_y))) / c.PhysicalConstants.au
        max_astrometry *= 1.1

        ax = self.fig.add_subplot(1, 2, 1, projection="3d")
        line1, = ax.plot([], [], [])
        line2, = ax.plot([], [], [])
        line3, = ax.plot([], [], [], "bo")
        line4, = ax.plot([], [], [], "r.")
        max_val = 0.25 + system.semi_major_axis * (1 + system.eccentricity) / c.PhysicalConstants.au

        ax1 = self.fig.add_subplot(1, 2, 2)
        line5, = ax1.plot([], [])

        def init():
            ax.set(xlim=(-max_val, max_val), ylim=(-max_val, max_val), zlim=(-max_val, max_val))
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")
            ax1.set(xlim=(-max_astrometry, max_astrometry), ylim=(-max_astrometry, max_astrometry))
            return line1, line2, line3, line4, line5,

        def update(step):
            index = step + 1
            temp1 = system.body1_pos_x[:index]
            temp2 = system.body1_pos_y[:index]
            temp3 = system.body1_pos_z[:index]
            temp4 = system.body2_pos_x[:index]
            temp5 = system.body2_pos_y[:index]
            temp6 = system.body2_pos_z[:index]
            temp7 = system.astrometry_x[:index].copy()
            temp8 = system.astrometry_y[:index].copy()

            line1.set_data_3d(temp1, temp2, temp3)
            line2.set_data_3d(temp4, temp5, temp6)
            line3.set_data_3d([temp1[-1]], [temp2[-1]], [temp3[-1]])
            line4.set_data_3d([temp4[-1]], [temp5[-1]], [temp6[-1]])

            for i in range(len(temp7)):
                temp7[i] /= c.PhysicalConstants.au
                temp8[i] /= c.PhysicalConstants.au

            line5.set_data(temp7, temp8)
            return line1, line2, line3, line4, line5,

        ani = FuncAnimation(self.fig, update, frames=len(time), init_func=init, interval=15, blit=True)
        self.canvas.draw()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
