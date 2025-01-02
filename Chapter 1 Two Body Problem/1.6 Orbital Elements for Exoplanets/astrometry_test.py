from Helpers import two_body_system as tbs
from Helpers import constants as c
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def get_thiele_innes_elements(two_body_system: tbs.TwoBodySystem) -> tuple[float, float, float, float]:
    start_term = two_body_system.body2.mass * two_body_system.semi_major_axis / (
            two_body_system.body1.mass + two_body_system.body2.mass)
    A = start_term * np.cos(two_body_system.peri)
    B = start_term * np.cos(two_body_system.inclination) * np.sin(two_body_system.peri)
    F = start_term * -1 * np.sin(two_body_system.peri)
    G = start_term * np.cos(two_body_system.inclination) * np.cos(two_body_system.peri)

    return A, B, F, G


b1 = tbs.AstroBody(c.Solar.mass, c.Solar.radius)
b2 = tbs.AstroBody(c.Jupiter.mass, c.Jupiter.reference_radius)

system = tbs.TwoBodySystem(b1, b2, 1, 0.25, np.pi/4, np.pi/2)

time = np.linspace(0, system.period, 500)
system.fill_path_list(time)

fig = plt.figure(layout="constrained")
spec = fig.add_gridspec(1, 2, hspace=1.0)
ax = fig.add_subplot(spec[0, 0], projection="3d")
line1, = ax.plot([], [], [])
line2, = ax.plot([], [], [])
line3, = ax.plot([], [], [], "bo")
line4, = ax.plot([], [], [], "r.")
max_val = 0.25 + system.semi_major_axis * (1 + system.eccentricity) / c.PhysicalConstants.au

ax1 = fig.add_subplot(spec[0, 1])
line5, = ax1.plot([], [])

x = []
y = []

A, B, F, G = get_thiele_innes_elements(system)
print(A, B, F, G)

for true_anom in system.true_anomaly_path:
    start_term = (1 - system.eccentricity**2) / (1 + system.eccentricity * np.cos(true_anom))
    temp_x = -start_term * (A*np.cos(true_anom) + F*np.sin(true_anom))
    temp_y = -start_term * (B*np.cos(true_anom) + G*np.sin(true_anom))

    x.append(temp_x / c.PhysicalConstants.au)
    y.append(temp_y / c.PhysicalConstants.au)
max_astrometry = np.abs(max(max(x), max(y)))
max_astrometry *= 1.1


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

    line1.set_data_3d(temp1, temp2, temp3)
    line2.set_data_3d(temp4, temp5, temp6)
    line3.set_data_3d([temp1[-1]], [temp2[-1]], [temp3[-1]])
    line4.set_data_3d([temp4[-1]], [temp5[-1]], [temp6[-1]])

    line5.set_data(x[:index], y[:index])
    return line1, line2, line3, line4, line5,


ani = FuncAnimation(fig, update, frames=len(time), init_func=init, interval=15, blit=True)
# ani.save(filename="assets/test_3d_orbit.gif", writer="pillow")
plt.tight_layout()
plt.show()
