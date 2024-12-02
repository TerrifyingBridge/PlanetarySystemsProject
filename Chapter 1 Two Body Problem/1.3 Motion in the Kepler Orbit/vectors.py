import math

import numpy as np


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return Vector2D(self.x, self.y)

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        return Vector2D(self.x, self.y)

    def multiply(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return Vector2D(self.x, self.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        mag = self.magnitude()
        return Vector2D(self.x / mag, self.y / mag)

    def __str__(self):
        return ("(" + str(self.x) + "," + str(self.y) + ")")


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return Vector3D(self.x, self.y, self.z)

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return Vector3D(self.x, self.y, self.z)

    def multiply(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return Vector3D(self.x, self.y, self.z)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        mag = self.magnitude()
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def angle_between(self, other):
        dot = self.x * other.x + self.y * other.y + self.z * other.z
        return np.arccos((dot / (self.magnitude() * other.magnitude())))

    def cross_mag(self, other):
        angle = self.angle_between(other)
        return (self.magnitude() * other.magnitude() * np.sin(angle))

    def __str__(self):
        return ("(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")")
