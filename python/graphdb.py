#!/usr/local/bin/python

"""GraphDB"""

class GraphObject(object):
    """Object used in Graph"""
    def __init__(self, name=''):
        self.name = name

    def __str__(self):
        return "{0}".format(self.name)


class Graph(object):
    """Graph object
    
    G = (N, E)
    """
    def __init__(self, name=''):
        self.name = name
        self.node_list = list()
        self.edge_list = list()

    def add_node(self, node):
        """Add node in node_list

        Args:
            node: a added node object
        """
        self.node_list.append(node)

    def add_edge(self, edge):
        """Add edge in edge_list

        Args:
            edge: a added edge object
        """
        self.edge_list.append(edge)

    def __str__(self):
        return ("{0}\n{1}\n{2}".format(
            self.name, self.node_list, self.edge_list
        ))


class Node(GraphObject):
    """Node object"""
    def __init__(self, name=''):
        super().__init__(name=name)


class Edge(GraphObject):
    """Edge object"""
    def __init__(self, name='', source_node=None, target_node=None):
        super().__init__(name=name)
        self.source_node = source_node
        self.target_node = target_node


def main():
    graph = Graph("test")
    graph.add_node(Node("node1"))
    graph.add_node(Node("node2"))
    print(graph)

if __name__ == '__main__':
    main()