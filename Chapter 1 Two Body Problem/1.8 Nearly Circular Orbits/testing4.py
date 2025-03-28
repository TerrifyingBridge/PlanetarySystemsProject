import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from Helpers import constants as const

planet_radius = const.Saturn.equatorial_radius
planet_radius *= 1000
orbit_radius = const.Saturn.equatorial_radius + 100
orbit_radius *= 1000
J2 = const.Saturn.quadrupole_moment
mass_par = const.Saturn.mass_parameter
ref_rad = const.Saturn.reference_radius * 1000

kappa_phi = math.sqrt((mass_par / math.pow(orbit_radius, 3)) * (1 + (3 * J2 * ref_rad ** 2) / (2 * orbit_radius ** 2)))
kappa_r = math.sqrt((mass_par / math.pow(orbit_radius, 3)) * (1 - (3 * J2 * ref_rad ** 2) / (2 * orbit_radius ** 2)))
kappa_z = math.sqrt((mass_par / math.pow(orbit_radius, 3)) * (1 + (9 * J2 * ref_rad ** 2) / (2 * orbit_radius ** 2)))

a = orbit_radius / (1 - (3 / 2) * J2 * math.pow(ref_rad / orbit_radius, 2))
e = 3 * J2 * math.pow(ref_rad, 2) / math.pow(orbit_radius, 2)
q = a * (1 - e)
x0 = orbit_radius - q
z0 = orbit_radius * np.tan(5 * (np.pi / 180))
print(e)

polar_angle = np.linspace(0, np.pi, 100)
azimuth_angle = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(polar_angle, azimuth_angle)

x = 0.9 * planet_radius * np.sin(theta) * np.cos(phi)
y = 0.9 * planet_radius * np.sin(theta) * np.sin(phi)
z = 0.9 * planet_radius * np.cos(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=15)

planet = ax.plot_surface(x, y, z)
# planet, = ax.plot([0], [0], [0], "bo")
orbit_path, = ax.plot([], [], [], "r")

time = np.linspace(0, 10 * (2 * np.pi / kappa_phi), 300)
orbits = np.linspace(0, 499, 500)


def init():
    ax.set(xlim=(-1.1 * orbit_radius, 1.1 * orbit_radius), ylim=(-1.1 * orbit_radius, 1.1 * orbit_radius),
           zlim=(-1.1 * orbit_radius, 1.1 * orbit_radius))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    return orbit_path,


def update(step):
    phi = np.linspace(2 * np.pi * orbits[step], 2 * np.pi * (orbits[step] + 1), 100)
    x1 = []
    x2 = []
    x3 = []
    for i in range(len(phi)):
        x = x0 * np.cos(kappa_r * phi[i] / kappa_phi)
        r = x + orbit_radius
        z = z0 * np.cos(kappa_z * phi[i] / kappa_phi)

        x1.append(r * np.cos(phi[i]))
        x2.append(r * np.sin(phi[i]))
        x3.append(z)

    orbit_path.set_data_3d(x1, x2, x3)
    return orbit_path,


ani = FuncAnimation(fig, update, frames=len(orbits), init_func=init, interval=100, blit=True)
# ani.save(filename="assets/sim_animation2.gif", writer="pillow")
plt.show()
