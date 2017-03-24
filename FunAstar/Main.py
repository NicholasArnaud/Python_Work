'''Entry Point'''

import Astar
from Graph import Graph
#from Node import Node

graph = Graph([6, 6])

startnode = graph.nodelist[1]
endnode = graph.nodelist[35]

graph.nodelist[14].walkable = False
graph.nodelist[28].walkable = False
graph.nodelist[29].walkable = False
Astar.algorithm(startnode, endnode, graph)
