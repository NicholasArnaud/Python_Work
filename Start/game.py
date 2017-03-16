import sys
import pygame as game
import astar

class Game(object):
    def __init__(self, graphpos):
        posx = graphpos[0].width
        posy = graphpos[0].height
        self.parent = None
        self.walkable = True

        # drawing vars
        size = 50
        self.width = size
        self.height = size
        self.index = (posx, posy)
        self.xpos = (5 + self.width) * posx + 5
        self.ypos = (5 + self.height) * posy + 5
        self.pos = (self.width * posx, self.height * posy)
        self.screenpos = (self.xpos, self.ypos)
        self.rect = game.Rect(self.xpos, self.ypos, self.width, self.height)
        self.dirty = False
        self._color = (125, 255, 255)
        self.screen = game.display.set_mode((self.pos))

    def drawscreen(self):
        '''draws the screen'''
        done = False
        clock = game.time.Clock()
        self.screen.fill(self.colsel("black"))
        game.init()
        game.draw.lines(self.screen, self.colsel("red"), False, [(10, 10), (15, 20), (20, 10)], 1)
        while not done:
            # This limits the while loop to a max of 10 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(10)

            for event in game.event.get():  # User did something
                if event.type == game.QUIT:  # If user clicked close
                    done = True  # Flag that we are DONE so we exit this loop
        game.quit()

    def colsel(self, collor):
        '''Chooses Color'''
        if collor == "red":
            return (255, 0, 0)
        if collor == "green":
            return (0, 255, 0)
        if collor == "blue":
            return (0, 0, 255)
        if collor == "darkblue":
            return (0, 0, 128)
        if collor == "white":
            return (255, 255, 255)
        if collor == "black":
            return (0, 0, 0)
        if collor == "pink":
            return (255, 200, 200)
