#pylint: disable = E1101
#pylint: disable = C0103
import pygame as game
import Astar
from Graph import Graph


game.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

pad = (23, 23)
columns = 10
rows = 10
width = 30
height = 30

screen_width = columns * (pad[0] + width) + pad[1]
screen_height = rows * (pad[0] + height) + pad[1]

screen = game.display.set_mode((screen_width, screen_height))
search_space = Graph([rows, columns])

done = False
clock = game.time.Clock()

game.font.init()

startnode = search_space.nodelist[0]
endnode = search_space.nodelist[99]
search_space.nodelist[26].walkable = False
search_space.nodelist[36].walkable = False
search_space.nodelist[46].walkable = False
search_space.nodelist[56].walkable = False
search_space.nodelist[66].walkable = False
search_space.nodelist[63].walkable = False
search_space.nodelist[64].walkable = False
search_space.nodelist[65].walkable = False
#search_space.nodelist[29].walkable = False
#search_space.nodelist[32].walkable = False
#search_space.nodelist[20].walkable = False


Astar.algorithm(startnode, endnode, search_space)

screen.fill(black)


for i in Astar.retrace(endnode):
    i.color = yellow



while not done:
    clock.tick(5)
    for  event in game.event.get():
        if event.type == game.QUIT:
            done = True
        for i in search_space.nodelist:
            i.draw(screen)
            if i.walkable is False:
                i.color = red
            if i == startnode:
                i.color = green
            if i == endnode:
                i.color = blue

    game.display.flip()

game.quit()
