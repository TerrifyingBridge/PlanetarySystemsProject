from Helpers import vectors as v
from Helpers import constants
from Helpers import orbital_elements as oe
import numpy as np


class AstroBody:
    def __init__(self, mass: float, radius: float):
        self.mass = mass
        self.radius = radius
        self.position = v.Vector2D(0, 0)


class TwoBodySystem:
    def __init__(self, body1: AstroBody, body2: AstroBody, init_sep_dist: float, eccentricity: float, inclination: float):
        self.body1 = body1
        self.body2 = body2
        self.eccentricity = eccentricity
        self.inclination = inclination
        self.semi_major_axis = init_sep_dist * constants.PhysicalConstants.au / (1 - self.eccentricity)
        self.period = self.calc_period(init_sep_dist * constants.PhysicalConstants.au)
        self.mean_motion = oe.calc_mean_motion(self.semi_major_axis, int(self.body1.mass + self.body2.mass))

        self.body1_pos_x = []
        self.body1_pos_y = []
        self.body2_pos_x = []
        self.body2_pos_y = []
        self.true_anomaly_path = []

    def calc_radius_eccentric_anomaly(self, semi_major_axis: float, ecc_anom: float) -> float:
        return semi_major_axis * (1 - self.eccentricity * np.cos(ecc_anom))

    def calc_period(self, init_sep_dist: float) -> float:
        total_mass = self.body1.mass + self.body2.mass
        a = init_sep_dist / (1 - self.eccentricity)
        return 2*np.pi * np.sqrt(pow(a, 3) / (constants.PhysicalConstants.gravitational_constant * total_mass))

    def fill_path_list(self, time: np.ndarray):
        total_mass = self.body1.mass + self.body2.mass
        for step in time:
            mean_anomaly = oe.calc_mean_anomaly(0, self.mean_motion, step)
            eccentric_anomaly = oe.calc_eccentric_anomaly(mean_anomaly, self.eccentricity, 1e-10)
            true_anomaly = oe.calc_true_anomaly(self.eccentricity, eccentric_anomaly)
            self.true_anomaly_path.append(true_anomaly)
            current_sep = self.calc_radius_eccentric_anomaly(self.semi_major_axis, eccentric_anomaly)
            current_pos = v.Vector2D(current_sep * np.cos(true_anomaly), current_sep * np.sin(true_anomaly))

            body1_pos = v.Vector2D.multiply_scalar(current_pos, -1 * self.body2.mass / (total_mass * constants.PhysicalConstants.au))
            body2_pos = v.Vector2D.multiply_scalar(current_pos, self.body1.mass / (total_mass * constants.PhysicalConstants.au))

            self.body1_pos_x.append(body1_pos.x)
            self.body1_pos_y.append(body1_pos.y)
            self.body2_pos_x.append(body2_pos.x)
            self.body2_pos_y.append(body2_pos.y)
