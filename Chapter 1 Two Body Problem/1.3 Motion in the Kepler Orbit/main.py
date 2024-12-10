import tkinter

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def start_sim():
    pass

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
start_pos_label = tkinter.Label(root, text="Starting Pos: ", font=("Arial", 12))
start_pos_label.place(x=50, y=146)
start_pos_input1 = tkinter.Text(root, height=1, width=4)
start_pos_input1.place(x=170, y=150)
start_pos_label1 = tkinter.Label(root, text="X", font=("Arial", 12))
start_pos_label1.place(x=210, y=147)
start_pos_input2 = tkinter.Text(root, height=1, width=4)
start_pos_input2.place(x=270, y=150)
start_pos_label2 = tkinter.Label(root, text="Y", font=("Arial", 12))
start_pos_label2.place(x=310, y=147)
start_pos_input3 = tkinter.Text(root, height=1, width=4)
start_pos_input3.place(x=370, y=150)
start_pos_label3 = tkinter.Label(root, text="Z", font=("Arial", 12))
start_pos_label3.place(x=410, y=147)

# Starting Velocity Options
start_vel_label = tkinter.Label(root, text="Starting Vel: ", font=("Arial", 12))
start_vel_label.place(x=50, y=196)
start_vel_input1 = tkinter.Text(root, height=1, width=4)
start_vel_input1.place(x=170, y=200)
start_vel_label1 = tkinter.Label(root, text="X", font=("Arial", 12))
start_vel_label1.place(x=210, y=197)
start_vel_input2 = tkinter.Text(root, height=1, width=4)
start_vel_input2.place(x=270, y=200)
start_vel_label2 = tkinter.Label(root, text="Y", font=("Arial", 12))
start_vel_label2.place(x=310, y=197)
start_vel_input3 = tkinter.Text(root, height=1, width=4)
start_vel_input3.place(x=370, y=200)
start_vel_label3 = tkinter.Label(root, text="Z", font=("Arial", 12))
start_vel_label3.place(x=410, y=197)

start_button = tkinter.Button(root, text="Start Sim", font=("Arial", 12), command=start_sim, height=2, width=15)
start_button.pack(side=tkinter.BOTTOM, pady=10)

root.mainloop()