import math


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
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        return Vector2D(self.x / mag, self.y/mag)

    def __str__(self):
        return ("(" + str(self.x) + "," + str(self.y) + ")")