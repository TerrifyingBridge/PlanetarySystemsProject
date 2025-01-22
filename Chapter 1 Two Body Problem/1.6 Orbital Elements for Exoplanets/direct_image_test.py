from Helpers import two_body_system as tbs
from Helpers import constants as c
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

b1 = tbs.AstroBody(c.Solar.mass, c.Solar.radius)
b2 = tbs.AstroBody(c.Jupiter.mass, c.Jupiter.reference_radius)

system = tbs.TwoBodySystem(b1, b2, 1, 0.25, 0, np.pi/2)

time = np.linspace(0, system.period, 500)
system.fill_path_list(time)
system.fill_direct_image()

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection="3d")
line1, = ax.plot([], [], [])
line2, = ax.plot([], [], [])
line3, = ax.plot([], [], [], "bo")
line4, = ax.plot([], [], [], "r.")
max_val = 0.25 + system.semi_major_axis * (1 + system.eccentricity) / c.PhysicalConstants.au

ax1 = fig.add_subplot(1, 2, 2)
line5, = ax1.plot([], [])
line6, = ax1.plot([], [], "b.")
max_dist = max(max(np.abs(system.direct_image_x)), max(np.abs(system.direct_image_y))) / c.PhysicalConstants.au
max_dist *= 1.1


def init():
    ax.set(xlim=(-max_val, max_val), ylim=(-max_val, max_val), zlim=(-max_val, max_val))
    ax.set_xlabel("X (au)")
    ax.set_ylabel("Y (au)")
    ax.set_zlabel("Z (au)")

    ax1.set(xlim=(-max_dist, max_dist), ylim=(-max_dist, max_dist))
    ax1.set_xlabel("X (au)")
    ax1.set_ylabel("Y (au)")
    return line1, line2, line3, line4, line5, line6,


def update(step):
    index = step+1
    temp1 = system.body1_pos_x[:index]
    temp2 = system.body1_pos_y[:index]
    temp3 = system.body1_pos_z[:index]
    temp4 = system.body2_pos_x[:index]
    temp5 = system.body2_pos_y[:index]
    temp6 = system.body2_pos_z[:index]
    temp7 = system.direct_image_x[:index].copy()
    temp8 = system.direct_image_y[:index].copy()

    line1.set_data_3d(temp1, temp2, temp3)
    line2.set_data_3d(temp4, temp5, temp6)
    line3.set_data_3d([temp1[-1]], [temp2[-1]], [temp3[-1]])
    line4.set_data_3d([temp4[-1]], [temp5[-1]], [temp6[-1]])

    for i in range(len(temp7)):
        temp7[i] /= c.PhysicalConstants.au
        temp8[i] /= c.PhysicalConstants.au

    line5.set_data(temp7, temp8)
    line6.set_data([temp7[-1]], [temp8[-1]])
    return line1, line2, line3, line4, line5, line6,


ani = FuncAnimation(fig, update, frames=len(time), init_func=init, interval=15, blit=True)
ani.save(filename="assets/direct_image.gif", writer="pillow")
plt.show()
