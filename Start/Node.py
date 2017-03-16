'''Node creator'''


class Node(object):
    '''Creates Nodes '''
    def __init__(self, val, idee):
        '''Node Constuctor'''
        self.__ide = idee
        self.__val = val
        self.adjacents = []

    def print_info(self):
        '''prints info'''
        print("ID:", self.__ide, "Value:", self.__val)

    @property
    def value(self):
        '''gets value'''
        return self.__val

    @property
    def ident(self):
        '''gets id'''
        return self.__ide

    @property
    def adjacents(self):
        return self.adjacents

    def get_neighbors(self, node, graph):
        '''Looks for the node's neighbors'''
        right = [1, 0]
        top = [0, 1]
        left = [-1, 0]
        down = [0, -1]
        dirs = [right, top, left, down]
        for i in dirs:
            nodekey = node.value[0] + i[0], node.value[1] + i[1]
            if graph.get_node(nodekey) is not None:
                self.adjacents.append(graph.get_node(nodekey))
        return self.adjacents
