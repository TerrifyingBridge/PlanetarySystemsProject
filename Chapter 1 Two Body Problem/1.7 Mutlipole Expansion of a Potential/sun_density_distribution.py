import matplotlib.pyplot as plt
import csv
import math

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


# 190 or 155?
def exp1(x):
    return 155 * math.pow(10, -3.75 * x)


# Non-linear regression
def exp2(x):
    return 165 * math.pow(10, -3.16 * x)


line_x1 = [(i / 99) for i in range(100)]
line_y1 = [exp2(i) for i in line_x1]

plt.plot(x, y)
plt.plot(line_x1, line_y1)
#plt.yscale("log")
plt.show()
