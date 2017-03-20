'''Alorithm for A*'''


# setup your search area
def algorithm(start, goal, grid):
    '''The legendary A* algorithm'''
    openlist = [start]
    closedlist = []
    camefrom = {}
    currentnode = None
    currentnode = start



    while openlist != openlist.count(0):
        if currentnode == goal:
            return repath(goal, camefrom)
        currentnode.neighbors(currentnode, grid)
        currentnode.updatescores(currentnode, goal)
        sort_list(grid)
        currentnode = openlist[0]
        openlist.remove(currentnode)
        closedlist.append(currentnode)


        for node in currentnode.adjacents:
            if node in closedlist is False:
                continue
            currentnode.tempg = currentnode.g + node.g
            if node not in openlist:
                openlist.append(node)
            else:
                continue
            node.parent = currentnode
            node.hscore = node.shscore
            node.gscore = node.sgscore
            node.fscore = node.sfscore




def repath(camefrom, current):
    '''Rebuilds the path'''
    total_path = [current]
    while current in camefrom.Keys:
        current = camefrom[current]
        total_path.append(current)
    return total_path


def sort_list(grid):
    '''Sorts the open and closed lists'''
    for node in grid.nodelist:
        for nodes in grid.nodelist:
            if node.fscore < nodes.fscore:
                tempnode = node
                node = nodes
                nodes = tempnode
