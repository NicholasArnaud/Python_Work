'''gametemplate.py'''
#pylint: disable=E1101
#from gameobject import GameObject
import pygame as game
from agent import agent
from mathlib import Vector
from constants import *


class GameTemplate(object):
    '''pygame object'''
    def __init__(self):

        game.init()
        self.startpos = Vector([30, 30])
        self.goal = Vector([50, 50])
        self.screen = game.display.set_mode((1280, 720))
        self.agentlist = []
        for i in range(0, 100):
            self.agentlist.append(agent(100, Vector([i + 20, i + 10])))

    def _startup(self):
        '''do startup routines'''
        self.screen.fill(BLACK)
        return True

    def _update(self):
        '''input and time'''
        self.c = game.time.Clock()
        self.delta_time = self.c.tick(60) / 1000.0

        mouse_pos = game.mouse.get_pos()
        for  event in game.event.get():
            if game.mouse.get_pressed()[0]:
                for i in self.agentlist:
                    i.seeking(self.goal, self.delta_time)
                self.goal.xpos = mouse_pos[0]
                self.goal.ypos = mouse_pos[1]

            if game.mouse.get_pressed()[1]:
                for i in self.agentlist:
                    i.wondering(15, 10)

            if game.mouse.get_pressed()[2]:
                for i in self.agentlist:
                    i.fleeing(self.goal, self.delta_time)
                self.goal.xpos = mouse_pos[0]
                self.goal.ypos = mouse_pos[1]

            if event.type == game.QUIT:
                return False
        return True

    def _draw(self):
        '''base draw'''
        game.display.flip()
        self.screen.fill(BLACK)
        for i in self.agentlist:
            agent.draw(i, self.screen, RED)


    def _shutdown(self):
        '''shutdown the game properly'''
        game.quit()
