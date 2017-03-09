'''Main file '''


from Graph import Graph
from Node import Node


def test_nodes():
    '''test the nodes'''
    graph = Graph(5, 5)
    node = Node.Node(1, 0).get_node(2, graph)
    node.print_info()
    neighbors = get_neighbors(node, graph)
    for node in neighbors:
        node.print_info()


if __name__ == '__main__':
    test_nodes()
