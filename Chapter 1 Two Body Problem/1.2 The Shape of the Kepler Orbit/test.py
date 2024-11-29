import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parabola(x):
    return 0.5 * x ** 2


x = [x/4 for x in range(-5*4, 5*4)]
y = [parabola(i) for i in x]
fig, ax = plt.subplots()
ax.grid()
line1, = ax.plot([], [], "red")
line2, = ax.plot([], [], "bo")


def init():
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1, 15)
    return line1, line2,


def update(frame):
    line1.set_data(x[:frame+1], y[:frame+1])
    line2.set_data([x[frame]], [y[frame]])
    return line1, line2,


ani = FuncAnimation(
    fig, update,
    frames=len(x),
    init_func=init, blit=True, interval=50)

plt.show()
