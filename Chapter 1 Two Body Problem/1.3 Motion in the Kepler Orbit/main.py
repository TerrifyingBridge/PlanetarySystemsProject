import vectors
import numpy as np

r_0 = vectors.Vector3D(100, 0, 100)
v_0 = vectors.Vector3D(0, -10, 0)

# Constants
G = 6.673430e-11
M = 10 ** 15


# Functions
def find_a(r, v):
    r_mag = r.magnitude()
    v_mag = v.magnitude()

    temp = (2 / r_mag) - v_mag ** 2 / (G * M)
    return (1 / temp)


def find_n(A):
    temp = G * M / A ** 3
    return np.sqrt(temp)


def find_L(r, v):
    return r.cross_mag(v)


def find_e(l, A):
    temp = l ** 2 / (G * M * A)
    temp -= 1
    temp *= -1
    return np.sqrt(temp)


a = find_a(r_0, v_0)
n = find_n(a)
L = find_L(r_0, v_0)
e = find_e(L, a)
print(e)
