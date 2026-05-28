def minmax_pruning(node, depth, if_max, alpha= float("-inf"), beta= float("inf")):
    if depth == 0 or not node.children:
        val = heuristic(node, depth)
        print(f"Heuristic value at node = {val}")
        return val

    

    if if_max:
        best = float("-inf")

        for child in node.children:
            value = minmax_pruning(child, depth - 1, False, alpha, beta)
            best = max(best, value)
            alpha = max(best, alpha)

            if alpha >= beta:
                print(f"Pruned subtree at node {child.data}")
                # print(value)
                break

        node.data = best
        return best

    else:
        best = float("inf")

        for child in node.children:
            value = minmax_pruning(child, depth -1, True, alpha, beta)
            best = min(best, value)
            beta = min(best, beta)

            if alpha >= beta:
                # print(value)
                print(f"Pruned subtree at node {child.data}")
                break
                
        node.data = best
        return best

def heuristic(node, depth):
    if not node.children:
        return node.data

    avg = sum(child.data for child in node.children) / len(node.children)

    return avg - depth


    