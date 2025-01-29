import matplotlib.pyplot as plt
import numpy as np
import math

from Helpers import two_body_system as tbs
from Helpers import constants as const


def monopole(body: tbs.AstroBody, dist: float) -> float:
    return -1 * const.PhysicalConstants.gravitational_constant * body.mass / dist


def quadrupole(body: tbs.AstroBody, dist: float, theta: float) -> float:
    moment = const.Solar.quadrupole_moment
    val = moment*math.pow((body.radius*1000 / dist), 2)*((3/2)*math.pow(np.cos(theta), 2) - 1/2)
    return -1*const.PhysicalConstants.gravitational_constant * body.mass * val / dist


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
sun = tbs.AstroBody(const.Solar.mass, const.Solar.radius*1000)

distance = sun.radius*1500
polar_angle = np.linspace(0, np.pi, 100)
azimuth_angle = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(polar_angle, azimuth_angle)
# values = np.array([[monopole(sun, distance) for i in range(100)] for j in range(100)])
values = np.array([[quadrupole(sun, distance, theta[j, i]) for i in range(len(theta))] for j in range(len(phi))])
print(values.min(), values.max())

x = distance*np.sin(theta)*np.cos(phi)
y = distance*np.sin(theta)*np.sin(phi)
z = distance*np.cos(theta)

cmap = plt.cm.ScalarMappable(cmap=plt.get_cmap("PRGn"))
plot = ax.plot_surface(x, y, z, facecolors=cmap.to_rgba(values))
plt.colorbar(plot)

plt.show()
