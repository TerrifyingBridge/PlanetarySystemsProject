import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib as mpl
import numpy as np
import math

from Helpers import two_body_system as tbs
from Helpers import constants as const


def monopole(body: tbs.AstroBody, dist: float) -> float:
    return -1 * const.PhysicalConstants.gravitational_constant * body.mass / dist


def quadrupole(body: tbs.AstroBody, dist: float, theta: float) -> float:
    moment = const.Solar.quadrupole_moment
    val = moment * math.pow((body.radius * 1000 / dist), 2) * ((3 / 2) * math.pow(np.cos(theta), 2) - 1 / 2)
    return -1 * const.PhysicalConstants.gravitational_constant * body.mass * val / dist


def generate_coef(l: int) -> list[int]:
    temp_list: list[int] = []
    for n in range(l):
        if (l - 2 * n >= 0):
            scalar = math.pow(2, l) * math.factorial(l)
            temp_list.append(math.pow(-1, n) * math.comb(l, n) * math.factorial(2 * l - 2 * n) / (
                        scalar * math.factorial(l - 2 * n)))
    return temp_list


def n_pole(pole: int, azimuth: float) -> float:
    coefficients = generate_coef(pole)
    coefficients.reverse()
    val = np.cos(azimuth)
    temp = 0
    for i in range(len(coefficients)):
        # print((pole % 2) + 2*i)
        temp += coefficients[i] * math.pow(val, (pole % 2) + 2 * i)
    return -temp


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
sun = tbs.AstroBody(const.Solar.mass, const.Solar.radius * 1000)

distance = sun.radius * 1500
polar_angle = np.linspace(0, np.pi, 100)
azimuth_angle = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(polar_angle, azimuth_angle)
# values = np.array([[monopole(sun, distance) for i in range(100)] for j in range(100)])
values = np.array([[n_pole(6, theta[j, i]) for i in range(len(theta))] for j in range(len(phi))])

x = distance * np.sin(theta) * np.cos(phi)
y = distance * np.sin(theta) * np.sin(phi)
z = distance * np.cos(theta)

test = [2 * (i / 99) - 1 for i in range(100)]

print(generate_coef(4))

cmap = mpl.colormaps["PRGn"]
norm = mcolors.Normalize(vmin=np.min(values), vmax=np.max(values))
plot = ax.plot_surface(x, y, z, facecolors=cmap(norm(values)))
map = cm.ScalarMappable(norm=norm, cmap=cmap)
map.set_array(values)
fig.colorbar(map, ax=ax)

print(np.max(values))

plt.show()
