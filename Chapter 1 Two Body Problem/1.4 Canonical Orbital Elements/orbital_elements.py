import numpy as np
import vectors

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
    return ang_mom.angle_between(vectors.Vector3D(0,0,1))


if __name__ == "__main__":
    temp_r = vectors.Vector3D(100, 100, 0)
    temp_v = vectors.Vector3D(-10, 10, -5)

    print(temp_r.cross_mag(temp_v))
    print(temp_r.cross_prod(temp_v))
    print(temp_r.cross_prod(temp_v).magnitude())
    print((180 / np.pi)*calc_inclination(temp_r.cross_prod(temp_v)))
