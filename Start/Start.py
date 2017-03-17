'''Main file '''
from Game import GameLoop
from Game import AStarInteraction
from Astar import AStar
from Graph import Graph
from Node import NodeInformation

astar = AStar()
__graph__ = Graph([10, 10])
__node__ = __graph__.get_node([1, 1])
__node2__ = __graph__.get_node([5, 5])
astar.astaralgorithm(__node__, __node2__, __graph__)

INFO = NodeInformation([0, 750])

interaction = AStarInteraction(__graph__, GameLoop())
interaction.addalgorithmstate("InfoMode", False)
interaction.addalgorithmstate("UserStep", False)
interaction.addbuttoncontrol("I", False)
interaction.addbuttoncontrol("LeftMouse", False)
interaction.addbuttoncontrol("MiddleMouse", False)
interaction.addbuttoncontrol("RightMouse", False)


while GameLoop().update():
    interaction.update(GameLoop().deltatime)
    if astar.currentnode != None:
        INFO.drawinformation(astar.currentnode)
