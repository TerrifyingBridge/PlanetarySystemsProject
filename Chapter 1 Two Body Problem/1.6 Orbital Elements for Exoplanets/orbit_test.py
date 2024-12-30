from Helpers import two_body_system as tbs
from Helpers import constants as c
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

b1 = tbs.AstroBody(c.Solar.mass, c.Solar.radius)
b2 = tbs.AstroBody(c.Jupiter.mass, c.Jupiter.reference_radius)

system = tbs.TwoBodySystem(b1, b2, 1, 0.25, 0)

time = np.linspace(0, system.period, 500)
system.fill_path_list(time)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
line1, = ax.plot([], [], [])
line2, = ax.plot([], [], [])
line3, = ax.plot([], [], [], "bo")
line4, = ax.plot([], [], [], "r.")
max_val = 0.25 + system.semi_major_axis * (1 + system.eccentricity) / c.PhysicalConstants.au


def init():
    ax.set(xlim=(-max_val, max_val), ylim=(-max_val, max_val), zlim=(-max_val, max_val))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    return line1, line2, line3, line4,


def update(step):
    index = step+1
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
    return line1, line2, line3, line4,


ani = FuncAnimation(fig, update, frames=len(time), init_func=init, interval=15, blit=True)
# ani.save(filename="assets/test_3d_orbit.gif", writer="pillow")
plt.show()
