from Helpers import two_body_system as tbs
from Helpers import constants as c
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def au_to_star_rad(dist: float, star: tbs.AstroBody) -> float:
    temp = dist * c.PhysicalConstants.au
    return temp / (star.radius*1000)


b1 = tbs.AstroBody(c.Solar.mass, c.Solar.radius)
b2 = tbs.AstroBody(c.Jupiter.mass, c.Jupiter.reference_radius)

system = tbs.TwoBodySystem(b1, b2, 1, 0.25, np.pi / 2.0039, np.pi)

time = np.linspace(0, system.period, 100000)
system.fill_path_list(time)

temp_trans = []
temp = []
consec = 0
for i in range(len(system.body2_pos_x)):
    x = system.body2_pos_x[i] * c.PhysicalConstants.au
    y = system.body2_pos_y[i] * c.PhysicalConstants.au
    z = system.body2_pos_z[i]
    r_planet = system.body2.radius
    r_star = system.body1.radius
    if x**2 + y**2 <= (r_planet*1000 + r_star*1000)**2 and z >= 0:
        consec += 1
        temp.append(i)
        if (i == len(system.body2_pos_x) - 1):
            temp_trans.append(temp)
    else:
        if (consec != 0):
            temp_trans.append(temp)
            temp = []
        consec = 0

print(temp_trans)

if len(temp_trans) == 2:
    if (temp_trans[0][0] < temp_trans[1][0]):
        second_list = temp_trans[1].copy()
        temp_trans.pop(1)
        temp_trans.insert(0, second_list)
    temp_trans = temp_trans[0] + temp_trans[1]
elif (len(temp_trans) == 1):
    temp_trans = temp_trans[0]

print()
print(temp_trans)

transit_x = []
transit_y = []

for index in temp_trans:
    transit_x.append(system.body2_pos_x[index])
    transit_y.append(system.body2_pos_y[index])

fig = plt.figure(figsize=(7, 7))
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_aspect("equal")
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_aspect("equal")

star_radius = b1.radius
max_val = 1 + b2.radius / b1.radius
max_val *= 1.1
dpv = fig.get_figwidth() * fig.get_dpi() / (max_val*2)
print(dpv)
line1, = ax1.plot([], [], marker=".", markersize=dpv * b2.radius / b1.radius)
line2, = ax1.plot([0], [0], marker=".", markersize=dpv)


def init():
    ax1.set(xlim=(-max_val, max_val), ylim=(-max_val, max_val))
    return line1,


def update(step):
    x = transit_x[:step+1].copy()
    y = transit_y[:step+1].copy()

    for i in range(len(x)):
        x[i] = au_to_star_rad(x[i], b1)
        y[i] = au_to_star_rad(y[i], b1)

    line1.set_data([x[-1]], [y[-1]])
    return line1,


ani = FuncAnimation(fig, update, frames=len(temp_trans), init_func=init, interval=50, blit=True)
# ani.save(filename="assets/better_transit.gif", writer="pillow")
plt.show()
