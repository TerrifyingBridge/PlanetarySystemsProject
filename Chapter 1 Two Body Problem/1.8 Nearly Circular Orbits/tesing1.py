import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation

radius = 75

# Kepler Orbits with GM = 1
kappa_r = math.pow((1.05*radius)**3, 1/2)
kappa_phi = math.pow((1*radius)**3, 1/2)
kappa_z = math.pow((1.05*radius)**3, 1/2)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

center_pos, = ax.plot([0], [0], [0], "bo")
orbit_path, = ax.plot([], [], [], "r")

time = np.linspace(0, 6*np.pi / kappa_r, 300)

x0 = 5
z0 = 5

x = np.zeros(len(time))
z = np.zeros(len(time))
phi = np.zeros(len(time))

x1 = np.zeros(len(time))
x2 = np.zeros(len(time))
x3 = np.zeros(len(time))

for i in range(len(time)):
    z[i] = z0 * np.cos(kappa_z*time[i])
    x[i] = x0 * np.cos(kappa_r*time[i])
    phi[i] = kappa_phi * time[i] - (2*x0*kappa_phi*np.sin(kappa_r*time[i])) / (radius * kappa_r)

    temp_r = x[i] + radius

    x1[i] = temp_r * np.cos(phi[i])
    x2[i] = temp_r * np.sin(phi[i])
    x3[i] = z[i]

def init():
    ax.set(xlim=(-100, 100), ylim=(-100, 100), zlim=(-100, 100))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    return center_pos, orbit_path,


def update(step):
    orbit_path.set_data_3d(x1[:step], x2[:step], x3[:step])
    return center_pos, orbit_path,


ani = FuncAnimation(fig, update, frames=len(time), init_func=init, interval=1, blit=True)
# ani.save(filename="assets/orbit_animation.gif", writer="pillow")
plt.show()
