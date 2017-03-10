'''Main file '''


from Graph import Graph

def get_neighbors(node, graph):
    '''Looks for the node's neighbors'''
    right = [1, 0]
    top = [0, 1]
    left = [-1, 0]
    down = [0, -1]
    dirs = [right, top, left, down]
    neighbors = []
    for i in dirs:
        nodekey = node.value[0] + i[0], node.value[1] + i[1]
        if graph.get_node(nodekey) is not None:
            neighbors.append(graph.get_node(nodekey))
    return neighbors


def test_nodes():
    '''test the nodes'''
    graph = Graph([5, 5])
    node = graph.get_node([2, 1])
    node.print_info()
    neighbors = get_neighbors(node, graph)
    for node in neighbors:
        node.print_info()


if __name__ == '__main__':
    test_nodes()
