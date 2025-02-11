from Helpers import constants as const
import math

# 0 - .19R
def line1(x):
    return -591 * x + 148

# .19R - .33R
def line2(x):
    return -212.8 * x + 79.11

# .33R - .54R
def line3(x):
    return -40.96 * x + 22.31

# .54R - .71R
def line4(x):
    return -6.438 * x + 4.772

# .71R - 1R
def line5(x):
    return -1.325 * x + 1.250

def quad_moment(factor, slope, intercept):
    outside_term = math.pi / (mass * math.pow(r_equatorial, 2))
    inner_const = 4*b / (3 * math.pow(1 + b, 3/2))
    coef_const = intercept * math.pow(alpha*factor*r_polar,5) / 5
    inner_lin2 = math.atan(math.sqrt(b))*3*(b - 1) / (4 * math.pow(b, 3/2))
    inner_lin1 = (3*math.pow(b, 2) + 2*b + 3) / (4*b*math.pow(b + 1, 2))
    coef_lin = slope * math.pow(alpha*factor*r_polar, 6) / 6
    return outside_term * (coef_lin * (inner_lin1 + inner_lin2) + coef_const*inner_const)

flattening = 0.00005
r_equatorial = 6.95991756e8
r_polar = 6.9598438e8
alpha = r_equatorial / r_polar
b = alpha*alpha - 1
mass = const.Solar.mass
density = 1140

#print(4*density*alpha*alpha*math.pow(r_polar, 5)*math.pi*(alpha*alpha-1) / (15*mass*r_equatorial*r_equatorial))
#print(const.Solar.quadrupole_moment)

J_1 = quad_moment(0.19, -591 * 1000 / r_polar, 148 * 1000)
print(J_1)
J_21 = quad_moment(0.19, -212.8 * 1000 / r_polar, 79.11 * 1000)
J_22 = quad_moment(0.33, -212.8 * 1000 / r_polar, 79.11 * 1000)
J_2 = J_22 - J_21
print(J_2)
J_31 = quad_moment(0.33, -40.96 * 1000 / r_polar, 22.31 * 1000)
J_32 = quad_moment(0.54, -40.96 * 1000 / r_polar, 22.32 * 1000)
J_3 = J_32 - J_31
print(J_3)
J_41 = quad_moment(0.54, -6.438 * 1000 / r_polar, 4.772 * 1000)
J_42 = quad_moment(0.71, -6.438 * 1000 / r_polar, 4.772 * 1000)
J_4 = J_42 - J_41
print(J_4)
J_51 = quad_moment(0.71, -1.325 * 1000 / r_polar, 1.25 * 1000)
J_52 = quad_moment(1, -1.325 * 1000 / r_polar, 1.25 * 1000)
J_5 = J_52 - J_51
print(J_5)
#print()
#print(quad_moment(1, -155*1000 / r_polar, 155*1000))
print(J_1 + J_2 + J_3 + J_4 + J_5)
