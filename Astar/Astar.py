'''Alorithm for A*'''
import Graph
import Node

# setup your search area
def algorithm(start, goal, grid):
    '''The legendary A* algorithm'''
    openlist = []
    closedlist = []
    camefrom = {}
    currentnode = None
    openlist.append(start)
    currentnode = start
    gscore = []
    fscore = []
    fscore[start] = cost_estimate(start, goal)


    while openlist != openlist.count(0):
        if currentnode == goal:
            return repath(goal, camefrom)
        openlist.remove(currentnode)
        closedlist.append(currentnode)
        sort_list(openlist, closedlist)
        currentnode = openlist[0]
        openlist.remove(openlist[0])

        for node in currentnode.neighbor:
            if node in closedlist is False:
                continue
            camefrom[currentnode.neighbor] = currentnode
            fscore[currentnode.neighbor] = gscore[currentnode.neighbor] + cost_estimate(currentnode.neighbor, goal)


def repath(camefrom, current):
    '''Rebuilds the path'''
    total_path = [current]
    while current in camefrom.Keys:
        current = camefrom[current]
        total_path.append(current)
    return total_path


def sort_list(openlist, closedlist):
    '''Sorts the open and closed lists'''
    if len(openlist) != 0:
        openlist.sort(key=lambda x: x.fscore)
        closedlist.append(openlist[0])

def cost_estimate(node, goal):
    '''Returns the distance'''
    return  (abs(goal.point[0] - node.point[0]) + abs(goal.point[1] - node.point[1]))* 10

def sgscore(node, goal):
    '''Gets gscore'''
    u = abs(goal.posx - node.posx)
    l = abs(goal.posy - node.posy)
    if u > l:
        return (l * 14) + (u-l) * 10
    if l > u:
        return (u * 14) + (l-u) * 10
    else:
        return u * 14
