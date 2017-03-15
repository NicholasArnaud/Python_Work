'''Alorithm for A*'''
from Node import Node
from Graph import Graph

class AStar(object):
	def __init__(self):
		__openlist__ = []
		__closedlist__ = []
		posx = graphnode.value[0]
		posy = graphnode.value[1]
		self.adjacents = []
		self.parent = None
		self.walkable = True
		self.gscore = 0
		self.hscore = 0
		self.fscore = self.gscore + self.hscore

	def get_node(self, node):
    		'''Gets the node'''
        	nodekey = str(node[0]), ',', str(node[1])
        	if nodekey in self._nodes:
            		return self._nodes[nodekey]

	# properties
	@property
	def walkable(self):
		'''property'''
		return self.walkable

	@walkable.setter
	def walkable(self, value):
		white = (255, 255, 255)
		red = (255, 0, 0)
		self.walkable = value
		# if it's set to walkable change to white
		# this will mark it as undirty
		if value:
			self.color = white
		else:
			self.color = red

	@property
	def fscore(self):
		return self.fscore

	@property
	def gscore(self):
		return self.gscore

	@property
	def hscore(self):
		return self.hscore

	@fscore.setter
	def fscore(self, value):
		self.fscore = value

	@gscore.setter
	def gscore(self, value):
		self.gscore = value

	@hscore.setter
	def hscore(self, value):
		self.hscore = value

	#setup your search area


	def getnode(index, g_node):
		'''gets node called'''
		return g_node.nodes[index]

	def get_neighbors(node, graph):
		'''Looks for the node's neighbors'''
		right = [1, 0]
		top = [0, 1]
		left = [-1, 0]
		down = [0, -1]
		dirs = [right, top, left, down]
		neighbors = []
		for i in dirs:
			nodekey = node.value[0] + i[0], node.value[1] + i[1]
			if graph.get_node(nodekey) is not None:
				neighbors.append(graph.get_node(nodekey))
				return neighbors

	def parentnode():
    		


	def moveparent(node, graph):
		'''set new node'''
		for i in self.__openlist__:
    			i.value(0)



		
def testastar():
    	astar = AStar()
	node = astar.get_node([1, 1])
    	node.print_info()
   	neighbors = get_neighbors(node, graph)
    	for neighbor in neighbors:
       		neighbor.print_info()


if __name__ == "__main__":
    	testastar()
	'''
	while True:
			if __openlist__.empty:
			print("no path")
			break
		elif (__closedlist__.contains(targetSquare)):
			print("path found")
			break
		else:
				
		draw the picture
		how do i get from the green to the red?
		there be a wall in between...

		Once we have simplified our search area into a manageable number of nodes,
		as we have done with the grid layout above,
		the next step is to conduct a search to find the shortest path.
		We do this by starting at point A,
		checking the adjacent squares,
		and generally searching outward until we find our target.

		1.
		Begin at A and add it to an "open list" of squares to be considered.
		open list is a list of potentital nodes we can go to.
		The items in this list MIGHT fall along the path you want to take, but maybe not.
		Basically a list of squares that need to be checked out

		2.
		Look at all the reachable or walkable squares adjacent to A and add them to the open List
		Important!
		save point A as their parent
		need this to retrace path

		3.
		Drop the starting square from openList and
		add it to closed list of squares that we don't need to look at anymore

		4.
		Choose one of the adjacent squares on the open list and repeat
		Which to choose? lowest F cost!
		What is F?
		F = G + H
		G = the movement cost to move from the starting point A to
		#a given square on the grid, following the path generated to get there
		H = the estimated movement cost to move from that given square
		on the grid to the final destination, point B.
	'''