'''Main file '''

import astar
from Graph import Graph

__star__ = astar

def test_nodes():
    '''test the nodes'''
    graph = Graph([5, 5])
    node = graph.get_node([2, 1])
    node.print_info()
    neighbors = node.get_neighbors(node, graph)
    for nna in neighbors:
        nna.print_info()


if __name__ == '__main__':
    test_nodes()
