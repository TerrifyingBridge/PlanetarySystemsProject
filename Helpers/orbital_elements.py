from Helpers import vectors
import numpy as np

# Constants #
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


def calc_mean_anomaly(init_mean_anom: float, mean_motion: float, time: float) -> float:
    return init_mean_anom + mean_motion * time


def calc_eccentric_anomaly(mean_anon: float, ecc: float, accuracy: float) -> float:
    E = mean_anon
    err = E
    count = 0
    while (err > accuracy):
        temp = mean_anon + ecc * np.sin(E)
        err = np.abs(E - temp)
        E = temp
        count += 1
    return E


def calc_initial_f(ecc: float, ecc_anom: float) -> float:
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


def gauss_f_ecc_anom(ecc_anom: float, init_ecc_anom: float, ecc: float) -> float:
    top = np.cos(ecc_anom - init_ecc_anom) - ecc * np.cos(init_ecc_anom)
    bot = 1 - ecc * np.cos(init_ecc_anom)
    return top / bot


def gauss_g_ecc_anom(ecc_anom: float, init_ecc_anom: float, ecc: float, mean_motion: float) -> float:
    return (1 / mean_motion) * (np.sin(ecc_anom - init_ecc_anom) - ecc * np.sin(ecc_anom) + ecc * np.sin(init_ecc_anom))


def position_f(start_r: vectors.Vector3D, start_v: vectors.Vector3D, true_anom: float, init_true_anom: float,
               ecc: float,
               mean_motion: float) -> vectors.Vector3D:
    temp_r = start_r.copy()
    temp_v = start_v.copy()

    f_val = gauss_f_true_anom(true_anom, init_true_anom, ecc)
    g_val = gauss_g_true_anom(true_anom, init_true_anom, ecc, mean_motion)

    return temp_r.multiply(f_val).add(temp_v.multiply(g_val))


def velocity_f(start_r: vectors.Vector3D, start_v: vectors.Vector3D, true_anom: float, init_true_anom: float,
               ecc: float,
               mean_motion: float) -> vectors.Vector3D:
    temp_r = start_r.copy()
    temp_v = start_v.copy()

    dfdt_val = gauss_dfdt_true_anom(true_anom, init_true_anom, ecc, mean_motion)
    dgdt_val = gauss_dgdt_true_anom(true_anom, init_true_anom, ecc)

    return temp_r.multiply(dfdt_val).add(temp_v.multiply(dgdt_val))


def position_t(start_r: vectors.Vector3D, start_v: vectors.Vector3D, time: float, init_ecc_anom: float, ecc: float,
               mean_motion: float) -> vectors.Vector3D:
    temp_r = start_r.copy()
    temp_v = start_v.copy()

    l0 = calc_initial_l(ecc, init_ecc_anom)
    current_l = calc_mean_anomaly(l0, mean_motion, time)
    current_u = calc_eccentric_anomaly(current_l, ecc, 1e-10)

    f_val = gauss_f_ecc_anom(current_u, init_ecc_anom, ecc)
    g_val = gauss_g_ecc_anom(current_u, init_ecc_anom, ecc, mean_motion)

    return temp_r.multiply(f_val).add(temp_v.multiply(g_val))


def calc_period(mean_motion: float) -> float:
    return 2 * np.pi / mean_motion


def calc_arg_of_peri(peri_r: vectors.Vector3D, peri_v: vectors.Vector3D, incline: float) -> float:
    angle = np.arcsin(peri_r.z / (peri_r.magnitude() * np.sin(incline)))
    if (angle > 0):
        if (peri_v.z >= 0):
            return angle
        else:
            return np.pi - angle
    elif (angle < 0):
        if (peri_v.z >= 0):
            return 2 * np.pi + angle
        else:
            return np.pi - angle
    else:
        if (peri_v.z >= 0):
            return angle
        else:
            return np.pi


def calc_ascending_node(start_r: vectors.Vector3D, start_v: vectors.Vector3D, arg_of_peri: float, init_true_anom: float,
                        ecc: float, mean_motion: float) -> float:
    angle_diff = 2 * np.pi - arg_of_peri
    ascending_node_pos = position_f(start_r, start_v, angle_diff, init_true_anom, ecc, mean_motion)
    ascending_node = ascending_node_pos.angle_between(vectors.unit_x_3d)
    if (ascending_node_pos.y > 0):
        return ascending_node
    else:
        return 2 * np.pi - ascending_node


