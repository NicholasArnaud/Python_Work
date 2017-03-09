'''Main file '''


from Graph import Graph




def test_nodes():
    '''test the nodes'''
    graph = Graph([5, 5])
    node = graph.get_node([2, 1])
    node.print_info()
    neighbors = graph.get_neighbors(node, graph)
    for node in neighbors:
        node.print_info()


if __name__ == '__main__':
    test_nodes()
