import tkinter
import vectors
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def calc_semimajor_axis(r, v):
    r_mag = r.magnitude()
    v_mag = v.magnitude()

    temp = (2 / r_mag) - v_mag ** 2 / (G * M)
    return (1 / temp)


def calc_mean_motion(semi_axis):
    temp = G * M / np.abs(semi_axis) ** 3
    return np.sqrt(temp)


def calc_ang_momentum(r, v):
    return r.cross_mag(v)


def calc_e(ang_mom, semi_axis):
    temp = ang_mom ** 2 / (G * M * semi_axis)
    temp -= 1
    temp *= -1
    return np.sqrt(temp)


def is_r_dot_positive(r, v):
    temp_r = r.copy()
    temp_v = v.copy()

    temp_r.add(temp_v)

    return r.magnitude() < temp_r.magnitude()


def calc_u0(semi_axis, ecc, r, v):
    r_mag = r.magnitude()
    temp = r_mag / np.abs(semi_axis)
    if (ecc < 1):
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
        if (is_r_dot_positive(r, v)):
            return np.arccos(temp)
        else:
            return 2 * np.pi - np.arccos(temp)
    else:
        temp = (temp + 1) / ecc
        if (temp < 1):
            temp = 1
        return np.arccosh(temp)


def calc_l0(ecc, u):
    if (ecc < 1):
        return u - ecc * np.sin(u)
    else:
        return ecc * np.sinh(u) - u


def calc_l(l_0, mean_motion, time):
    return (l_0 + mean_motion * time)


def calc_u(l, ecc, accuracy):
    E = l
    err = E
    count = 0
    while (err > accuracy):
        if (ecc < 1):
            temp = l + ecc * np.sin(E)
            err = np.abs(E - temp)
            E = temp
            count += 1
        else:
            temp = (l - ecc * np.sinh(E) + E) / (ecc * np.cosh(E) - 1)
            err = np.abs(temp)
            # print(temp)
            E += temp
            count += 1
    return E


def calc_period(mean_motion, ecc):
    if (ecc < 1):
        return 2 * np.pi / mean_motion
    else:
        return 200


def start_sim():
    can_start = False
    try:
        r0 = vectors.Vector3D(int(start_pos_input1.get("1.0", "end-1c")),
                              int(start_pos_input2.get("1.0", "end-1c")),
                              int(start_pos_input3.get("1.0", "end-1c")))
        v0 = vectors.Vector3D(int(start_vel_input1.get("1.0", "end-1c")),
                              int(start_vel_input2.get("1.0", "end-1c")),
                              int(start_vel_input3.get("1.0", "end-1c")))
        print("loaded")
        err_label.config(text="")
        can_start = True
    except:
        err_label.config(text="Input Error - Try Again")

    if (can_start):
        for widget in root.winfo_children():
            widget.destroy()

        a = calc_semimajor_axis(r0, v0)
        n = calc_mean_motion(a)
        L = calc_ang_momentum(r0, v0)
        e = calc_e(L, a)
        u0 = calc_u0(a, e, r0, v0)
        l0 = calc_l0(e, u0)
        P = calc_period(n, e)

        def true_anom(u, trig):
            if (trig == "c" and e < 1):
                return (np.cos(u) - e) / (1 - e * np.cos(u))
            elif (trig == "s" and e < 1):
                return ((1 - e ** 2) ** (1 / 2) * np.sin(u)) / (1 - e * np.cos(u))
            elif (trig == "c" and e > 1):
                return (e - np.cosh(u)) / (e * np.cosh(u) - 1)
            elif (trig == "s" and e > 1):
                return (np.sinh(u) * (e ** 2 - 1) ** (1 / 2)) / (e * np.cosh(u) - 1)
            return None

        def f(t):
            temp_l = calc_l(l0, n, t)
            temp_u = calc_u(temp_l, e, 1e-10)
            top = true_anom(temp_u, "c") * true_anom(u0, "c") + true_anom(temp_u, "s") * true_anom(u0,
                                                                                                   "s") + e * true_anom(
                temp_u, "c")
            bot = 1 + e * true_anom(temp_u, "c")
            return top / bot

        def g(t):
            temp_l = calc_l(l0, n, t)
            temp_u = calc_u(temp_l, e, 1e-10)
            top = (true_anom(temp_u, "s") * true_anom(u0, "c") - true_anom(temp_u, "c") * true_anom(u0, "s")) * np.abs(
                1 - e ** 2) ** (3 / 2)
            bot = n * (1 + e * true_anom(temp_u, "c")) * (1 + e * true_anom(u0, "c"))
            return top / bot

        def position(t):
            temp_f = f(t)
            temp_g = g(t)
            temp_pos = r0.copy()
            temp_vel = v0.copy()

            temp_pos.multiply(temp_f)
            temp_vel.multiply(temp_g)
            return temp_pos.add(temp_vel)

        time = np.linspace(0, round(P + 1), 200)
        x = np.zeros(len(time))
        y = np.zeros(len(time))
        z = np.zeros(len(time))

        for i in range(len(time)):
            temp_vec = position(time[i])
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

        def init():
            ax.set(xlim3d=(-500, 500))
            ax.set(ylim3d=(-500, 500))
            ax.set(zlim3d=(-500, 500))
            return line1, line2, line3,

        def update(frame):
            line1.set_data_3d(x[:frame + 1], y[:frame + 1], z[:frame + 1])
            line2.set_data_3d([x[frame]], [y[frame]], [z[frame]])
            return line1, line2, line3,

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()

        print(e)
        ani = FuncAnimation(
            fig, update,
            frames=len(time),
            init_func=init, blit=False, interval=50)

        canvas.draw()


