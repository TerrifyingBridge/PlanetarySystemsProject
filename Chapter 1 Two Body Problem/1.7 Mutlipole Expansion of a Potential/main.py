from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QWidget,
    QSlider,
    QVBoxLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
import math


def generate_coefficients(degree: int) -> list[int]:
    temp_list: list[int] = []
    for n in range(degree):
        if (degree - 2 * n >= 0):
            scalar: float = math.pow(2, degree) * math.factorial(degree)
            temp_list.append(int(math.pow(-1, n) * math.comb(degree, n) * math.factorial(2 * degree - 2 * n) / (
                    scalar * math.factorial(degree - 2 * n))))
    return temp_list


def n_pole(degree: int, azimuth: float) -> float:
    coefficients: list[int] = generate_coefficients(degree)
    coefficients.reverse()
    val: float = np.cos(azimuth)
    temp: float = 0
    for i in range(len(coefficients)):
        temp += coefficients[i] * math.pow(val, (degree % 2) + 2 * i)
    return -temp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gravitational Multi-Pole Graphs")
        self.windowWidth: int = 500
        self.windowHeight: int = 500
        self.setFixedSize(self.windowWidth, self.windowHeight)

        main_layout = QVBoxLayout()

        title = QLabel("Gravitational Multi-Pole Potential")
        title_font = QFont("Arial", 20)
        title_font.setBold(True)
        title_font.setUnderline(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(title)

        instructions = QLabel("The graph below shows the gravitational potential from the multi-degree of degree l. \n"
                              "To see the different effects of the multi-degree on gravitational potential,\n"
                              "move and release the slider below.")
        instructions.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        instructions.setFont(QFont("Arial", 10))
        main_layout.addWidget(instructions)

        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        main_layout.addWidget(self.canvas)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 10)
        self.slider.setValue(0)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.valueChanged.connect(self.display_slider)
        self.slider.sliderReleased.connect(self.plot_pole)
        main_layout.addWidget(self.slider)

        self.pole_label = QLabel("Current Pole: 0-pole ( \u2113 = 0 )")
        self.pole_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.pole_label.setFixedHeight(30)
        main_layout.addWidget(self.pole_label)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.plot_pole()

    def display_slider(self) -> None:
        pole_val: int = self.slider.value()
        self.pole_label.setText("Current Pole: " + str(2 ** pole_val) + "-pole ( \u2113 = " + str(pole_val) + " )")

    def plot_pole(self):
        self.fig.clear()

        deg: int = self.slider.value()
        ax = self.fig.add_subplot(111, projection="3d")

        polar_angle = np.linspace(0, np.pi, 100)
        azimuth_angle = np.linspace(0, 2 * np.pi, 100)
        theta, phi = np.meshgrid(polar_angle, azimuth_angle)
        values = np.array([[n_pole(deg, theta[j, i]) for i in range(len(theta))] for j in range(len(phi))])

        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)

        cmap = mpl.colormaps["PRGn"]
        norm = colors.Normalize(vmin=np.min(values), vmax=np.max(values))
        ax.plot_surface(x, y, z, facecolors=cmap(norm(values)))
        ax.set_title(str(int(math.pow(2, deg))) + "-Pole")
        mappable = cm.ScalarMappable(norm=norm, cmap=cmap)
        mappable.set_array(values)
        self.fig.colorbar(mappable, ax=ax, pad=0.1)

        self.fig.text(0.01, 0.9, "Distance is in\nobject radius")
        self.fig.text(0.01, 0.05, "Color in terms \nof (GMJ/R)")

        self.canvas.draw()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
