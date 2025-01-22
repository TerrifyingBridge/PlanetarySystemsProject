from Helpers import vectors as v
from Helpers import constants
from Helpers import orbital_elements as oe
from Helpers import constants as c
import numpy as np


class AstroBody:
    def __init__(self, mass: float, radius: float):
        self.mass = mass
        self.radius = radius
        self.position = v.Vector3D(0, 0, 0)


class TwoBodySystem:
    def __init__(self, body1: AstroBody, body2: AstroBody, init_sep_dist: float, eccentricity: float,
                 inclination: float, peri: float):
        self.body1 = body1
        self.body2 = body2
        self.eccentricity = eccentricity
        self.inclination = inclination
        self.semi_major_axis = init_sep_dist * constants.PhysicalConstants.au / (1 - self.eccentricity)
        self.period = self.calc_period(init_sep_dist * constants.PhysicalConstants.au)
        self.mean_motion = oe.calc_mean_motion(self.semi_major_axis, int(self.body1.mass + self.body2.mass))
        self.peri = peri

        self.body1_pos_x = []
        self.body1_pos_y = []
        self.body1_pos_z = []
        self.body2_pos_x = []
        self.body2_pos_y = []
        self.body2_pos_z = []
        self.true_anomaly_path = []
        self.eccentric_anomaly_path = []

        self.los_vel = []
        self.transit_x = []
        self.transit_y = []
        self.flux = []
        self.transit_time = []
        self.astrometry_x = []
        self.astrometry_y = []
        self.direct_image_x = []
        self.direct_image_y = []

    def calc_radius_eccentric_anomaly(self, semi_major_axis: float, ecc_anom: float) -> float:
        return semi_major_axis * (1 - self.eccentricity * np.cos(ecc_anom))

    def calc_period(self, init_sep_dist: float) -> float:
        total_mass = self.body1.mass + self.body2.mass
        a = init_sep_dist / (1 - self.eccentricity)
        return 2 * np.pi * np.sqrt(pow(a, 3) / (constants.PhysicalConstants.gravitational_constant * total_mass))

    def calc_los_vel(self, true_anomaly: float) -> float:
        term1 = -1 * self.body2.mass / (self.body1.mass + self.body2.mass)
        term2 = self.mean_motion * self.semi_major_axis / np.sqrt(1 - self.eccentricity ** 2)
        term3 = np.sin(self.inclination) * (np.cos(true_anomaly + self.peri) + self.eccentricity * np.cos(self.peri))
        return term1 * term2 * term3

    def calc_semi_amplitude(self) -> float:
        total_mass = self.body1.mass + self.body2.mass
        term1 = self.body2.mass / total_mass
        term2 = pow(2 * np.pi * constants.PhysicalConstants.gravitational_constant * total_mass / self.period, 1 / 3)
        term3 = np.sin(self.inclination) / np.sqrt(1 - self.eccentricity ** 2)
        return term1 * term2 * term3

    def get_thiele_innes_elements_astrometry(self) -> tuple[float, float, float, float]:
        start_term = self.body2.mass * self.semi_major_axis / (
                self.body1.mass + self.body2.mass)
        A = start_term * np.cos(self.peri)
        B = start_term * np.cos(self.inclination) * np.sin(self.peri)
        F = start_term * -1 * np.sin(self.peri)
        G = start_term * np.cos(self.inclination) * np.cos(self.peri)

        return A, B, F, G

    def get_thiele_innes_elements_direct_images(self) -> tuple[float, float, float, float]:
        A = self.semi_major_axis * np.cos(self.peri)
        B = self.semi_major_axis * np.cos(self.inclination) * np.sin(self.peri)
        F = -self.semi_major_axis * np.sin(self.peri)
        G = self.semi_major_axis * np.cos(self.inclination) * np.cos(self.peri)

        return A, B, F, G

    def get_transit_intersection(self, x1: float, y1: float, x2: float, y2: float) -> float:
        r1 = self.body1.radius * 1000
        r2 = self.body2.radius * 1000
        dist = np.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) * c.PhysicalConstants.au
        if (dist >= r1 + r2):
            return 0.0
        elif (dist <= np.abs(r1 - r2)):
            return r2 * r2 * np.pi
        else:
            term1 = pow(r1, 2) * np.arccos((dist * dist + r1 * r1 - r2 * r2) / (2 * dist * r1))
            term2 = pow(r2, 2) * np.arccos((dist * dist + r2 * r2 - r1 * r1) / (2 * dist * r2))
            term3 = 0.5 * np.sqrt(pow(2 * r2 * dist, 2) - pow(dist * dist + r2 * r2 - r1 * r1, 2))
            return term1 + term2 - term3

    def au_to_star_rad(self, dist: float) -> float:
        return (dist * c.PhysicalConstants.au) / (self.body1.radius*1000)

    def fill_los_vel(self) -> None:
        for angle in self.true_anomaly_path:
            self.los_vel.append(self.calc_los_vel(angle))

    def fill_temp_transit(self, time: np.ndarray) -> list[int]:
        temp_transit = []
        temp = []
        consec = 0
        for i in range(len(self.body2_pos_x)):
            x = self.body2_pos_x[i] * c.PhysicalConstants.au
            y = self.body2_pos_y[i] * c.PhysicalConstants.au
            z = self.body2_pos_z[i]
            r_planet = self.body2.radius
            r_star = self.body1.radius
            if x ** 2 + y ** 2 <= (r_planet * 1000 + r_star * 1000) ** 2 and z >= 0:
                consec += 1
                temp.append(i)
                if (i == len(self.body2_pos_x) - 1):
                    temp_transit.append(temp)
            else:
                if (consec != 0):
                    temp_transit.append(temp)
                    temp = []
                consec = 0
        if len(temp_transit) == 2:
            if (temp_transit[0][0] < temp_transit[1][0]):
                second_list = temp_transit[1].copy()
                temp_transit.pop(1)
                temp_transit.insert(0, second_list)
            temp_transit = temp_transit[0] + temp_transit[1]
        elif (len(temp_transit) == 1):
            temp_transit = temp_transit[0]
        return temp_transit

    def fill_transit(self, time: np.ndarray) -> None:
        temp_transit = self.fill_temp_transit(time)
        for index in temp_transit:
            self.transit_x.append(self.body2_pos_x[index])
            self.transit_y.append(self.body2_pos_y[index])
            area_of_star = pow(self.body1.radius * 1000, 2) * np.pi
            area_of_intersect = self.get_transit_intersection(self.body1_pos_x[index], self.body1_pos_y[index],
                                                              self.body2_pos_x[index], self.body2_pos_y[index])
            self.flux.append(1 - area_of_intersect / area_of_star)
            self.transit_time.append(time[index])

    def fill_astrometry(self) -> None:
        A, B, F, G = self.get_thiele_innes_elements_astrometry()
        for true_anom in self.true_anomaly_path:
            start_term = (1 - self.eccentricity ** 2) / (1 + self.eccentricity * np.cos(true_anom))
            temp_x = -start_term * (A * np.cos(true_anom) + F * np.sin(true_anom))
            temp_y = -start_term * (B * np.cos(true_anom) + G * np.sin(true_anom))

            self.astrometry_x.append(temp_x)
            self.astrometry_y.append(temp_y)

    def fill_direct_image(self) -> None:
        A, B, F, G = self.get_thiele_innes_elements_direct_images()
        for ecc_anom in self.eccentric_anomaly_path:
            temp_x = A * (np.cos(ecc_anom) - self.eccentricity) + F * np.sqrt(1 - self.eccentricity ** 2) * np.sin(
                ecc_anom)
            temp_y = B * (np.cos(ecc_anom) - self.eccentricity) + G * np.sqrt(1 - self.eccentricity ** 2) * np.sin(
                ecc_anom)

            self.direct_image_x.append(temp_x)
            self.direct_image_y.append(temp_y)

    def fill_path_list(self, time: np.ndarray) -> None:
        total_mass = self.body1.mass + self.body2.mass
        for step in time:
            mean_anomaly = oe.calc_mean_anomaly(0, self.mean_motion, step)
            eccentric_anomaly = oe.calc_eccentric_anomaly(mean_anomaly, self.eccentricity, 1e-10)
            self.eccentric_anomaly_path.append(eccentric_anomaly)
            true_anomaly = oe.calc_true_anomaly(self.eccentricity, eccentric_anomaly)
            self.true_anomaly_path.append(true_anomaly)
            current_sep = self.calc_radius_eccentric_anomaly(self.semi_major_axis, eccentric_anomaly)

            current_pos = v.Vector3D(np.cos(true_anomaly + self.peri),
                                     np.cos(self.inclination) * np.sin(true_anomaly + self.peri),
                                     np.sin(self.inclination) * np.sin(true_anomaly + self.peri))
            current_pos.multiply(current_sep)

            body1_pos = v.Vector3D.multiply_scalar(current_pos,
                                                   -1 * self.body2.mass / (total_mass * constants.PhysicalConstants.au))
            body2_pos = v.Vector3D.multiply_scalar(current_pos,
                                                   self.body1.mass / (total_mass * constants.PhysicalConstants.au))

            self.body1_pos_x.append(body1_pos.x)
            self.body1_pos_y.append(body1_pos.y)
            self.body1_pos_z.append(body1_pos.z)
            self.body2_pos_x.append(body2_pos.x)
            self.body2_pos_y.append(body2_pos.y)
            self.body2_pos_z.append(body2_pos.z)