# Constants
G = 6.673430e-11
M = 10 ** 15

root = tkinter.Tk()
root.geometry("600x600")
root.title("Kepler Orbit")
center_window(root)

# Instructions
main_label = tkinter.Label(root, text="Kepler Orbits with Time", font=("Arial", 30))
main_label.pack()
instruction_label = tkinter.Label(root, text="Input a Starting Position and Velocity", font=("Arial", 16))
instruction_label.pack()
mass_label = tkinter.Label(root, text="A fixed mass of 10^15 kg is at (0,0)", font=("Arial", 12))
mass_label.pack()
graph_label = tkinter.Label(root, text="Each axis goes from -500 m to 500 m (x, y, and z)", font=("Arial", 12))
graph_label.pack()

# Starting Position Options
start_x_buff = 50
start_y_buff = 50
start_pos_label = tkinter.Label(root, text="Starting Pos: ", font=("Arial", 12))
start_pos_label.place(x=50 + start_x_buff, y=146 + start_y_buff)
start_pos_input1 = tkinter.Text(root, height=1, width=4)
start_pos_input1.place(x=170 + start_x_buff, y=150 + start_y_buff)
start_pos_label1 = tkinter.Label(root, text="X", font=("Arial", 12))
start_pos_label1.place(x=210 + start_x_buff, y=147 + start_y_buff)
start_pos_input2 = tkinter.Text(root, height=1, width=4)
start_pos_input2.place(x=270 + start_x_buff, y=150 + start_y_buff)
start_pos_label2 = tkinter.Label(root, text="Y", font=("Arial", 12))
start_pos_label2.place(x=310 + start_x_buff, y=147 + start_y_buff)
start_pos_input3 = tkinter.Text(root, height=1, width=4)
start_pos_input3.place(x=370 + start_x_buff, y=150 + start_y_buff)
start_pos_label3 = tkinter.Label(root, text="Z", font=("Arial", 12))
start_pos_label3.place(x=410 + start_x_buff, y=147 + start_y_buff)

# Starting Velocity Options
start_vel_label = tkinter.Label(root, text="Starting Vel: ", font=("Arial", 12))
start_vel_label.place(x=50 + start_x_buff, y=226 + start_y_buff)
start_vel_input1 = tkinter.Text(root, height=1, width=4)
start_vel_input1.place(x=170 + start_x_buff, y=230 + start_y_buff)
start_vel_label1 = tkinter.Label(root, text="X", font=("Arial", 12))
start_vel_label1.place(x=210 + start_x_buff, y=227 + start_y_buff)
start_vel_input2 = tkinter.Text(root, height=1, width=4)
start_vel_input2.place(x=270 + start_x_buff, y=230 + start_y_buff)
start_vel_label2 = tkinter.Label(root, text="Y", font=("Arial", 12))
start_vel_label2.place(x=310 + start_x_buff, y=227 + start_y_buff)
start_vel_input3 = tkinter.Text(root, height=1, width=4)
start_vel_input3.place(x=370 + start_x_buff, y=230 + start_y_buff)
start_vel_label3 = tkinter.Label(root, text="Z", font=("Arial", 12))
start_vel_label3.place(x=410 + start_x_buff, y=227 + start_y_buff)

start_button = tkinter.Button(root, text="Start Sim", font=("Arial", 12), command=start_sim, height=2, width=15)
start_button.pack(side=tkinter.BOTTOM, pady=10)

err_label = tkinter.Label(root, text="", font=("Arial", 20), fg="red")
err_label.pack(side=tkinter.BOTTOM, pady=5)

root.mainloop()
