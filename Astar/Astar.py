'''Alorithm for A*'''


# setup your search area
def algorithm(start, goal, grid):
    '''The legendary A* algorithm'''
    openlist = []
    closedlist = []
    currentnode = start
    openlist.append(currentnode)
    while len(openlist) != 0:

        #sortlist sorts the node list from grid by the 'f' score
        sort_list(grid)
        #assigns the current node to the first node in openlist
        currentnode = openlist[0]
        #adds the new current node into the closed list
        closedlist.append(currentnode)
        #removes that node from the open list
        openlist.remove(currentnode)
        #gets the neighbors for the current node in the grid given
        currentnode.get_neighbors(grid)

        #loops through the adjacent nodes to check if they found the goal node
        for neighbor in currentnode.neighbors:
            currentnode.sgscore(neighbor)
            neighbor.updatescores(goal)
            if neighbor in closedlist or not neighbor.walkable:
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

        #checks if the current node is at the goal and follows parent path
        if currentnode == goal:
            return retrace(currentnode)

    return False


def retrace(node):
    '''reconstructs the path'''
    final_path = []
    parentednode = node
    while parentednode is not None:
        final_path.append(parentednode)
        parentednode = parentednode.parent
    for node in final_path:
        node.printnode()
    return final_path


def sort_list(grid):
    '''Sorts the open and closed lists'''
    for node in grid.nodelist:
        for nodes in grid.nodelist:
            if node.fscore < nodes.fscore:
                tempnode = node
                node = nodes
                nodes = tempnode
