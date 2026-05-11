def minmax_pruning(node , if_max, alpha= float("-inf"), beta= float("inf")):
    if not node.children:
        return node.data

    if if_max:
        best = float("-inf")

        for child in node.children:
            value = minmax_pruning(child, False, alpha, beta)
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
            value = minmax_pruning(child, True, alpha, beta)
            best = min(best, value)
            beta = min(best, beta)

            if alpha >= beta:
                # print(value)
                print(f"Pruned subtree at node {child.data}")
                break
                
        node.data = best
        return best



    