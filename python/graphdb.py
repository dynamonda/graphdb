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

    def Print(self):
        """Print info"""
        print(self.name)
        print("Nodes:")
        for n in self.node_list:
            print("\t{0}".format(n))
        print("Edges:")
        for e in self.edge_list:
            print("\t{0}:\t{1}\t-> {2}".format(e, e.source_node, e.target_node))


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
    node1 = Node("node1")
    node2 = Node("node2")
    edge1 = Edge('edge1', node1, node2)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_edge(edge1)
    graph.add_edge(Edge('edge2'))
    graph.Print()

if __name__ == '__main__':
    main()