'''Alorithm for A*'''


# setup your search area
def algorithm(start, goal, grid):
    '''The legendary A* algorithm'''
    openlist = []
    closedlist = []
    camefrom = {}
    currentnode = start

    for updatenodes in grid.nodelist:
        updatenodes.updatescores(goal)
    goal.updatescores(goal)
    openlist.append(currentnode)
    while openlist is not None:

        #checks if the current node is at the goal and follows parent path
        if currentnode == goal:
            return repath(goal, camefrom)

        #gets the neighbors for the current node in the grid given
        currentnode.get_neighbors(grid)
        #assigns the current node to the first node in openlist
        currentnode = openlist[0]
        #removes that node from the open list
        openlist.remove(currentnode)
        #adds the new current node into the closed list
        closedlist.append(currentnode)
        #updates the currentnodes f,g,h scores from the goal
        currentnode.updatescores(goal)
        #sortlist sorts the node list from grid by the 'f' score
        sort_list(grid)

        #loops through the adjacent nodes to check if they found the goal node
        for node in currentnode.neighbors:
            if node in closedlist is False:
                continue
            #not fully understanding the tentative g score yet
            currentnode.tempg = currentnode.gscore + node.gscore
            #if the searched node is not in the open list yet it adds it to be checked
            if node not in openlist:
                openlist.append(node)
            else:
                #updates all the node's f,g,h scores in the grid
                node.updatescores(goal)
                continue




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
