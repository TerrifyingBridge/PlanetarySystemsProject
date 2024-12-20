from Helpers import vectors
import numpy as np


G = 6.673430e-11


def calc_semi_major_axis(r: vectors.Vector3D, v: vectors.Vector3D, M: int) -> float:
    r_mag = r.magnitude()
    v_mag = v.magnitude()

    temp = (2 / r_mag) - v_mag ** 2 / (G * M)
    return (1 / temp)


def calc_mean_motion(semi_major: float, M: int) -> float:
    temp = G * M / np.abs(semi_major) ** 3
    return np.sqrt(temp)


def calc_ang_mom_mag(r: vectors.Vector3D, v: vectors.Vector3D) -> float:
    return r.cross_mag(v)


def calc_ang_mom(r: vectors.Vector3D, v: vectors.Vector3D) -> vectors.Vector3D:
    return r.cross_prod(v)


def calc_eccentricity(ang_mom_mag: float, semi_major: float, M: int) -> float:
    temp = ang_mom_mag ** 2 / (G * M * semi_major)
    temp -= 1
    temp *= -1
    return np.sqrt(temp)


def calc_inclination(ang_mom: vectors.Vector3D) -> float:
    return ang_mom.angle_between(vectors.Vector3D(0, 0, 1))


def calc_initial_u(semi_major: float, ecc: float, r: vectors.Vector3D, v: vectors.Vector3D) -> float:
    r_mag = r.magnitude()
    temp = r_mag / np.abs(semi_major)
    temp = ((temp - 1) * -1) / ecc
    if (temp > 1):
        temp = 1
    elif (temp < -1):
        temp = -1
    if (is_r_dot_positive(r, v)):
        return np.arccos(temp)
    else:
        return 2 * np.pi - np.arccos(temp)


def is_r_dot_positive(r: vectors.Vector3D, v: vectors.Vector3D) -> bool:
    temp_r = r.copy()
    temp_v = v.copy()

    temp_r.add(temp_v)

    return r.magnitude() < temp_r.magnitude()


def calc_initial_l(ecc: float, ecc_anom: float) -> float:
    return ecc_anom - ecc * np.sin(ecc_anom)


def calc_initial_f(ecc_anom: float, ecc: float) -> float:
    top = np.cos(ecc_anom) - ecc
    bot = 1 - ecc * np.cos(ecc_anom)
    angle = np.arccos(top / bot)
    if (ecc_anom > np.pi):
        return 2 * np.pi - angle
    else:
        return angle


def gauss_f_true_anom(true_anom: float, init_true_anom: float, ecc: float) -> float:
    top = np.cos(true_anom - init_true_anom) + ecc * np.cos(true_anom)
    bot = 1 + ecc * np.cos(true_anom)
    return top / bot


def gauss_dfdt_true_anom(true_anom: float, init_true_amon: float, ecc: float, mean_motion: float) -> float:
    top = mean_motion * (ecc * np.sin(init_true_amon) - ecc * np.sin(true_anom) - np.sin(true_anom - init_true_amon))
    bot = (1 - ecc ** 2) ** (3 / 2)
    return top / bot


def gauss_g_true_anom(true_anom: float, init_true_anom: float, ecc: float, mean_motion: float) -> float:
    top = np.sin(true_anom - init_true_anom) * (1 - ecc ** 2) ** (3 / 2)
    bot = mean_motion * (1 + ecc * np.cos(true_anom)) * (1 + ecc * np.cos(init_true_anom))
    return top / bot


def gauss_dgdt_true_anom(true_anom: float, init_true_anom: float, ecc: float) -> float:
    top = ecc * np.cos(init_true_anom) + np.cos(true_anom - init_true_anom)
    bot = 1 + ecc * np.cos(init_true_anom)
    return top / bot


def position(start_r: vectors.Vector3D, start_v: vectors.Vector3D, true_anom: float, init_true_anom: float, ecc: float,
             mean_motion: float) -> vectors.Vector3D:
    temp_r = start_r.copy()
    temp_v = start_v.copy()

    f_val = gauss_f_true_anom(true_anom, init_true_anom, ecc)
    g_val = gauss_g_true_anom(true_anom, init_true_anom, ecc, mean_motion)

    return temp_r.multiply(f_val) + temp_v.multiply(g_val)


def velocity(start_r: vectors.Vector3D, start_v: vectors.Vector3D, true_anom: float, init_true_anom: float, ecc: float,
             mean_motion: float) -> vectors.Vector3D:
    temp_r = start_r.copy()
    temp_v = start_v.copy()

    dfdt_val = gauss_dfdt_true_anom(true_anom, init_true_anom, ecc, mean_motion)
    dgdt_val = gauss_dgdt_true_anom(true_anom, init_true_anom, ecc)

    return temp_r.multiply(dfdt_val) + temp_v.multiply(dgdt_val)


def calc_arg_of_peri(peri_r: vectors.Vector3D, peri_v: vectors.Vector3D, incline: float) -> float:
    angle = np.arcsin(peri_r.z / (peri_r.magnitude() * np.sin(incline)))
    if (angle > 0):
        if (peri_v.z >= 0):
            return angle
        else:
            return np.pi - angle
    elif (angle < 0):
        if (peri_v.z >= 0):
            return 2*np.pi + angle
        else:
            return np.pi - angle
    else:
        if (peri_v.z >= 0):
            return angle
        else:
            return np.pi


def calc_ascending_node(start_r: vectors.Vector3D, start_v: vectors.Vector3D, arg_of_peri: float, init_true_anom: float,
                        ecc: float, mean_motion: float) -> float:
    angle_diff = 2*np.pi - arg_of_peri
    ascending_node_pos = position(start_r, start_v, angle_diff, init_true_anom, ecc, mean_motion)
    ascending_node = ascending_node_pos.angle_between(vectors.unit_x_3d)
    if (ascending_node_pos.y > 0):
        return ascending_node
    else:
        return 2*np.pi - ascending_node


if __name__ == "__main__":
    test_r = vectors.Vector3D(100, 100, 0)
    test_v = vectors.Vector3D(-10, 10, -5)
