class Node:
    def __init__(self, x, y, z, id=None):
        self.position = (x, y, z)
        self.id = id
        self.neighbors = []

class Network:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, x, y, z, id=None):
        """Add a node to the network"""
        node = Node(x, y, z, id)
        self.nodes.append(node)
        return node
    
    def connect_nodes(self, node1, node2):
        """Create a connection between two nodes"""
        if node2 not in node1.neighbors:
            node1.neighbors.append(node2)
        if node1 not in node2.neighbors:
            node2.neighbors.append(node1)
    
    def distance(self, node1, node2):
        """Calculate Euclidean distance between two nodes"""
        x1, y1, z1 = node1.position
        x2, y2, z2 = node2.position
        return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5