class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.childnren = [child for child in self.children if child is not child_node]

    def traverse(self):
        nodes_to_traverse = [self]
        while len(nodes_to_traverse) > 0:
            current_node = nodes_to_traverse.pop()
            nodes_to_traverse += current_node.children