from Helpers import TwoBodySystem as tbs
from Helpers import constants as c
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

b1 = tbs.AstroBody(c.Solar.mass, c.Solar.radius)
b2 = tbs.AstroBody(c.Jupiter.mass, c.Jupiter.reference_radius)

system = tbs.TwoBodySystem(b1, b2, 1, 0.1, 0)

time = np.linspace(0, system.period, 500)
system.fill_path_list(time)

fig, ax = plt.subplots()
line1, = ax.plot([], [])
line2, = ax.plot([], [])
line3, = ax.plot([0], [0], "bo")
line4, = ax.plot([], [], "r.")
max_val = system.semi_major_axis * (1 + system.eccentricity) / c.PhysicalConstants.au


def init():
    plt.xlim(-max_val, max_val)
    plt.ylim(-max_val, max_val)
    return line1, line2, line3, line4,


def update(step):
    index = step+1
    temp1 = system.body1_pos_x[:index]
    temp2 = system.body1_pos_y[:index]
    temp3 = system.body2_pos_x[:index]
    temp4 = system.body2_pos_y[:index]

    line1.set_data(temp1, temp2)
    line2.set_data(temp3, temp4)
    line3.set_data([temp1[-1]], [temp2[-1]])
    line4.set_data([temp3[-1]], [temp4[-1]])
    return line1, line2, line3, line4,


ani = FuncAnimation(fig, update, frames=len(time), init_func=init, interval=15, blit=True)
# ani.save(filename="test_orbit.gif", writer="pillow")
plt.show()
