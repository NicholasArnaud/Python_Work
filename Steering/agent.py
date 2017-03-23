'''Agent nodes'''
from mathlib import vector

class agent(object):
    '''Agent class'''
    def __init__(self, maxvelocity, start):
        self.maxvelocity = maxvelocity #scalar
        self.currentvelocity = None #vector
        self.position = start


    def steering(self, targetvector):
        ''''Runs the steering behavior'''
        selfcreatedvector = vector(targetvector[0], targetvector[1])
        setvelocity = selfcreatedvector - self.position
        setvelocity.normal()
        setvelocity.scalarmult(self.maxvelocity)
        steering = setvelocity - self.currentvelocity
        return steering

    def head(self, velocity):
        '''Drives agent which way to go'''
        heading = self.maxvelocity/velocity
        return heading
