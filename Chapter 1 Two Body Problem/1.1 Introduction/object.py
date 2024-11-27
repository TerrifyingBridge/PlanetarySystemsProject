import math

import vectors
import pygame

# m^3 kg^-1 s^-2
G = 6.673430e-11
# 1 tick = 10^2 seconds, or 600 times faster than real life
G *= 10**4


class Object:
    def __init__(self, pos, vel, mass, color):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos.x, self.pos.y), math.log10(self.mass))

    def update(self, other):
        temp_pos = vectors.Vector2D(other.pos.x, other.pos.y)
        temp_pos.subtract(self.pos)
        accel_mag = G * other.mass / temp_pos.magnitude() ** 2
        norm = temp_pos.normalize()
        accel = vectors.Vector2D(accel_mag * norm.x, accel_mag * norm.y)

        self.vel.add(accel)
        self.pos.add(self.vel)
