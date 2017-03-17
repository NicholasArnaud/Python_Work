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
                nodekey = str(i) + "," + str(k)
                self.nodes[nodekey] = Node([i, k], len(self.nodes))

    def get_node(self, node):
        '''Gets the node'''
        nodekey = str(node[0]) + ',' + str(node[1])
        if nodekey in self.nodes:
            return self.nodes[nodekey]


    def get_neighbors(self, node, graph):
        '''Looks for the node's neighbors'''
        right = [1, 0]
        top = [0, 1]
        left = [-1, 0]
        down = [0, -1]
        dirs = [right, top, left, down]
        neighbors = []
        for i in dirs:
            item1 = i[0] + node.value[0]
            item2 = i[1] + node.value[1]
            fetch_node = graph.get_node([item1, item2])
            if fetch_node:
                neighbors.append(fetch_node)
        return neighbors


def test_graph(graph):
    '''abc'''
    node = graph.get_node([1, 1])
    node.print_info()
    neighbors = graph.get_neighbors(node, graph)
    for neighbor in neighbors:
        neighbor.print_info()


if __name__ == "__main__":
    test_graph(Graph([3, 3]))
