'''Vector math'''


def Mag():
    return sqrt((x * x) + (y*y))

def Normal():
    '''normalizes a vector'''
    tmp = Vector2D(x / Mag(), y / Mag())
    return tmp


def dotprod(avector):
    '''gets the dot product'''
    return (x *avector.x) + (y*avector.y)
