#!/usr/local/bin/python

"""GraphDB"""

import argparse
import json
from pathlib import Path

class GraphObject(object):
    """Object used in Graph"""
    def __init__(self, name=''):
        self.name = name
        self.info = dict()

    def __str__(self):
        return "{0}".format(self.name)


class Graph(object):
    """Graph object
    
    G = (N, E)
    """
    def __init__(self, name=''):
        self.name = name
        self.node_dict = dict()
        self.edge_dict = dict()
        self.node_next_index = 0
        self.edge_next_index = 0

    def add_node(self, node, key=None):
        """Add node in node_dict

        Args:
            key : a key of node
            node: a added node object
        """
        if key is None:
            self.node_dict[str(self.node_next_index)] = node
            self.node_next_index += 1
        else:
            self.node_dict[key] = node

    def add_edge(self, edge, key=None):
        """Add edge in edge_dict

        Args:
            edge: a added edge object
        """
        if key is None:
            self.edge_dict[str(self.edge_next_index)] = edge
            self.edge_next_index += 1
        else:
            self.edge_dict[key] = edge

    def get_key_node(self, node):
        """get key of node

        Args:
            node: a node object
        Rerutn:
            index key
        """
        if node is None:
            return None
        for k, n in self.node_dict.items():
            if n is node:
                return k
        raise NotFoundException()

    def Print(self):
        """Print info"""
        print(self.name)
        print("Nodes:\tnext index {0}".format(self.node_next_index))
        for k, n in self.node_dict.items():
            print("\t{0}: {1}".format(k, n))
        print("Edges:\tnext index {0}".format(self.edge_next_index))
        for k, e in self.edge_dict.items():
            print("\t{0}: {1}: {2} -> {3}".format(
                k, e, e.source_node, e.target_node))

    def save_json(self, path):
        """save json file
        
        Args:
            path: save file path
        """
        json_object = {
            'name': self.name,
            'node': dict(),
            'edge': dict(),
            'node_next_index': self.node_next_index,
            'edge_next_index': self.edge_next_index
        }
        for k, n in self.node_dict.items():
            json_object['node'][k] = n.Dict()
        for k, e in self.edge_dict.items():
            json_object['edge'][k] = e.Dict(self)
        with open(path, mode='w') as file:
            json.dump(json_object, file, ensure_ascii=False, indent=4)


def GraphFromJson(json_file_path):
    """Create Graph object from json file

    Args:
        json_object: json file path

    Return:
        A Graph object
    """
    json_path = Path(json_file_path)
    if json_path.exists():
        with open(json_path) as f:
            json_object = json.load(f)
            graph = Graph(name=json_object['name'])
            for k, v in json_object['node'].items():
                graph.add_node(key=k, node=v)
            for k, v in json_object['edge'].items():
                source_node = None
                if 'source_node' in v:
                    source_node = v['source_node']
                target_node = None
                if 'target_node' in v:
                    target_node = v['target_node']
                edge = Edge(
                    name=v['name'],
                    source_node=source_node,
                    target_node=target_node
                )
                graph.add_edge(key=k, edge=edge)
            graph.node_next_index = int(json_object['node_next_index'])
            graph.edge_next_index = int(json_object['edge_next_index'])
            return graph
    else:
        raise NotFoundException()


class Node(GraphObject):
    """Node object"""
    def __init__(self, name=''):
        super().__init__(name=name)

    def Dict(self):
        """return dict object"""
        dict_object = {
            'name': self.name
        }
        return dict_object


class Edge(GraphObject):
    """Edge object"""
    def __init__(self, name='', source_node=None, target_node=None):
        super().__init__(name=name)
        self.source_node = source_node
        self.target_node = target_node

    def Dict(self, graph):
        """return dict object"""
        dict_object = {
            'name': self.name
        }
        if self.source_node != None:
            # ここ変更
            dict_object['source_node'] = graph.get_key_node(self.source_node)
        if self.target_node != None:
            # ここ変更
            dict_object['target_node'] = graph.get_key_node(self.target_node)
        return dict_object


class NotFoundException(Exception):
    """Error not found to target"""
    pass

def print_help_message():
    """interactive mode help message"""
    print("help\t\t:print help message")
    print("exit\t\t:exit interactive mode")
    print()
    print("print:\t\t:print graph object")
    print("set [graphname]\t:set Graph name")
    print("save [filepath]\t:save Graph to json file")
    print()
    print("create node [name]\t:Create Node object into Graph")
    print()
    print("create edge [name]\t:Create Edge object into Graph")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='use .json file')
    parser.add_argument('-i', action='store_true', help='interactive mode')
    args = parser.parse_args()

    if args.file != None:
        graph = GraphFromJson(args.file)
        graph.Print()
    elif args.i == True:
        print("Hello! graphdb [help] or [exit]")
        interactive_loop = True
        graph = Graph()
        while interactive_loop:
            print("> ", end='')
            inputs = input().split()
            if len(inputs) > 0:
                if inputs[0] == 'exit':
                    interactive_loop = False
                    print('Bye.')
                elif inputs[0] == 'help':
                    print_help_message()
                elif inputs[0] == 'print':
                    graph.Print()
                elif inputs[0] == 'set':
                    if len(inputs) > 1 and len(inputs[1]) > 0:
                        graph.name = inputs[1]
                elif inputs[0] == 'save':
                    if len(inputs) > 1 and len(inputs[1]) > 0:
                        graph.save_json(inputs[1])
                elif inputs[0] == 'create':
                    if len(inputs) < 2:
                        print("create node\t:Create Node object into Graph")
                    elif inputs[1] == 'node':
                        node = Node(inputs[2])
                        graph.add_node(node)
                    elif inputs[1] == 'edge':
                        edge = Edge(inputs[2])
                        graph.add_edge(edge)
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