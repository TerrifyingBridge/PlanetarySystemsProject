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
orbits = np.linspace(0, 19, 20)
print(orbits)

x0 = 5
z0 = 5

def init():
    ax.set(xlim=(-100, 100), ylim=(-100, 100), zlim=(-100, 100))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    return center_pos, orbit_path,


def update(step):
    phi = np.linspace(2*np.pi * orbits[step], 2*np.pi * (orbits[step] + 1), 100)
    x1 = []
    x2 = []
    x3 = []
    for i in range(len(phi)):
        x = x0 * np.cos(kappa_r * phi[i] / kappa_phi)
        r = x + radius
        z = z0 * np.cos(kappa_z * phi[i] / kappa_phi)

        x1.append(r*np.cos(phi[i]))
        x2.append(r*np.sin(phi[i]))
        x3.append(z)

    orbit_path.set_data_3d(x1, x2, x3)
    return center_pos, orbit_path,


ani = FuncAnimation(fig, update, frames=len(orbits), init_func=init, interval=100, blit=True)
# ani.save(filename="assets/orbit_animation.gif", writer="pillow")
plt.show()
