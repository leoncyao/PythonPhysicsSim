"""Class For Circular Objects"""
from Tools import find_angle
import math

import pygame
g = 6.67 * 10 ** -11

class Obj:
    """
    a
    """
    def __init__(self, colour: tuple, mass: int, pos: tuple, vel: tuple, rad: int):
        """
        input as a tuple, store as an int to make mutating easier
        """
        self.colour = colour
        self.mass = mass
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.vel_x = vel[0]
        self.vel_y = vel[1]
        self.rad = rad
        self.acel_x = 0
        self.acel_y = 0
        self.dynamic = True
        self.forces = []

    def update_pos(self, t):
        """
        a
        """
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def update_vel(self, t):
        """
        a
        """

        self.vel_x += self.acel_x
        self.vel_y += self.acel_y

        # for reflection against walls
        # if 0 >= self.pos_x or self.pos_x >= display_width:
        #     self.vel_x *= -1
        # if 0 >= self.pos_y or self.pos_y >= display_height:
        #     self.vel_y *= -1

    def update_acel(self, t):
        """
        a
        """
        for force in self.forces:
            angle = force[0]
            mag = force[1] / self.mass
            self.acel_x = math.cos(angle) * mag
            self.acel_y = math.sin(angle) * mag

    def update_grav(self, objects):
        """
        calculates gravity for all other objects
        """
        # print("for obj {}".format(id(self)))
        for obj in objects:
            # print("id obj {}".format((id(obj))))
            if obj is not self:
                self.forces.append(self.calc_grav(obj))

    def calc_grav(self, other: 'Obj'):
        """
        assume other is the origin
        :param other:
        :type other:
        :return:
        :rtype:
        """

        dist_x = self.pos_x - other.pos_x
        dist_y = self.pos_y - other.pos_y

        total_dist = math.sqrt(math.pow(dist_x, 2) + math.pow(dist_y, 2))

        if total_dist == 0:
            total_dist = 1

        force = self.mass * other.mass / total_dist  # * g
        angle = find_angle(self.pos_x, self.pos_y, other.pos_x, other.pos_y)
        # print("obj 1 (origin) {} {} obj 2 {} {}".format(other.pos_x, other.pos_y))
        return (angle, force)

    def draw(self, display):
        """:arg"""
        pygame.draw.circle(display, self.colour, (int(self.pos_x), int(self.pos_y)), self.rad)

    def get_velocity(self):
        """gets velocity magnitude"""
        vel = math.sqrt(math.pow(self.vel_x, 2) + math.pow(self.vel_y, 2))
        return vel

    def update_stats(self, objects):
        """
        :return:
        :rtype:
        """
        if self.mass != 3 or True:
            self.update_pos(1)
            self.update_vel(1)
            self.update_acel(1)
            self.forces = []
            if self.dynamic:
                self.update_grav(objects)
#
# class Plank(Obj):
#     """Plank Class"""

