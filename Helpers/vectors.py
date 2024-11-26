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

    def __str__(self):
        return ("(" + str(self.x) + "," + str(self.y) + ")")