import vectors
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Broken Case 1 - FIXED
r_0 = vectors.Vector3D(-300, 100, 100)
v_0 = vectors.Vector3D(10, 8, -5)

# Broken Case 2 - FIXED
# r_0 = vectors.Vector3D(-300, 100, 0)
# v_0 = vectors.Vector3D(10, 8, 0)

# Working Case - STILL FIXED
# r_0 = vectors.Vector3D(-300, 100, 0)
# v_0 = vectors.Vector3D(0, 0, 10)

# Constants
G = 6.673430e-11
M = 10 ** 15


# Functions
def find_a(r, v):
    r_mag = r.magnitude()
    v_mag = v.magnitude()

    temp = (2 / r_mag) - v_mag ** 2 / (G * M)
    return (1 / temp)


def find_n(semi_axis):
    temp = G * M / semi_axis ** 3
    return np.sqrt(temp)


def find_ang_momentum(r, v):
    return r.cross_mag(v)


def find_e(ang_mom, semi_axis):
    temp = ang_mom ** 2 / (G * M * semi_axis)
    temp -= 1
    temp *= -1
    return np.sqrt(temp)


def is_r_dot_positive(r0, v0):
    temp_r = r0.copy()
    temp_v = v0.copy()

    temp_r.add(temp_v)

    return r0.magnitude() < temp_r.magnitude()


def find_u0(semi_axis, ecc, r):
    temp = r / semi_axis
    temp = (temp - 1) * -1
    temp /= ecc
    if (temp > 1):
        print(temp - 1)
        temp = 1
    elif (temp < -1):
        print(temp + 1)
        temp = -1
    else:
        print(temp)
    if (is_r_dot_positive(r_0, v_0)):
        return np.arccos(temp)
    else:
        return 2*np.pi - np.arccos(temp)


def find_l0(ecc, u_0):
    return u_0 - ecc * np.sin(u_0)


def calc_l(l_0, mean_motion, time):
    return (l_0 + mean_motion * time)


def calc_u(l, ecc, accuracy):
    E = l
    err = E
    count = 0
    while (err > accuracy):
        temp = l + ecc * np.sin(E)
        err = np.abs(E - temp)
        E = temp
        count += 1
    return E


def calc_period(mean_motion):
    return 2 * np.pi / mean_motion


def f(t):
    temp_l = calc_l(l0, n, t)
    temp_u = calc_u(temp_l, e, 1e-10)
    top = np.cos(temp_u - u0) - e * np.cos(u0)
    bot = 1 - e * np.cos(u0)
    return top / bot


def g(t):
    temp_l = calc_l(l0, n, t)
    temp_u = calc_u(temp_l, e, 1e-10)
    return (1 / n) * (np.sin(temp_u - u0) - e * np.sin(temp_u) + e * np.sin(u0))


def position(t):
    temp_f = f(t)
    temp_g = g(t)
    temp_pos = r_0.copy()
    temp_vel = v_0.copy()

    temp_pos.multiply(temp_f)
    temp_vel.multiply(temp_g)
    return temp_pos.add(temp_vel)


a = find_a(r_0, v_0)
n = find_n(a)
L = find_ang_momentum(r_0, v_0)
e = find_e(L, a)
u0 = find_u0(a, e, r_0.magnitude())
l0 = find_l0(e, u0)
P = calc_period(n)

time = np.linspace(0, round(P + 1), 200)
x = np.zeros(len(time))
y = np.zeros(len(time))
z = np.zeros(len(time))

for i in range(len(time)):
    temp_vec = position(time[i])
    temp_vec2 = r_0.copy()
    temp_vec2.subtract(temp_vec)
    x[i] = temp_vec.x
    y[i] = temp_vec.y
    z[i] = temp_vec.z

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection="3d")

line3, = ax.plot([0], [0], [0], "o", color="black", markersize=20)
line1, = ax.plot([], [], [], "red")
line2, = ax.plot([], [], [], "bo")


def init():
    ax.set(xlim3d=(-500, 500))
    ax.set(ylim3d=(-500, 500))
    ax.set(zlim3d=(-500, 500))
    return line1, line2, line3,


def update(frame):
    line1.set_data_3d(x[:frame + 1], y[:frame + 1], z[:frame + 1])
    line2.set_data_3d([x[frame]], [y[frame]], [z[frame]])
    return line1, line2, line3,


# ax.plot(x, y, z, label='parametric curve')
print(e)
ani = FuncAnimation(
    fig, update,
    frames=len(time),
    init_func=init, blit=True, interval=50)

plt.show()
