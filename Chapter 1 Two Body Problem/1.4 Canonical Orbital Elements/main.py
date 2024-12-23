from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from Helpers import orbital_elements as oe
from Helpers import vectors as v
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
        rad_label.setFixedHeight(40)
        vel_label = QLabel("Velocity")
        vel_label.setFixedHeight(40)
        mass_label = QLabel("Mass")
        mass_label.setFixedHeight(40)
        left_layout.addWidget(rad_label)
        left_layout.addWidget(vel_label)
        left_layout.addWidget(mass_label)
        middle_layout.addLayout(left_layout)

        center_layout = QVBoxLayout()

        row_layout1 = QHBoxLayout()
        rad_x_label = QLabel("X")
        rad_y_label = QLabel("Y")
        rad_z_label = QLabel("Z")
        self.rad_x_input = QLineEdit()
        self.rad_y_input = QLineEdit()
        self.rad_z_input = QLineEdit()
        row_layout1.addWidget(rad_x_label)
        row_layout1.addWidget(self.rad_x_input)
        row_layout1.addWidget(rad_y_label)
        row_layout1.addWidget(self.rad_y_input)
        row_layout1.addWidget(rad_z_label)
        row_layout1.addWidget(self.rad_z_input)
        center_layout.addLayout(row_layout1)

        row_layout2 = QHBoxLayout()
        vel_x_label = QLabel("X")
        vel_y_label = QLabel("Y")
        vel_z_label = QLabel("Z")
        self.vel_x_input = QLineEdit()
        self.vel_y_input = QLineEdit()
        self.vel_z_input = QLineEdit()
        row_layout2.addWidget(vel_x_label)
        row_layout2.addWidget(self.vel_x_input)
        row_layout2.addWidget(vel_y_label)
        row_layout2.addWidget(self.vel_y_input)
        row_layout2.addWidget(vel_z_label)
        row_layout2.addWidget(self.vel_z_input)
        center_layout.addLayout(row_layout2)

        row_layout3 = QHBoxLayout()
        mass_label2 = QLabel("kg")
        self.mass_input = QLineEdit()
        row_layout3.addWidget(mass_label2)
        row_layout3.addWidget(self.mass_input)
        center_layout.addLayout(row_layout3)

        middle_layout.addLayout(center_layout)
        main_layout.addLayout(middle_layout)

        radio_layout = QHBoxLayout()
        hill_label = QLabel("Hill Variables")
        self.hill_input = QRadioButton()
        self.hill_input.setChecked(True)
        del_label = QLabel("Delaunay Variables")
        self.del_input = QRadioButton()
        poin_label = QLabel("Poincare Variables")
        self.poin_input = QRadioButton()
        radio_layout.addWidget(hill_label)
        radio_layout.addWidget(self.hill_input)
        radio_layout.addWidget(del_label)
        radio_layout.addWidget(self.del_input)
        radio_layout.addWidget(poin_label)
        radio_layout.addWidget(self.poin_input)
        main_layout.addLayout(radio_layout)

        bottom_layout = QHBoxLayout()

        filler_widget = QWidget()
        filler_widget.setFixedWidth(100)
        bottom_layout.addWidget(filler_widget)

        col_layout1 = QVBoxLayout()
        self.q1_label = QLabel("q1")
        self.q1_label.setFont(QFont("Arial", 12))
        self.q2_label = QLabel("q2")
        self.q2_label.setFont(QFont("Arial", 12))
        self.q3_label = QLabel("q3")
        self.q3_label.setFont(QFont("Arial", 12))
        col_layout1.addWidget(self.q1_label)
        col_layout1.addWidget(self.q2_label)
        col_layout1.addWidget(self.q3_label)
        bottom_layout.addLayout(col_layout1)

        col_layout2 = QVBoxLayout()
        self.p1_label = QLabel("p1")
        self.p1_label.setFont(QFont("Arial", 12))
        self.p2_label = QLabel("p2")
        self.p2_label.setFont(QFont("Arial", 12))
        self.p3_label = QLabel("p3")
        self.p3_label.setFont(QFont("Arial", 12))
        col_layout2.addWidget(self.p1_label)
        col_layout2.addWidget(self.p2_label)
        col_layout2.addWidget(self.p3_label)
        bottom_layout.addLayout(col_layout2)

        main_layout.addLayout(bottom_layout)

        self.err_label = QLabel("")
        self.err_label.setFont(QFont("Arial", 20))
        self.err_label.setStyleSheet("color: red")
        self.err_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        main_layout.addWidget(self.err_label)

        button = QPushButton("Calculate Canonical Elements")
        button.clicked.connect(self.activate_button)
        main_layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.setFixedSize(QSize(600, 600))

    def activate_button(self):
        try:
            r_x = float(self.rad_x_input.text())
            r_y = float(self.rad_y_input.text())
            r_z = float(self.rad_z_input.text())

            v_x = float(self.vel_x_input.text())
            v_y = float(self.vel_y_input.text())
            v_z = float(self.vel_z_input.text())

            mass = float(self.mass_input.text())

            hill = self.hill_input.isChecked()
            delaunay = self.del_input.isChecked()
            poincare = self.poin_input.isChecked()

            self.err_label.setText("")

            r0 = v.Vector3D(r_x, r_y, r_z)
            v0 = v.Vector3D(v_x, v_y, v_z)

            a = oe.calc_semi_major_axis(r0, v0, int(mass))
            if (a <= 0):
                self.err_label.setText("Hyperbolic Orbit. Decrease Velocity Magnitude")
            else:
                if (hill):
                    try:
                        q1, q2, q3, p1, p2, p3 = oe.calc_hill_variables(r0, v0, int(mass))
                        self.q1_label.setText("r: " + str(round(q1, 3)))
                        self.q2_label.setText("w: " + str(round(q2, 3)))
                        self.q3_label.setText("\uAB65: " + str(round(q3, 3)))
                        self.p1_label.setText("r" + "\u0307" + ": " + str(round(p1, 3)))
                        self.p2_label.setText("L: " + str(round(p2, 3)))
                        self.p3_label.setText("L<sub>z</sub>: " + str(round(p3, 3)))
                    except:
                        self.err_label.setText("Velocity and Radius Cannot be Parallel.")
                elif (delaunay):
                    try:
                        q1, q2, q3, p1, p2, p3 = oe.calc_delaunay_variables(r0, v0, int(mass))
                        self.q1_label.setText("\u2113: " + str(round(q1, 3)))
                        self.q2_label.setText("\u03C9: " + str(round(q2, 3)))
                        self.q3_label.setText("\uAB65: " + str(round(q3, 3)))
                        self.p1_label.setText("\u039B" + ": " + str(round(p1, 3)))
                        self.p2_label.setText("L: " + str(round(p2, 3)))
                        self.p3_label.setText("L<sub>z</sub>: " + str(round(p3, 3)))
                    except:
                        self.err_label.setText("Velocity and Radius Cannot be Parallel.")
                elif (poincare):
                    try:
                        q1, q2, q3, p1, p2, p3 = oe.calc_poincare_variables(r0, v0, int(mass))
                        self.q1_label.setText("\u03BB: " + str(round(q1, 3)))
                        self.q2_label.setText("[2(\u039B - L)]<sup>1/2</sup>cos(\u03D6): " + str(round(q2, 3)))
                        self.q3_label.setText("[2(L - L<sub>z</sub>)]<sup>1/2</sup>cos(\uAB65): " + str(round(q3, 3)))
                        self.p1_label.setText("\u039B" + ": " + str(round(p1, 3)))
                        self.p2_label.setText("[2(\u039B - L)]<sup>1/2</sup>sin(\u03D6): " + str(round(p2, 3)))
                        self.p3_label.setText("[2(L - L<sub>z</sub>)]<sup>1/2</sup>sin(\uAB65): " + str(round(p3, 3)))
                    except:
                        self.err_label.setText("Velocity and Radius Cannot be Parallel.")

        except:
            self.err_label.setText("Invalid Input. Please only use Numbers")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
