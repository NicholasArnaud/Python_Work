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
        self._wanderangle = 0
        self._displacement = Vector([0, 1])
        self.acceleration = self._force * (1 / self._mass)

        self.surface = pygame.Surface((20, 20))


    def seeking(self, targetvector):
        ''''Runs the seeking behavior'''
        self._displacement = targetvector - self.position
        self._force = Vector.normal(self._displacement) * self.maxvelocity
        self._headed = self._force - self._velocity
        return self._headed

    def fleeing(self, targetvector):
        '''Runs the fleeing behavior'''
        self._displacement = targetvector - self.position
        self._force = Vector.normal(self._displacement) * self.maxvelocity * -1
        self._headed = self._force - self._velocity
        return self._headed

    def wondering(self, distance, radius):
        '''Runs the wondering behavior'''
        center_circle = Vector.normal(self._velocity)
        center_circle = center_circle * distance
        self._displacement = Vector.normal(self._velocity)
        self._displacement = Vector([0, 1]) * radius
        self._wanderangle += (random.randrange(0.0, 1.0)*1.0) - (1.0*.5)
        self._displacement.xpos = math.cos(self._wanderangle)* Vector.mag(self._displacement)
        self._displacement.ypos = math.sin(self._wanderangle)* Vector.mag(self._displacement)
        self._headed = center_circle + self._displacement
        return self._headed

    def update_force(self, deltatime):
        '''adds force'''
        self._force = self._force * 5
        self.acceleration = self._force
        self._velocity += self.acceleration * deltatime
        if Vector.mag(self._velocity) > self.maxvelocity:
            self._velocity = Vector.normal(self._velocity) * self.maxvelocity
        self.position += self._velocity * deltatime
        return self

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
        firstagent.seeking(goal)
        firstagent.position.print_info()
