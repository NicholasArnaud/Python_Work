'''main file'''
from mathlib import vector

def testvector(vector1, vector2):
    '''tests vector class'''
    vector3 = vector1 + vector2
    vector3 = vector1 - vector2
    vector1.mag()
    vector1.normal()
    vectortest = vector1.scalarmult(2)
    vectortest.print_info()

if __name__ == "__main__":
    vectora = vector(2, 2)
    vectorb = vector(1, 1)
    testvector(vectora, vectorb)
