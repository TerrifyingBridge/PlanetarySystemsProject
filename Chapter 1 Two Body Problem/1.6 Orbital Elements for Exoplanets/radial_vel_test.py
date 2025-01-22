from Helpers import two_body_system as tbs
from Helpers import constants as c
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

b1 = tbs.AstroBody(c.Solar.mass, c.Solar.radius)
b2 = tbs.AstroBody(c.Jupiter.mass, c.Jupiter.reference_radius)

system = tbs.TwoBodySystem(b1, b2, 1, 0.3, np.pi/5, np.pi/3)

time = np.linspace(0, system.period, 500)
system.fill_path_list(time)
system.fill_los_vel()

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1, projection="3d")
line1, = ax.plot([], [], [])
line2, = ax.plot([], [], [])
line3, = ax.plot([], [], [], "bo")
line4, = ax.plot([], [], [], "r.")
max_val = 0.25 + system.semi_major_axis * (1 + system.eccentricity) / c.PhysicalConstants.au

ax2 = fig.add_subplot(1, 2, 2)
ax2.grid(True)
line5, = ax2.plot([], [])
line6, = ax2.plot([], [], "b.")


def init():
    ax.set(xlim=(-max_val, max_val), ylim=(-max_val, max_val), zlim=(-max_val, max_val))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    semi_amp = system.calc_semi_amplitude()
    ax2.set(xlim=(-10, time[-1]), ylim=(-semi_amp - semi_amp*0.1, semi_amp + semi_amp*0.1))
    return line1, line2, line3, line4, line5, line6,


def update(step):
    index = step+1
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


ani = FuncAnimation(fig, update, frames=len(time), init_func=init, interval=15, blit=True)
# ani.save(filename="assets/rad_vel.gif", writer="pillow")
plt.show()
