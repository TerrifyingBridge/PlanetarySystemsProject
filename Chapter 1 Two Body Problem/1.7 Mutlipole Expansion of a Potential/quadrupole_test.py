import matplotlib.pyplot as plt
import csv

x = []
y = []
with open("sun_density_dist.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            x.append(float(row[0]))
            y.append(float(row[1]))
        except ValueError:
            print("Header Line")

plt.plot(x, y)
plt.yscale("log")
plt.show()
