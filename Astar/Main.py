'''Entry Point'''

import Astar
from Graph import Graph
#from Node import Node

graph = Graph([7, 7])

startnode = graph.nodelist[1]
endnode = graph.nodelist[46]
Astar.algorithm(startnode, endnode, graph)
