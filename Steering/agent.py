'''Agent nodes'''
import pygame
import math
from constants import *
import random
from mathlib import Vector


class agent(object):
    '''Agent class'''
    def __init__(self, maxvelocity, start):


        self.maxvelocity = maxvelocity #scalar
        self.currentvelocity = Vector([0, 0]) #Vector
        self._velocity = Vector([0, -1])
        self.position = start
        self._mass = 1
        self._force = Vector([1, 1])
        self._headed = Vector([0, 1])
        self._forward = self._headed

        self.surface = pygame.Surface((600, 500))

    def seeking(self, targetvector, deltatime):
        ''''Runs the seeking behavior'''
        self._velocity = Vector.normal(targetvector - self.position) * self.maxvelocity
        self._force = self._velocity - self.currentvelocity
        self._velocity += self._force * deltatime
        self.position += self._velocity * deltatime
        return self

    def fleeing(self, targetvector, delt):
        '''Runs the fleeing behavior'''
        self._velocity = Vector.normal(targetvector - self.position) * self.maxvelocity
        self._force = self._velocity - self.currentvelocity
        self._velocity += self._force * delt
        self.position -= self._velocity * delt
        return self

    def wondering(self, distance, radius):
        '''Runs the wondering behavior'''
        center_circle = self._velocity.normal(self._velocity)
        center_circle = center_circle * distance
        displacement = Vector([0, 1]) * radius
        wanderangle = (random.Random()*1) - (1*.5)
        self.position.xpos = math.cos(wanderangle)* displacement.mag(displacement)
        self.position.ypos = math.sin(wanderangle)* displacement.mag(displacement)

    def add_force(self):
        '''adds force'''
        self._force = self._force * delta_time
        acceleration = self._force * (1 / self._mass)
        self._velocity = self.currentvelocity + self._force * delta_time
        self._forward = self._headed
        if self._velocity.magnitude > 20:
            self._velocity = self._velocity * (1 / 20)
        return self._force

    def draw(self, surface, color):
        '''draws agent when called'''
        pointlist = [(self.position.xpos + 5, self.position.ypos),
                     (self.position.xpos, self.position.ypos - 10),
                     (self.position.xpos - 5, self.position.ypos)]
        self.surface.blit(surface, (int(self.position.xpos), int(self.position.ypos)))
        pygame.draw.polygon(surface, color, pointlist, 2)

if __name__ == "__main__":
    pygame.init()
    c = pygame.time.Clock()
    starter = Vector([1, 0])
    goal = Vector([1, 1])
    firstagent = agent(5, starter)

    while firstagent.position != goal:
        delta_time = c.tick(3) / 1000.0
        firstagent.seeking(goal, delta_time)
        firstagent.position.print_info()
