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
        self._headed = Vector([0, -1])
        self._forward = self._headed
        if self._velocity.magnitude > 20:
            self._velocity = self._velocity * (1 / 20)

    def seeking(self, targetvector, deltatime):
        ''''Runs the seeking behavior'''
        selfcreatedvector = targetvector - self._position
        self._velocity = Vector.normal(self._position - selfcreatedvector) * self.maxvelocity
        self._force = self._velocity - self.currentvelocity
        self._velocity += self._force * deltatime
        self._position += self._velocity * deltatime
        self._headed = Vector.normal(self._velocity)

        #follows the real world laws
        self._force = self._force * deltatime
        self._acceleration = self._force * (1 / self._mass)
        self._velocity = self.currentvelocity + self._force * deltatime
        self._direction = self._headed
        self._forward = self._direction
        if self._velocity.magnitude > 20:
            self._velocity = self._velocity * (1 / 20)

        seek = self._velocity - self.currentvelocity
        return seek


    def print_position(self):
        '''prints position'''
        return str(self._position)

if __name__ == "__main__":
    pygame.init()
    c = pygame.time.Clock()
    starter = Vector([5, 5])
    goal = Vector([15, 15])
    firstagent = agent(5, starter)

    while firstagent.currentvelocity != firstagent.maxvelocity:
        milliseconds = c.tick(10)
        deltatime = milliseconds / 1000
        print(milliseconds)
        firstagent.currentvelocity += firstagent.seeking(goal, deltatime)
