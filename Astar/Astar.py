'''Alorithm for A*'''


# setup your search area
def algorithm(start, goal, grid):
    '''The legendary A* algorithm'''
    openlist = []
    closedlist = []
    currentnode = start
    openlist.append(currentnode)
    while openlist is not None:

        #checks if the current node is at the goal and follows parent path
        if currentnode == goal:
            return repath(goal, start)
        #assigns the current node to the first node in openlist
        currentnode = openlist[0]
        #gets the neighbors for the current node in the grid given
        currentnode.get_neighbors(grid)

        #loops through the adjacent nodes to check if they found the goal node
        for neighbor in currentnode.neighbors:
            currentnode.sgscore(neighbor)
            neighbor.updatescores(goal)
            if neighbor in closedlist:
                continue
            tentative_gscore = currentnode.gscore + currentnode.sgscore(neighbor)
            #if the searched node is not in the open list yet it adds it to be checked
            if neighbor not in openlist:
                openlist.append(neighbor)
            elif tentative_gscore > neighbor.gscore:
                continue
            #updates all the node's f,g,h scores in the grid
            neighbor.parent = currentnode
            neighbor.gscore = tentative_gscore
            neighbor.updatescores(goal)
        #sortlist sorts the node list from grid by the 'f' score
        sort_list(grid)
        #removes that node from the open list
        openlist.remove(currentnode)
        #adds the new current node into the closed list
        closedlist.append(currentnode)
    return False



def repath(endnode, startnode):
    '''Rebuilds the path'''

def sort_list(grid):
    '''Sorts the open and closed lists'''
    for node in grid.nodelist:
        for nodes in grid.nodelist:
            if node.fscore < nodes.fscore:
                tempnode = node
                node = nodes
                nodes = tempnode
