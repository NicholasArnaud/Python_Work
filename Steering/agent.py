'''Agent nodes'''
from mathlib import vector

class agent(object):
    '''Agent class'''
    def __init__(self, maxvelocity, vector):
        self.maxvelocity = maxvelocity #scalar
        self.currentvelocity = None #vector
        self.position = vector
        self.heading


    def steering(self, targetvector):
        ''''Runs the steering behavior'''
        selfcreatedvector = vector(targetvector[0], targetvector[1])
        if targetvector[0] == 0 or targetvector[1] == 0:
            selfcreatedvector += vector(1, 1)
            setvelocity = (self.position.normal() - selfcreatedvector.normal()) * self.maxvelocity
        else:
            setvelocity = (self.position.normal() - selfcreatedvector.normal()) * self.maxvelocity
        steering = setvelocity - self.currentvelocity
        return steering

    def head(self, velocity):
        '''Drives agent which way to go'''
        self.heading = self.maxvelocity/velocity
        return self.heading
