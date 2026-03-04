from collections import deque

def successors(a, b, cap_a=5, cap_b=3):
    moves = [
        (cap_a, b), (a, cap_b),
        (0, b),     (a, 0),
        (a - min(a, cap_b-b), b + min(a, cap_b-b)),
        (a + min(b, cap_a-a), b - min(b, cap_a-a))
    ]
    return [(na, nb) for na, nb in moves if (na, nb) != (a, b)]

def bfs(goal=4):
    q = deque([[(0,0)]])
    visited = {(0,0)}
    while q:
        path = q.popleft()
        a, b = path[-1]
        if goal in (a, b): return path
        for nxt in successors(a, b):
            if nxt not in visited:
                visited.add(nxt)
                q.append(path + [nxt])

def dfs(goal=4):
    stack = [[(0,0)]]
    visited = {(0,0)}
    while stack:
        path = stack.pop()
        a, b = path[-1]
        if goal in (a, b): return path
        for nxt in successors(a, b):
            if nxt not in visited:
                visited.add(nxt)
                stack.append(path + [nxt])

def dls(path, depth, goal=4):
    a, b = path[-1]
    if goal in (a, b): return path
    if depth == 0:     return None
    for nxt in successors(a, b):
        if nxt not in path:                   # avoid cycles using path itself
            res = dls(path + [nxt], depth-1, goal)
            if res: return res

def iddfs(goal=4):
    for depth in range(20):
        res = dls([(0,0)], depth, goal)
        if res: return res

print("BFS  :", bfs())
print("DFS  :", dfs())
print("DLS  :", dls([(0,0)], 10))
print("IDDFS:", iddfs())
