from Helpers import constants as const
import math


def frac(top, bot):
    return top / bot


'''
r_sync = 42164
r1 = const.Earth.reference_radius + 300
A = r1 / r_sync

# Problem 1.6a
v_esc = math.sqrt(2 * const.Earth.mass_parameter / (const.Earth.reference_radius*1000 + 300*1000))
v_cur = math.sqrt(const.Earth.mass_parameter / (const.Earth.reference_radius*1000 + 300*1000))

# Problem 1.6b
e = (1 - A) / (1 + A)
a1 = 24421
v1 = math.sqrt(const.Earth.mass_parameter * ( frac(2, r1*1000) - frac(1, a1*1000) ))
print(v1)
delta1 = v1 - v_cur
v2 = math.sqrt(const.Earth.mass_parameter / (r_sync * 1000))
v1a = math.sqrt(const.Earth.mass_parameter * (frac(2, r_sync*1000) - frac(1, a1*1000)))
print(v1a)
delta2 = v2 - v1a
print(delta2)
print(delta1 + delta2)

print((r_sync + r1) / 2)

print()

# Problem 1.6c
v_last = math.sqrt(const.Earth.mass_parameter / (r_sync*1000))
print(v_last)

print(v_last - v_cur)'''

r_cur = const.PhysicalConstants.au  # meters
v_cur = math.sqrt(const.Solar.mass_parameter / r_cur)
print(v_cur)
