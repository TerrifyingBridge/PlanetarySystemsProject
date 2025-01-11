from Helpers import two_body_system as tbs
from Helpers import constants as c
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def au_to_star_rad(dist: float, star: tbs.AstroBody) -> float:
    temp = dist * c.PhysicalConstants.au
    return temp / star.radius


b1 = tbs.AstroBody(c.Solar.mass, c.Solar.radius)
b2 = tbs.AstroBody(c.Jupiter.mass, c.Jupiter.reference_radius)

system = tbs.TwoBodySystem(b1, b2, 1, 0.25, np.pi / 2, np.pi/2)

time = np.linspace(0, system.period, 100)
system.fill_path_list(time)

fig = plt.figure(figsize=(7, 7), layout="constrained")
spec = fig.add_gridspec(2, 2)
ax = fig.add_subplot(spec[:, 0], projection="3d")
ax1 = fig.add_subplot(spec[0, 1])
ax2 = fig.add_subplot(spec[1, 1])

line1, = ax.plot([], [], [])
line2, = ax.plot([], [], [])
line3, = ax.plot([], [], [], "bo")
line4, = ax.plot([], [], [], "r.")
max_val = 0.25 + system.semi_major_axis * (1 + system.eccentricity) / c.PhysicalConstants.au

star_radius = b1.radius
circle1 = plt.Circle((0, 0), 1.0, color="b")
circle2 = plt.Circle((-100, -100), b2.radius / b1.radius, color="r")
ax1.add_patch(circle1)
ax1.add_patch(circle2)


def init():
    ax.set(xlim=(-max_val, max_val), ylim=(-max_val, max_val), zlim=(-max_val, max_val))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax1.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
    return line1, line2, line3, line4, circle2


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

    circle2.center = (au_to_star_rad(temp4[-1], b1), au_to_star_rad(temp5[-1], b1))
    return line1, line2, line3, line4, circle2


ani = FuncAnimation(fig, update, frames=len(time), init_func=init, interval=50, blit=True)
# ani.save(filename="assets/bad_transit.gif", writer="pillow")
fig.tight_layout(pad=3.0)
plt.show()
