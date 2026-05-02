class Treenode:
    def __init__(self, data = None):
        self.data = data
        self.children = []
    


def build_tree(depth, branching_factor):
    node = Treenode()
    if depth == 0:
        return node

    for _ in range(branching_factor):
        node.children.append(build_tree(depth -1 , branching_factor))
    return node 

def assign_tree(node):
    if not node.children:
        node.data = int(input("Enter value for leaf node: "))
        return
    
    for child in node.children:
        assign_tree(child)

def print_tree(node, level= 0):
    pass
