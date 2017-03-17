'''Node creator'''
import pygame
from Drawable import Rectangle
from Drawable import Circle
from Drawable import Line
from Drawable import Text
from Drawable import WHITE
from Drawable import BLACK
from Drawable import GREEN
from Drawable import BLUE
from Drawable import RED
from Drawable import YELLOW

SIZE = WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode(SIZE)

class Node(object):
    '''Creates Nodes '''
    def __init__(self, val, idee):
        '''Node Constuctor'''
        self.__ide = idee
        self.__val = val
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.adjacents = []

    def print_info(self):
        '''prints info'''
        print("ID:", self.__ide, "Value:", self.__val)

  # properties
    @property
    def value(self):
        '''gets value'''
        return self.__val

    @property
    def ident(self):
        '''gets id'''
        return self.__ide

    def get_neighbors(self, node, graph):
        '''Looks for the node's neighbors'''
        right = [1, 0]
        top = [0, 1]
        left = [-1, 0]
        down = [0, -1]
        dirs = [right, top, left, down]
        for i in dirs:
            nodekey = node.value[0] + i[0], node.value[1] + i[1]
            if graph.get_node(nodekey) is not None:
                self.adjacents.append(graph.get_node(nodekey))
        return self.adjacents

class NodeInformation(object):
    '''Creates text to display to the window with a nodes gscore, hscore, and fscore'''
    def __init__(self, position):
        self.position = position

    def drawinformation(self, node):
        '''Updates the text element with the information of the node passed in'''
        if(node != None):
            gposition = self.position
            hposition = [self.position[0], self.position[1] + 50]
            fposition = [self.position[0], self.position[1] + 100]
            gtext = Text(SCREEN, gposition, [WHITE, BLACK], "G Score: " + str(node.gscore), 25)
            htext = Text(SCREEN, hposition, [WHITE, BLACK], "H Score:" + str(node.hscore), 25)
            ftext = Text(SCREEN, fposition, [WHITE, BLACK], "F Score:" + str(node.fscore), 25)
            gtext.draw()
            htext.draw()
            ftext.draw()
