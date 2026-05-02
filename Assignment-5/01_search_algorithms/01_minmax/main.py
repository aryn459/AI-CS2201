from tree import build_tree, assign_tree
from minmax import min_max

depth = int(input("Enter the depth(root- depth 0) for your minmax tree: "))
branching_factor = int(input("Enter the Branching factor for your minmax tree: "))

root = build_tree(depth, branching_factor)

assign_tree(root)

result = min_max(root, True) 

print("The Optimal value: ", result)

