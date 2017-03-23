'''Vector math'''
import math
class vector(object):
    '''2D vector'''
    def __init__(self, posx, posy):
        self.xpos = posx
        self.ypos = posy
        self.normalized = None
        self.magnitude = None


    def __add__(self, other):
        add = vector
        add.xpos = self.xpos + other.xpos
        add.ypos = self.ypos + other.ypos
        return add

    def __sub__(self, other):
        sub = vector
        sub.xpos = self.xpos - other.xpos
        sub.ypos = self.ypos - other.ypos
        return sub

    def __mul__(self, other):
        mult = vector
        mult.x = self.xpos * other.xpos
        mult.y = self.ypos * other.ypos
        return mult

    def __eq__(self, other):
        if self.xpos == other.xpos and self.ypos == other.ypos:
            return True
        return False

    def scalarmult(self, scal):
        '''multiplies a vector by a scalar'''
        tmp = vector(self.xpos * scal, self.ypos * scal)
        return tmp

    def mag(self):
        '''gets the magnitude of a vector'''
        self.magnitude = float(math.sqrt((self.xpos * self.xpos) + (self.ypos * self.ypos)))
        return self.magnitude

    def normal(self):
        '''normalizes a vector'''
        self.normalized = vector(self.xpos / self.mag(), self.ypos / self.mag())
        return self.normalized

    def dotprod(self, avector):
        '''gets the dot product'''
        return float((self.xpos * avector.xpos) + (self.ypos * avector.ypos))

    def print_info(self):
        '''Prints vector coordinates'''
        print(str(self.xpos), str(self.ypos))
        