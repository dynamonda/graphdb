#!/usr/local/bin/python

"""GraphDB"""

import argparse
import json
from pathlib import Path

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
    def __init__(self, name='', json_file=None):
        self.node_list = list()
        self.edge_list = list()
        if json_file != None:
            json_path = Path(json_file)
            if json_path.exists():
                with open(json_path) as f:
                    json_object = json.load(f)
                    self.name = json_object['name']
                    for data in json_object['node']:
                        node = Node(name=data['name'])
                        self.node_list.append(node)
                    for data in json_object['edge']:
                        source_node = None
                        if data['source_node'] != -1:
                            source_node = self.node_list[data['source_node']]
                        target_node = None
                        if data['target_node'] != -1:
                            target_node = self.node_list[data['target_node']]
                        edge = Edge(
                            name=data['name'],
                            source_node=source_node,
                            target_node=target_node
                        )
                        self.edge_list.append(edge)
            else:
                print("Graph __init__(): not found file {0}".format(json_file))
        else:
            self.name = name
            

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

    def get_index_node(self, node):
        """get index of node

        Args:
            node: a node object
        Rerutn:
            index number [0..N]
        """
        if node is None:
            return -1
        for index in range(len(self.node_list)):
            if node is self.node_list[index]:
                return index
        raise NotFoundException()

    def Print(self):
        """Print info"""
        print(self.name)
        print("Nodes:")
        for n in self.node_list:
            print("\t{0}".format(n))
        print("Edges:")
        for e in self.edge_list:
            print("\t{0}:\t{1}\t-> {2}".format(e, e.source_node, e.target_node))

    def save_json(self, path):
        """save json file
        
        Args:
            path: save file path
        """
        json_object = {
            'name': self.name,
            'node': list(),
            'edge': list()
        }
        for index in range(len(self.node_list)):
            node_obj = {
                'id': index,
                'name': self.node_list[index].name
            }
            json_object['node'].append(node_obj)
        for index in range(len(self.edge_list)):
            edge_obj = {
                'id': index,
                'name': self.edge_list[index].name,
                'source_node': self.get_index_node(self.edge_list[index].source_node),
                'target_node': self.get_index_node(self.edge_list[index].target_node)
            }
            json_object['edge'].append(edge_obj)
        with open(path, mode='w') as file:
            json.dump(json_object, file, ensure_ascii=False, indent=4)


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


class NotFoundException(Exception):
    """Error not found to target"""
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='use .json file')
    args = parser.parse_args()

    if args.file != None:
        graph = Graph(json_file=args.file)
        graph.Print()
    else:
        graph = Graph("test")
        node1 = Node("node1")
        node2 = Node("node2")
        edge1 = Edge('edge1', node1, node2)
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_edge(edge1)
        graph.add_edge(Edge('edge2'))
        graph.Print()
        graph.save_json('./json/testdb.json')

if __name__ == '__main__':
    main()