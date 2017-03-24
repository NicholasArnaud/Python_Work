'''Vector math'''
import math
class vector(object):
    '''2D vector'''
    def __init__(self, posxy):
        self.xpos = posxy[0]
        self.ypos = posxy[1]


    def __add__(self, other):
        add = vector
        add.xpos = self.xpos + other.xpos
        add.ypos = self.ypos + other.ypos
        return add

    def __iadd__(self, other):
        self.xpos += other.xpos
        self.ypos += other.ypos
        return self

    def __sub__(self, other):
        sub = vector
        sub.xpos = self.xpos - other.xpos
        sub.ypos = self.ypos - other.ypos
        return sub

    def __mul__(self, other):
        '''multiply a vector by a scalar value'''
        tmp0 = other * self.xpos
        tmp1 = other * self.ypos
        return vector([tmp0, tmp1])

    def __eq__(self, other):
        if self.xpos == other.xpos and self.ypos == other.ypos:
            return True
        return False

    @staticmethod
    def scalarmult(vec, scal):
        '''multiplies a vector by a scalar'''
        tmp = vector([(vec.xpos * scal), (vec.ypos * scal)])
        return tmp
    @staticmethod
    def mag(vec):
        '''gets the magnitude of a vector'''
        return float(math.sqrt((vec.xpos * vec.xpos) + (vec.ypos * vec.ypos)))

    @staticmethod
    def normal(vec):
        '''normalizes a vector'''
        if vector.mag(vec) == 0:
            return vector([vec.xpos / (1), vec.ypos / (1)])
        return vector([vec.xpos / vec.mag(vec), vec.ypos / vec.mag(vec)])

    def dotprod(self, avector):
        '''gets the dot product'''
        return float((self.xpos * avector.xpos) + (self.ypos * avector.ypos))

    def print_info(self):
        '''Prints vector coordinates'''
        print(str(self.xpos), str(self.ypos))
        