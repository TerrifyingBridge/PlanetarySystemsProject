from Helpers import vectors
from Helpers import orbital_elements
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# r0 = vectors.Vector3D(-300, 100, 100)
# v0 = vectors.Vector3D(10, 8, -5)

# Test
r0 = vectors.Vector3D(200, 200, 0)
v0 = vectors.Vector3D(-12, 10, -8)

# Constants
M = 10 ** 15

oe_list = orbital_elements.calc_orbital_elements_l(r0, v0, M)
a = oe_list[0]
e = oe_list[1]
ascend_node = oe_list[3]
arg_of_peri = oe_list[4]
l0 = oe_list[5]
u0 = orbital_elements.calc_initial_u(a, e, r0, v0)
f0 = orbital_elements.calc_initial_f(e, u0)
n = orbital_elements.calc_mean_motion(a, M)
P = orbital_elements.calc_period(n)

angle_diff = 2 * np.pi - arg_of_peri
ascend_node_pos = orbital_elements.position_f(r0, v0, angle_diff, f0, e, n)


time = np.linspace(0, round(P + 1), 200)
x = np.zeros(len(time))
y = np.zeros(len(time))
z = np.zeros(len(time))

x_pos = np.linspace(-500, 500, 100)
y_pos = np.linspace(-500, 500, 100)
X, Y = np.meshgrid(x_pos, y_pos)
Z = 0*X + 0*Y
z_pos = np.zeros((100, 100))

for i in range(len(time)):
    current_time = float(time[i])
    temp_vec = orbital_elements.position_t(r0, v0, current_time, u0, e, n)
    temp_vec2 = r0.copy()
    temp_vec2.subtract(temp_vec)
    x[i] = temp_vec.x
    y[i] = temp_vec.y
    z[i] = temp_vec.z

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection="3d")

line3, = ax.plot([0], [0], [0], "o", color="black", markersize=20)
line1, = ax.plot([], [], [], "red")
line2, = ax.plot([], [], [], "bo")
line4 = ax.plot_surface(X, Y, Z, alpha=0.25)
line5, = ax.plot([ascend_node_pos.x, 0], [ascend_node_pos.y, 0], [ascend_node_pos.z, 0], "green")


def init():
    ax.set(xlim3d=(-500, 500))
    ax.set(ylim3d=(-500, 500))
    ax.set(zlim3d=(-500, 500))
    return line1, line2, line3, line5, line4


def update(frame):
    line1.set_data_3d(x[:frame + 1], y[:frame + 1], z[:frame + 1])
    line2.set_data_3d([x[frame]], [y[frame]], [z[frame]])
    return line1, line2, line3, line5, line4


print(e)
ani = FuncAnimation(
    fig, update,
    frames=len(time),
    init_func=init, blit=True, interval=50)

plt.show()
