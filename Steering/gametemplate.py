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
        self.screen = game.display.set_mode((600, 600))
        self.c = game.time.Clock()
        self.delta_time = self.c.tick(10) / 1000.0

        self.startpos = Vector([30, 30])
        self.goal = Vector([200, 301])
        self.guy = agent(2, self.startpos)

    def _startup(self):
        '''do startup routines'''
        self.screen.fill(BLACK)
        return True

    def _update(self):
        '''input and time'''
        mouse.pos = game.mouse.get_pos()
        for  event in game.event.get():
            if game.mouse.get_pressed()[0]:
                self.goal.xpos = mouse_pos[0]
                self.goal.ypos = mouse_pos[1]
            if event.type == game.QUIT:
                return False
        return True

    def _draw(self):
        '''base draw'''
        game.display.flip()
        self.guy.seeking(self.goal, self.delta_time)
        self.screen.fill(BLACK)
        agent.draw(self.guy, self.screen, RED)


    def _shutdown(self):
        '''shutdown the game properly'''
        game.quit()
