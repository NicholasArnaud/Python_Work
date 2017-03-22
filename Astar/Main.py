'''Entry Point'''

import Astar
from Graph import Graph
#from Node import Node

graph = Graph([5, 5])

startnode = graph.nodelist[1]
endnode = graph.nodelist[16]
Astar.algorithm(startnode, endnode, graph)
