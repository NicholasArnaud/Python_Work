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
        self.center_circle = Vector([0, 1])
        self._displacement = Vector([0, 1])
        self.acceleration = self._force * (1 / self._mass)
        self.surface = pygame.Surface((20, 20), pygame.SRCALPHA, 32)
        self._wanderangle = math.pi
        self._prevangle = math.pi
        self.subsurface = self.surface.copy()


    def seeking(self, targetvector):
        ''''Runs the seeking behavior'''
        self._displacement = targetvector - self.position
        self._headed = Vector.normal(self._displacement)
        self._forward = targetvector
        return Vector.normal(self._displacement) * self.maxvelocity

    def fleeing(self, targetvector):
        '''Runs the fleeing behavior'''
        self._displacement = targetvector - self.position
        self._headed = Vector.normal(self._displacement)
        self._forward = targetvector
        return Vector.normal(self._displacement) * self.maxvelocity * -1

    def wandering(self, distance, radius):
        '''Runs the wondering behavior'''
        self.center_circle = Vector.normal(self._velocity)
        self.center_circle = self.center_circle * distance
        self._displacement = Vector.normal(self._velocity) * radius
        deltaangle = self._prevangle - self._wanderangle
        self._wanderangle += (random.randrange(0.0, 1.0)*deltaangle) - (deltaangle*.5)
        newangle = (random.randrange(0.0, 1.0)*deltaangle) - (deltaangle*.5)
        self._wanderangle += newangle
        self._prevangle = newangle
        self._displacement.xpos = math.cos(self._wanderangle)* Vector.mag(self._displacement)
        self._displacement.ypos = math.sin(self._wanderangle)* Vector.mag(self._displacement)
        self._forward = self.center_circle + self._displacement
        return self.center_circle + self._displacement

    def update_force(self, forced, deltatime):
        '''adds force'''
        self._force = forced * 5
        self.acceleration = self._force
        self._velocity += self.acceleration * deltatime
        if Vector.mag(self._velocity) > self.maxvelocity:
            self._velocity = Vector.normal(self._velocity) * self.maxvelocity
        self._force += Vector.normal(self._velocity)
        self.position += self._velocity * deltatime

    def rotateimage(self, image, angle):
        loc = image.get_rect().center  #rot_image is not defined 
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite

    def draw(self, surface, color):
        '''draws agent when called'''
        pointlist = [(self.position.xpos, self.position.ypos),
                     (self.position.xpos, self.position.ypos + 20),
                     (self.position.xpos + 20, self.position.ypos)]

        angle = math.atan2(self._velocity.ypos, self._velocity.xpos) * 180 / math.pi
        if angle < 0:
            angle = 360 + angle

        self.subsurface = pygame.transform.rotate(surface, -angle)

        self.rotateimage(pygame.draw.polygon(surface, color, pointlist, 2), -angle)

        #pygame.draw.line(surface, GREEN, (self.position.xpos, self.position.ypos),
         #                (self._force.xpos + self.position.xpos,
          #                self._force.ypos + self.position.ypos), 1)

        pygame.draw.line(surface, CYAN, (self.position.xpos, self.position.ypos),
                         (self._velocity.xpos + self.position.xpos,
                          self._velocity.ypos + self.position.ypos), 1)

        #pygame.draw.line(surface, YELLOW, (self.position.xpos, self.position.ypos),
                         #(self._forward.xpos, self._forward.ypos), 1)
        self.subsurface.blit(surface, (int(self.position.xpos), int(self.position.ypos)))
