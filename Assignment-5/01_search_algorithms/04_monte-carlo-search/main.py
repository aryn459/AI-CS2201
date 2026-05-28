from tree import build_tree, assign_tree, print_tree
from monte_carlo import montecarlo

depth = int(input("Enter the depth(root- depth 0) for your monte-carlo tree: "))
branching_factor = int(input("Enter the Branching factor for your monte-carlo tree: "))

root = build_tree(depth, branching_factor)
assign_tree(root)

# print("Tree before monte-carlo:")
# print_tree(root)

result = montecarlo(root, iterations=100)
print("The Optimal value: ", result)
# print("Tree after monte-carlo:")
# print_tree(root)