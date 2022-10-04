import numpy as np
import pygame
import math
from helper import constants, methods


class Stone:
    """Class for creating and using stone in game."""
    def __init__(self, screen, color):
        """
        Parameterized constructor.
        :param screen:  Surface where stone is drawn.
        :param color: Stone's color.
        """
        self.screen = screen
        self.color = color
        self.x = 250
        self.y = 650
        self.position = np.array([self.x, self.y])

        self.angle = 0
        self.rk4n = np.zeros(100)
        self.rk4n_velocity = np.zeros((200,2))
        self.velocity = np.zeros(2, dtype=object)
        self.iteration = 0

        self.hitX = 0
        self.hitY = 0
        self.hitB = 0
        self.change = False
        self.shot = False

    def draw(self):
        self.x = self.x + self.velocity[0] * 0.01 * 17  # velocity is being multiplied due to ratio between meters and pixels
        self.y = self.y + self.velocity[1] * 0.01 * 17
        self.position = np.array([self.x, self.y])
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), constants.radius)

    def update(self):
        """
        Method assignes new value of velocity if the stone is moving.
        If not, all atributtes attached to movements are being reseted to zero values.
        """
        if self.iteration < len(self.rk4n) and self.change:
            v = self.rk4n_velocity[self.iteration]
            if self.hitX == 1 or self.hitY == 1:
                self.velocity = np.array([0.01, 0.01])
                if self.hitX == 1:
                    self.hitX = 0
                if self.hitY == 1:
                    self.hitY = 0
            elif self.rk4n[self.iteration] > 0:
                self.velocity = np.array([v[0], v[1]])
            self.iteration += 1
        else:
            self.iteration = 0
            self.angle = 0
            self.velocity = np.zeros(2)
            self.change = False
            self.hitX = 0
            self.hitY = 0
            self.hitB = 0

    def distance(self, stone):
        """
        Method calculates distance between current's and other's stone center.
        :return: (float) Distance between current's and other's stone center.
        """
        distance = stone.position - self.position
        return np.hypot(*distance)

    def center_distance(self):
        """
        Method calculates distance between stone's and home's center.
        :return: (float) Distance between stone's and home's center.
        """
        distance = self.position - constants.center
        return np.hypot(*distance)

    def wall_collision(self):
        """
        Method checks and reacts to collision between stone and wall.
        """
        if self.y > constants.game_screen_h - 10 - constants.radius or self.y < constants.radius:
            self.hitY = 1
            if self.y > 720 - constants.radius:
                self.y -= 6
            if self.y < constants.radius:
                self.y += 6
            for i in range(self.iteration, len(self.rk4n)):
                self.rk4n_velocity[i] = [self.rk4n_velocity[i][0], self.rk4n_velocity[i][1] * (-1)]

    def stone_collision(self, stone):
        """
        Method checks and reacts to collision between stone and wall.
        :param stone: Stone with which we check for collision.
        """
        if 2 * constants.radius >= self.distance(stone) and self.hitB == 0:
            stone_dist = stone.position - self.position
            distance = np.hypot(*stone_dist)
            coef = stone_dist / distance   # calculate unit vector
            stone1_dot = np.dot(self.velocity, coef)
            stone2_dot = np.dot(stone.velocity, coef)
            self.velocity += (stone2_dot - stone1_dot) * coef  # calculate new velocity
            angle = math.atan2(self.velocity[1], self.velocity[0])  # calculate direction's of movement angle
            self.initial_force(angle, np.hypot(*self.velocity))  # start new movement of the stone
            stone.velocity += (stone1_dot - stone2_dot) * coef
            angle = math.atan2(stone.velocity[1], stone.velocity[0])
            stone.initial_force(angle, np.hypot(*stone.velocity))

    def initial_force(self, angle, v = 7):
        """
        Method assignes list of velocity values through current movement.
        :param angle: Angle of movement.
        :param v: Initial velocity.
        """
        self.angle = angle
        self.rk4n = self.calculate_velocity(v)
        self.rk4n_velocity = np.zeros((len(self.rk4n),2))
        for i in range(len(self.rk4n)):
            self.rk4n_velocity[i] = [self.rk4n[i]*math.cos(angle), self.rk4n[i]*math.sin(angle)]
        self.change = True
        self.iteration = 0

    def calculate_velocity(self, v):
        """
        Method calculates velocity values for every moment.
        :param v: Initial value of velocity.
        :return: (list) Velocity values through every moment.
        """
        v0T = v
        F = constants.mi * constants.mass * constants.gravity
        m = constants.mass
        dvT = lambda *args: -F / m
        nv0T = np.array([v0T])
        ta = 0
        tb = 30
        h = (tb - ta) / 1000
        f_x_rk4 = methods.rk4n(ta, tb, h, nv0T, dvT)
        return f_x_rk4