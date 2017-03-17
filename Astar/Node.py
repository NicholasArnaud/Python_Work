'''Node creator'''

class Node(object):
    '''Creates Nodes '''
    def __init__(self, xposition, yposition):
        '''Node Constuctor'''
        self.xpos = xposition
        self.ypos = yposition
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.adjacents = []

    def neighbors(self, node, graph):
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
