'''Main file '''

from astar import AStar
from Graph import Graph
from game import Game

def test_nodes():
    '''test the nodes'''
    astar = AStar()
    __graph__ = Graph([10, 10])
    __node__ = __graph__.get_node([1, 1])
    __node2__ = __graph__.get_node([5, 5])
    astar.astaralgorithm(__node__, __node2__, __graph__)
    start = Game([__graph__])
    start.drawscreen([__graph__])


if __name__ == '__main__':
    test_nodes()
