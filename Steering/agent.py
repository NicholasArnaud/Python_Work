'''Agent nodes'''
from mathlib import vector

class agent(object):
    '''Agent class'''
    def __init__(self, maxvelocity, start):
        self.maxvelocity = maxvelocity #scalar
        self.currentvelocity = vector([0, 0]) #vector
        self.position = start
        self.velocity = vector([0, 0])


    def seeking(self, targetvector):
        ''''Runs the seeking behavior'''
        selfcreatedvector = targetvector - self.position
        self.velocity = vector([(selfcreatedvector.xpos - self.position.xpos),
                                (selfcreatedvector.ypos - self.position.ypos)])
        dif = (vector.normal(targetvector) - vector.normal(self.currentvelocity))
        self.velocity = vector.scalarmult(dif, self.maxvelocity)
        self.velocity.print_info()
        seek = self.velocity - self.currentvelocity
        return seek

    def head(self, velocity):
        '''Drives agent which way to go'''
        heading = self.maxvelocity/velocity
        return heading

    def add_force(self, deltatime):
        self.position += self.currentvelocity * deltatime


    def print_info(self):
        '''prints position'''
        return self.position

if __name__ == "__main__":
    starter = vector([5, 5])
    goal = vector([15, 15])
    firstagent = agent(5, starter)
    while firstagent.currentvelocity != firstagent.maxvelocity:
        firstagent.currentvelocity += firstagent.seeking(goal)
        firstagent.print_info()
