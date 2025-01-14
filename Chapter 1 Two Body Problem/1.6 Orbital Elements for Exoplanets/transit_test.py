from Helpers import two_body_system as tbs
from Helpers import constants as c
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def au_to_star_rad(dist: float, star: tbs.AstroBody) -> float:
    temp = dist * c.PhysicalConstants.au
    return temp / (star.radius*1000)


def area_of_intersection_circle(x1: float, y1: float, radius1: float, x2: float, y2: float, radius2: float) -> float:
    distance = np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) * c.PhysicalConstants.au
    r1 = radius1*1000
    r2 = radius2*1000
    if (distance >= r1 + r2):
        return 0.0
    elif (distance <= np.abs(r1 - r2)):
        return r2*r2*np.pi
    else:
        term1 = pow(r1, 2)*np.arccos((distance*distance + r1*r1 - r2*r2) / (2*distance*r1))
        term2 = pow(r2, 2)*np.arccos((distance*distance + r2*r2 - r1*r1) / (2*distance*r2))
        term3 = 0.5*np.sqrt(pow(2*r2*distance, 2) - pow(distance*distance + r2*r2 - r1*r1, 2))
        print(term1)
        return term1 + term2 - term3


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

# print(temp_trans)

if len(temp_trans) == 2:
    if (temp_trans[0][0] < temp_trans[1][0]):
        second_list = temp_trans[1].copy()
        temp_trans.pop(1)
        temp_trans.insert(0, second_list)
    temp_trans = temp_trans[0] + temp_trans[1]
elif (len(temp_trans) == 1):
    temp_trans = temp_trans[0]

# print()
# print(temp_trans)

transit_x = []
transit_y = []
flux = []
temp_time = []

for index in temp_trans:
    transit_x.append(system.body2_pos_x[index])
    transit_y.append(system.body2_pos_y[index])
    area_of_star = pow(system.body1.radius*1000, 2)*np.pi
    area_of_intersect = area_of_intersection_circle(system.body1_pos_x[index], system.body1_pos_y[index],
                                                    system.body1.radius, system.body2_pos_x[index],
                                                    system.body2_pos_y[index], system.body2.radius)
    flux.append(1 - area_of_intersect / area_of_star)
    temp_time.append(time[index])

print(flux)
print(temp_time)
max_time = max(temp_time)
min_time = min(temp_time)
min_flux = min(flux)
max_flux = max(flux)

fig = plt.figure(figsize=(7, 7))
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_aspect("equal")
ax2 = fig.add_subplot(1, 2, 2)

star_radius = b1.radius
max_val = 1 + b2.radius / b1.radius
max_val *= 1.1
dpv = fig.get_figwidth() * fig.get_dpi() / (max_val*2)
# print(dpv)
line1, = ax1.plot([], [], marker=".", markersize=dpv * b2.radius / b1.radius)
line2, = ax1.plot([0], [0], marker=".", markersize=dpv)
line3, = ax2.plot([], [])


def init():
    ax1.set(xlim=(-max_val, max_val), ylim=(-max_val, max_val))
    ax1.set_xlabel("X (Star Radii)")
    ax1.set_ylabel("Y (Star Radii)")
    ax2.set(xlim=(min_time, max_time), ylim=(min_flux*.95, max_flux*1.05))
    ax2.set_xlabel("Time (sec)")
    ax2.set_ylabel("Flux (Stellar Flux)")
    return line1, line3,


def update(step):
    x = transit_x[:step+1].copy()
    y = transit_y[:step+1].copy()

    for i in range(len(x)):
        x[i] = au_to_star_rad(x[i], b1)
        y[i] = au_to_star_rad(y[i], b1)

    line1.set_data([x[-1]], [y[-1]])
    line3.set_data(temp_time[:step+1], flux[:step+1])
    return line1, line3,


ani = FuncAnimation(fig, update, frames=len(temp_trans), init_func=init, interval=50, blit=True)
ani.save(filename="assets/transit_flux.gif", writer="pillow")
plt.show()
