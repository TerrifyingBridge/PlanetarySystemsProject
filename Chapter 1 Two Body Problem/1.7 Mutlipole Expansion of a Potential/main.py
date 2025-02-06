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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gravitational Multi-Pole Graphs")
        self.windowWidth: int = 500
        self.windowHeight: int = 500
        self.setFixedSize(self.windowWidth, self.windowHeight)

        main_layout= QVBoxLayout()

        title = QLabel("Gravitational Multi-Pole Potential")
        title_font = QFont("Arial", 20)
        title_font.setBold(True)
        title_font.setUnderline(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(title)

        instructions = QLabel("The graph below shows the gravitational potential from the multi-pole of degree l. \n"
                              "To see the different effects of the multi-pole on gravitational potential,\n"
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
        main_layout.addWidget(self.slider)

        self.pole_label = QLabel("Current Pole: 0-pole ( \u2113 = 0 )")
        self.pole_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.pole_label.setFixedHeight(30)
        main_layout.addWidget(self.pole_label)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def display_slider(self) -> None:
        pole_val = self.slider.value()
        self.pole_label.setText("Current Pole: " + str(2 ** pole_val) + "-pole ( \u2113 = " + str(pole_val) + " )")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
