import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

G = 6.673430e-11
M = 10**16

def calc_a(energy):
    return -G*M / (2*energy)


def calc_e(r, a):
    return (1 - r/a)


def calc_r(f_val):
    return (a*(1 - e**2)) / (1 + e * np.cos(f_val))


def polar_to_cart(r_val, th):
    return (r_val * np.cos(th), r_val * np.sin(th))


En = 10000
r_start = 350
a = calc_a(En)
print(a)
e = calc_e(r_start, a)
print(e)
f = np.linspace(0, 2*np.pi, 100)
r = calc_r(f)

fig, ax = plt.subplots()
ax.grid()
line1, = ax.plot([], [], "red")
line2, = ax.plot([], [], "bo")
line3, = ax.plot([0], [0], "o", color="black", markersize=20)


def init():
    ax.set_xlim(-500, 500)
    ax.set_ylim(-500, 500)
    return line1, line2, line3,


def update(frame):
    x = []
    y = []
    for i in range(frame+1):
        transform = polar_to_cart(r[i], f[i])
        x.append(transform[0])
        y.append(transform[1])
    line1.set_data(x, y)
    line2.set_data([x[frame]], [y[frame]])
    return line1, line2, line3,


ani = FuncAnimation(
    fig, update,
    frames=len(f),
    init_func=init, blit=True, interval=50)

plt.show()
