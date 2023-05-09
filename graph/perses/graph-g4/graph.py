import json

class Node:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id


class Edge:
    def __init__(self, from_node_id, to_node_id):
        self.from_node_id = from_node_id
        self.to_node_id = to_node_id
        self.weight = 0
        self.has_weight = False

    def set_weight(self, weight):
        self.weight = weight
        self.has_weight = True

    def get_edge_info(self):
        return {
            'from': self.from_node_id,
            'to': self.to_node_id,
            'weight': self.weight,
            'has_weight': self.has_weight
        }


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.present_id = 0

    def create_node(self, id):
        node = Node(id)
        self.nodes.append(node)
        # self.present_id += 1
        return node

    def remove_node(self, node):
        self.nodes.remove(node)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    def create_weighted_edge(self, from_node: Node, to_node: Node, weight):
        edge = Edge(from_node.get_id(), to_node.get_id())
        edge.set_weight(weight)
        self.edges.append(edge)
        return edge

    def create_unweighted_edge(self, from_node: Node, to_node: Node):
        edge = Edge(from_node.get_id(), to_node.get_id())
        self.edges.append(edge)
        return edge

    def print(self):
        output_graph = {'nodes': [], 'edges': []}
        for node in self.nodes:
            output_graph['nodes'].append(node.get_id())
        for edge in self.edges:
            output_graph['edges'].append(edge.get_edge_info())

        with open('graph.json', mode='w+') as f:
            json.dump(output_graph, f)









