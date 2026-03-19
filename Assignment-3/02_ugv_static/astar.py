import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start)]
    parent = {}
    g = {start: 0}

    while pq:
        _, curr = heapq.heappop(pq)

        if curr == goal:
            path = []
            while curr in parent:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            return path[::-1]

        x, y = curr

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy

            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:
                new_g = g[curr] + 1

                if (nx,ny) not in g or new_g < g[(nx,ny)]:
                    g[(nx,ny)] = new_g
                    f = new_g + heuristic((nx,ny), goal)
                    heapq.heappush(pq, (f, (nx,ny)))
                    parent[(nx,ny)] = curr

    return None