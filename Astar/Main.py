'''Entry Point'''

import Astar
from Graph import Graph
from Node import Node

start_node = Node(1, 1)
end_node = Node(5, 8)
graph = Graph([10, 10])

Astar.algorithm(start_node, end_node, graph)
