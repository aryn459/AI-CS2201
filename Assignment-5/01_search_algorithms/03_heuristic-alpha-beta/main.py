from tree import build_tree, assign_tree, print_tree
from alphabeta import minmax_pruning

depth = int(input("Enter the depth(root- depth 0) for your alpha-beta tree: "))
branching_factor = int(input("Enter the Branching factor for your alpha-beta tree: "))

root = build_tree(depth, branching_factor)
assign_tree(root)

print("Tree before alpha-beta heuristic:")
print_tree(root)

result = minmax_pruning(root, depth= depth, if_max= True) 
# print("The Optimal value: ", result)
print("Tree after alpha-beta heuristic:")
print_tree(root)