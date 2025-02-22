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


def line1(x):
    return -591 * x + 148


def line2(x):
    return -212.8 * x + 79.11


def line3(x):
    return -40.96 * x + 22.31


def line4(x):
    return -6.438 * x + 4.772


def line5(x):
    return -1.325 * x + 1.250


line_x1 = [(i / 99) for i in range(19)]
line_y1 = [line1(i) for i in line_x1]

line_x2 = [(i / 99) for i in range(19, 33)]
line_y2 = [line2(i) for i in line_x2]

line_x3 = [(i / 99) for i in range(33, 54)]
line_y3 = [line3(i) for i in line_x3]

line_x4 = [(i / 99) for i in range(54, 71)]
line_y4 = [line4(i) for i in line_x4]

line_x5 = [(i / 99) for i in range(71, 100)]
line_y5 = [line5(i) for i in line_x5]

print(len(line_x1))

plt.scatter(x, y)
plt.plot(line_x1, line_y1, c="red")
plt.plot(line_x2, line_y2, c="orange")
plt.plot(line_x3, line_y3, c="yellow")
plt.plot(line_x4, line_y4, c="green")
plt.plot(line_x5, line_y5, c="purple")
plt.yscale("log")
plt.show()
