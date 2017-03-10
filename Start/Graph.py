'''Graph creator'''
from Node import Node


class Graph(object):
    '''Graph constructor'''

    def __init__(self, dims):
        self.width = dims[0]
        self.height = dims[1]
        self.nodes = {}
        for i in range(0, self.width):
            for k in range(0, self.height):
                nodekey = str(i), ",", str(k)
                self.nodes[nodekey] = Node([i, k], len(self.nodes))

    def get_node(self, node):
        '''Gets the node'''
        nodekey = str(node[0]), ',', str(node[1])
        if nodekey in self.nodes:
            return self.nodes[nodekey]
        return None

    def passable(self, _id):
        '''checks if node can go through area'''
        return _id not in self.in_boundary(_id)

    def in_boundary(self, _id):
        '''checks if node is in grid'''
        return 0 <= _id.ide[0] < self.width and 0 <= _id.ide[1] < self.height
