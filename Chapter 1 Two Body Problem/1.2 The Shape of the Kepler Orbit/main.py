import tkinter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def calc_a(energy):
    return -G * M / (2 * energy)


def calc_e(a_val, r_val):
    return (1 - r_val / a_val)


def calc_r(f_val):
    return (a * (1 - e ** 2)) / (1 + e * np.cos(f_val))


def polar_to_cart(r_val, th):
    return (r_val * np.cos(th), r_val * np.sin(th))


def start_sim():
    global en, r, a, e, peri, ani
    can_start = False

    try:
        en = int(energy_input.get("1.0", "end-1c"))
        r = int(rad_input.get("1.0", "end-1c"))
        peri = rad_var.get()
        print(en, r, peri)

        a = calc_a(en)
        e = calc_e(a, r)
        print(e)

        if (e < 0):
            err_label.config(text="Unreal Orbit - Increase Energy")
        else:
            can_start = True
    except:
        err_label.config(text="Input Error - Try Again")

    if (can_start):
        for widget in root.winfo_children():
            widget.destroy()

        if (e < 1):
            if (peri):
                f = np.linspace(0, 2 * np.pi, 100)
            else:
                f = np.linspace(-1*np.pi, np.pi, 100)
        else:
            f_infinity = np.arccos(-1 / e)
            f = np.linspace(-1*f_infinity, f_infinity, 102)
            np.delete(f, -1)
            np.delete(f, 0)
        r = calc_r(f)

        fig = plt.Figure(figsize=(5, 5))
        ax = fig.add_subplot()
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
            for i in range(frame + 1):
                transform = polar_to_cart(r[i], f[i])
                x.append(transform[0])
                y.append(transform[1])
            line1.set_data(x, y)
            line2.set_data([x[frame]], [y[frame]])
            return line1, line2, line3,

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()

        ani = FuncAnimation(
            fig, update,
            frames=len(f),
            init_func=init, blit=False, interval=50)

        # ani.save("test.gif")
        canvas.draw()


# Variables and Constants
en = 0
r = 0
a = 0
e = 0
G = 6.673430e-11
M = 10 ** 16
peri = False
ani = None

### Setting up GUI Stuff ###
root = tkinter.Tk()
root.geometry("400x400")
root.title("Kepler Orbit")
center_window(root)

# Instructions
main_label = tkinter.Label(root, text="Kepler Orbits", font=("Arial", 30))
main_label.pack()
instruction_label = tkinter.Label(root, text="Input an Energy and Starting Location", font=("Arial", 16))
instruction_label.pack()
mass_label = tkinter.Label(root, text="A fixed mass of 10^16 kg is at (0,0)", font=("Arial", 12))
mass_label.pack()
graph_label = tkinter.Label(root, text="The screen is 500m by 500m", font=("Arial", 12))
graph_label.pack()

# Energy Options
energy_label1 = tkinter.Label(root, text="Energy: ", font=("Arial", 12))
energy_label1.place(x=50, y=146)
energy_input = tkinter.Text(root, height=1, width=20)
energy_input.place(x=140, y=150)
energy_label2 = tkinter.Label(root, text="J", font=("Arial", 12))
energy_label2.place(x=330, y=147)

# Radius Options
rad_label1 = tkinter.Label(root, text="Dist. from (0,0): ", font=("Arial", 12))
rad_label1.place(x=20, y=196)
rad_input = tkinter.Text(root, height=1, width=20)
rad_input.place(x=140, y=200)
rad_label2 = tkinter.Label(root, text="m", font=("Arial", 12))
rad_label2.place(x=330, y=197)

# Angle Options
rad_var = tkinter.BooleanVar()
radio1 = tkinter.Radiobutton(root, text="Periapsis", variable=rad_var, value=True)
radio1.place(x=250, y=250)
radio2 = tkinter.Radiobutton(root, text="Apoapsis", variable=rad_var, value=False)
radio2.place(x=150, y=250)
ang_label = tkinter.Label(root, text="Start Position:", font=("Arial", 12))
ang_label.place(x=25, y=250)
rad_var.set(True)

start_button = tkinter.Button(root, text="Start Sim", font=("Arial", 12), command=start_sim, height=2, width=15)
start_button.pack(side=tkinter.BOTTOM, pady=10)

err_label = tkinter.Label(root, text="", font=("Arial", 20), fg="red")
err_label.pack(side=tkinter.BOTTOM, pady=5)

root.mainloop()
