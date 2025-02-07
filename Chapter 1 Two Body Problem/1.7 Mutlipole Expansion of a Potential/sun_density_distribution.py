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
    return -630*x + 155

def line2(x):
    return (11.87 - 30.5*x) / 0.15

def line3(x):
    return (7.2 - 7.2*x) / 0.75

line_x1 = [(i / 99) for i in range(19)]
line_y1 = [line1(i) for i in line_x1]

line_x2 = [(i / 99) for i in range(19, 36)]
line_y2 = [line2(i) for i in line_x2]

line_x3 = [(i / 99) for i in range(36, 100)]
line_y3 = [line3(i) for i in line_x3]

for i in range(len(x)):
    print(x[i], y[i])

print()
print((line_x2[-1], line_y2[-1]))

plt.scatter(x, y)
plt.plot(line_x1, line_y1, c="red")
plt.plot(line_x2, line_y2, c="orange")
plt.plot(line_x3, line_y3, c="yellow")
plt.yscale("log")
plt.show()
