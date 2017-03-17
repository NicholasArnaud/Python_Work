'''Entry Point'''

from Node import Node
from Graph import Graph
import Astar

start_node = Node(1, 1)
end_node = Node(5, 8)
graph = Graph([10, 10])

Astar.algorithm(start_node, end_node)
