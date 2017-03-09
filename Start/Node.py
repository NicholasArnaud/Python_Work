'''Node creator'''


class Node(object):
    '''Creates Nodes '''
    def __init__(self, idee, val):
        '''Node Constuctor'''
        self.ide = idee
        self.val = val

    def print_info(self):
        '''prints info'''
        print "ID:", self.ide, "Value: ", self.val

    @property
    def value(self):
        '''gets value'''
        return self.val

    @property
    def ident(self):
        '''gets id'''
        return self.ide
