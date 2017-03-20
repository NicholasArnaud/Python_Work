'''Node creator'''


class Node(object):
    '''Creates Nodes '''
    def __init__(self, xposition, yposition):
        '''Node Constuctor'''
        self.xpos = xposition
        self.ypos = yposition
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.neighbors = []
        self.parent = None

    def get_neighbors(self, graph):
        '''Looks for the node's neighbors'''
        right = [1, 0]
        top = [0, 1]
        left = [-1, 0]
        down = [0, -1]
        dirs = [right, top, left, down]
        for node in graph.nodelist:
            for position in dirs:
                if node.xpos == position[0] and node.ypos == position[1]:
                    self.neighbors.append(node)

    def shscore(self, goal):
        '''Returns the distance'''
        self.hscore = (abs(goal.xpos - self.xpos) + abs(goal.ypos - self.ypos))* 10
        return  self.hscore


    def sgscore(self, node):
        '''Gets gscore'''
        if self.parent is None:
            if node.xpos == self.xpos or node.ypos == self.ypos:
                node.gscore = 10
            else:
                node.gscore = 14
            self.parent = node
        else:
            tempg = 0
            if self.parent.xpos == self.xpos or self.parent.ypos == self.ypos:
                tempg = 10
            else:
                tempg = 14
            if tempg < self.gscore:
                self.gscore = tempg
                self.parent.children.append(self)

    def sfscore(self):
        '''sets the f score'''
        self.fscore = self.gscore + self.hscore
        return self.fscore

    def updatescores(self, goal):
        '''updates all scores'''
        self.shscore(goal)
        self.sgscore(self)
        self.sfscore()
