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

        self.surface = pygame.Surface((20, 20))

    def seeking(self, targetvector):
        ''''Runs the seeking behavior'''
        self._velocity = Vector.normal(targetvector - self.position) * self.maxvelocity
        self._headed = Vector.normal(self._velocity)
        return self._force

    def fleeing(self, targetvector):
        '''Runs the fleeing behavior'''
        self._velocity = Vector.normal(targetvector - self.position) * self.maxvelocity
        self._headed = Vector.normal(self._velocity)
        return self._force * -1

    def wondering(self, distance, radius):
        '''Runs the wondering behavior'''
        center_circle = Vector.normal(self._velocity)
        center_circle = center_circle * distance
        displacement = Vector([0, 1]) * radius
        self._wanderangle = self._wanderangle + (random.randrange(0.0, 1.0)*1) - (1*.5)
        displacement.xpos = math.cos(self._wanderangle)* Vector.mag(displacement)
        displacement.ypos = math.sin(self._wanderangle)* Vector.mag(displacement)
        wanderforce = center_circle + displacement
        return wanderforce

    def add_force(self, force, deltatime):
        '''adds force'''
        force = force * 5
        acceleration = force * (1 / self._mass)
        self._force = acceleration * self._mass
        self._velocity = acceleration * deltatime
        self._forward = self._headed
        if self._velocity.magnitude > 20:
            self._velocity = self._velocity * (1 / 20)
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
        firstagent.seeking(goal, delta_time)
        firstagent.position.print_info()
