'''Alorithm for A*'''


# setup your search area
def algorithm(start, goal):
    '''The legendary A* algorithm'''
    openlist = []
    closedlist = []
    camefrom = {}
    currentnode = None
    openlist.append(start)
    currentnode = start



    while openlist != openlist.count(0):
        if currentnode == goal:
            return repath(goal, camefrom)
        openlist.remove(currentnode)
        closedlist.append(currentnode)
        sort_list(openlist, closedlist)
        currentnode = openlist[0]
        openlist.remove(openlist[0])

        for node in currentnode.neighbors:
            if node in closedlist is False:
                continue



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
