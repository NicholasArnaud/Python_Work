'''Alorithm for A*'''
from Node import Node
from Graph import Graph



class AStar(object):
    '''Class for the A* algorithm'''
    def __init__(self):
        self.openlist = []
        self.closedlist = []
        self.currentnode = None

    # setup your search area
    def astaralgorithm(self, start, goal, graph):
        '''The legendary A* algorithm'''
        startnode = Node(start.value, start.ident)
        self.openlist.append(start)
        self.currentnode = start
        while True:
            self.sortlist()
            self.currentnode = self.openlist[0]
            self.openlist.remove(self.openlist[0])
            neighbors = startnode.get_neighbors(self.currentnode, graph)
            print self.currentnode.value
            if self.currentnode is goal:
                print "Complete"
                return False
            for node in neighbors:
                if node in self.closedlist is False:
                    continue
                if node not in self.openlist:
                    updatevalue(node, goal)
                    self.openlist.append(node)

    def sortlist(self):
        '''Sorts the open and closed lists'''
        if len(self.openlist) != 0:
            self.openlist.sort(key=lambda x: x.fscore)
            self.closedlist.append(self.openlist[0])



def updatevalue(node, goal):
    '''updates the G,H,F values'''
    node.hscore = distancetracker(node, goal)
    node.gscore = 10
    node.fscore = node.gscore + node.hscore

def distancetracker(node, goal):
    '''Returns the distance'''
    return 10 * (abs(goal.value[0] - node.value[0]) + abs(goal.value[1] - node.value[1]))


def test_nodes():
    '''test the nodes'''
    astar = AStar()
    __graph__ = Graph([3, 3])
    __node__ = __graph__.get_node([1, 1])
    __node2__ = __graph__.get_node([2, 2])
    astar.astaralgorithm(__node__, __node2__, __graph__)

if __name__ == "__main__":
    test_nodes()





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
