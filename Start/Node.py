'''Node creator'''


class Node(object):
    '''Creates Nodes '''
    def __init__(self, val, idee):
        '''Node Constuctor'''
        self.__ide = idee
        self.__val = val

    def print_info(self):
        '''prints info'''
        print "ID:", self.__ide, "Value:", self.__val

    @property
    def value(self):
        '''gets value'''
        return self.__val

    @property
    def ident(self):
        '''gets id'''
        return self.__ide
