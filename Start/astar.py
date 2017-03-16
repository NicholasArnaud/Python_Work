'''Alorithm for A*'''
from Node import Node
from drawablenode import DrawableNode
from Graph import Graph


class AStar(object):

    def __init__(self):
        self.adjacents = []
        self.parent = None
        self.walkable = True
        self.gscore = 0
        self.hscore = 0
        self.fscore = self.gscore + self.hscore
        self.startfrom = [Node]
        self.openlist = [Node]
        self.closedlist = [Node]

    # properties
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

    # setup your search area

    def astaralgorithm(self, start, goal):
        self.openlist.append(start)
        while True:
            if self.openlist.count != 0:
                self.openlist.sort(self.openlist, key=lambda x: x.fscore)
                currentnode = self.openlist[0]
                self.closedlist.append(currentnode)
                if currentnode == goal:
                    self.startfrom = self.openlist[0]
                    return
                for node in currentnode.adjacents:
                    if node in self.closedlist is False:
                        continue
                    if node not in self.openlist:
                        self.openlist.append(node)
                    node.gscore = currentnode.gscore
                    node.fscore = currentnode.gscore + currentnode.hscore


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