def calc_orbital_elements_l(start_r: vectors.Vector3D, start_v: vectors.Vector3D, M: int) -> list:
    a = calc_semi_major_axis(start_r, start_v, M)
    if (a <= 0):
        return [float("Nan")]
    n = calc_mean_motion(a, M)
    L = calc_ang_mom_mag(start_r, start_v)
    e = calc_eccentricity(L, a, M)
    I = calc_inclination(calc_ang_mom(start_r, start_v))
    u0 = calc_initial_u(a, e, start_r, start_v)
    l0 = calc_initial_l(e, u0)
    f0 = calc_initial_f(e, u0)

    pari_r = position_f(start_r, start_v, 0, f0, e, n)
    pari_v = velocity_f(start_r, start_v, 0, f0, e, n)
    arg_of_peri = calc_arg_of_peri(pari_r, pari_v, I)
    ascend_node = calc_ascending_node(start_r, start_v, arg_of_peri, f0, e, n)

    return [a, e, I, ascend_node, arg_of_peri, l0]


def calc_orbital_elements_f(start_r: vectors.Vector3D, start_v: vectors.Vector3D, M: int) -> list:
    a = calc_semi_major_axis(start_r, start_v, M)
    n = calc_mean_motion(a, M)
    L = calc_ang_mom_mag(start_r, start_v)
    e = calc_eccentricity(L, a, M)
    I = calc_inclination(calc_ang_mom(start_r, start_v))
    u0 = calc_initial_u(a, e, start_r, start_v)
    f0 = calc_initial_f(e, u0)

    pari_r = position_f(start_r, start_v, 0, f0, e, n)
    pari_v = velocity_f(start_r, start_v, 0, f0, e, n)
    arg_of_peri = calc_arg_of_peri(pari_r, pari_v, I)
    ascend_node = calc_ascending_node(start_r, start_v, arg_of_peri, f0, e, n)

    return [a, e, I, ascend_node, arg_of_peri, f0]


def calc_hill_variables(start_r: vectors.Vector3D, start_v: vectors.Vector3D, M: int) -> list:
    r_mag = start_r.magnitude()
    temp_r = start_r.copy()
    temp_r.add(start_v)
    r_dot = temp_r.magnitude() - r_mag

    a, e, incline, ascending_node, arg_of_peri, l = calc_orbital_elements_l(start_r, start_v, M)
    ang_mon = calc_ang_mom_mag(start_r, start_v)

    ecc_anom = calc_eccentric_anomaly(l, e, 1e-10)
    true_anom = calc_initial_f(e, ecc_anom)

    return [r_mag, arg_of_peri + true_anom, ascending_node, r_dot, ang_mon, ang_mon*np.cos(incline)]


def calc_delaunay_variables(start_r: vectors.Vector3D, start_v: vectors.Vector3D, M: int) -> list:
    a, e, incline, ascending_node, arg_of_peri, l = calc_orbital_elements_l(start_r, start_v, M)

    cap_lambda = np.sqrt(G*M*a)
    ang_mom = calc_ang_mom_mag(start_r, start_v)
    ang_mom_z = ang_mom*np.cos(incline)

    return [l, arg_of_peri, ascending_node, cap_lambda, ang_mom, ang_mom_z]


def calc_poincare_variables(start_r: vectors.Vector3D, start_v: vectors.Vector3D, M: int) -> list:
    a, e, I, ascend_node, arg_of_peri, l = calc_orbital_elements_l(start_r, start_v, M)
    ang_mom = calc_ang_mom_mag(start_r, start_v)
    ang_mom_z = ang_mom*np.cos(I)

    q1 = l + arg_of_peri + ascend_node
    p1 = np.sqrt(G*M*a)
    q2 = np.sqrt(2*(p1 - ang_mom))*np.cos(arg_of_peri + ascend_node)
    p2 = np.sqrt(2*(p1 - ang_mom))*np.sin(arg_of_peri + ascend_node)
    q3 = np.sqrt(2*(ang_mom - ang_mom_z))*np.cos(ascend_node)
    p3 = np.sqrt(2*(ang_mom - ang_mom_z))*np.sin(ascend_node)

    return [q1, q2, q3, p1, p2, p3]


if __name__ == "__main__":
    test_r = vectors.Vector3D(200, 200, 0)
    test_v = vectors.Vector3D(-15, 10, -5)

    test1 = vectors.Vector3D(200, 200, 200)
    test2 = vectors.Vector3D(1, -1, 1)

    print(calc_orbital_elements_l(test_r, test_v, 10 ** (15)))
    print(calc_hill_variables(test_r, test_v, 10 ** 15))
    print(calc_delaunay_variables(test_r, test_v, 10 ** 15))
    print(calc_poincare_variables(test_r, test_v, 10 ** 15))
