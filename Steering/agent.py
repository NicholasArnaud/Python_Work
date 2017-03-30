'''Agent nodes'''
import pygame
import random
from mathlib import Vector


class agent(object):
    '''Agent class'''
    def __init__(self, maxvelocity, start):


        self.maxvelocity = maxvelocity #scalar
        self.currentvelocity = Vector([0, 0]) #Vector
        self._velocity = Vector([0, -1])
        self._position = start
        self._mass = 1
        self._force = Vector([1, 1])
        self._headed = Vector([0, 1])
        self._forward = self._headed
        if self._velocity.magnitude > 20:
            self._velocity = self._velocity * (1 / 20)

    def seeking(self, targetvector, deltatime):
        ''''Runs the seeking behavior'''
        self._velocity = Vector.normal(targetvector - self._position) * self.maxvelocity
        self._force = self._velocity - self.currentvelocity
        self._velocity += self._force * deltatime
        self._position += self._velocity * deltatime
        return self

    def fleeing(self, targetvector, delt):
        '''Runs the fleeing behavior'''
        return self.seeking(targetvector, delt) * -1


    def add_force(self):
        '''adds force'''
        self._force = self._force * delta_time
        acceleration = self._force * (1 / self._mass)
        self._velocity = self.currentvelocity + self._force * delta_time
        self._forward = self._headed
        if self._velocity.magnitude > 20:
            self._velocity = self._velocity * (1 / 20)
        return self._force


if __name__ == "__main__":
    pygame.init()
    c = pygame.time.Clock()
    starter = Vector([400, 400])
    goal = Vector([500, 600])
    firstagent = agent(5, starter)

    while firstagent._position != goal:
        delta_time = c.tick(3) / 1000.0
        firstagent.seeking(goal, delta_time)
        firstagent._position.print_info()
