import random
import math 

random.seed(42)

class MCTSNode:
    def __init__(self, tree_node, parent = None):
        self.tree_node = tree_node
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

def select(node):
    while node.children:
        node = max(node.children, key=uct)
    return node

def uct(node):
    if node.visits ==0 :
        return float("inf")

    return (node.wins / node.visits) + 1.41* math.sqrt(math.log(node.parent.visits) /node.visits)

def expand(node):
    if not node.tree_node.children:
        return node
    
    for child in node.tree_node.children:
        new = MCTSNode(child, node)
        node.children.append(new)
    
    return random.choice(node.children)

def simulate(node):
    cur = node.tree_node

    while cur.children:
        cur = random.choice(cur.children)

    return cur.data

def backpropogate(node, result):
    while node:
        node.visits += 1
        node.wins += result
        node = node.parent


def montecarlo(root, iterations= 10):
    root_node = MCTSNode(root)

    for i in range(iterations):
        node = select(root_node)
        node = expand(node)
        result = simulate(node)

        print(f"simulation {i+1}, result: {result}")

        backpropogate(node, result)
    
    best = max(root_node.children, key=lambda child: child.visits)

    root.data = best.wins / best.visits

    return root.data

