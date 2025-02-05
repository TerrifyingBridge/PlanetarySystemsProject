from Helpers import constants as const
import math

flattening = 0.00005
r_equatorial = 6.95991756e8
r_polar = 6.9598438e8
alpha = r_equatorial / r_polar
mass = const.Solar.mass
density = 1140

print(4*density*alpha*alpha*math.pow(r_polar, 5)*math.pi*(alpha*alpha-1) / (15*mass*r_equatorial*r_equatorial))
print(const.Solar.quadrupole_moment)
