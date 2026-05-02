def min_max(node , if_max):
    if not node.children:
        return node.data

    values = []
    for child in node.children:
        values.append(min_max(child, not if_max))
    
    if if_max:
        node.data = max(values)
    else:
        node.data =  min(values)
    
    return node.data


    