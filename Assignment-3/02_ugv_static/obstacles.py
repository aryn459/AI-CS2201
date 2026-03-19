import random

def add_obstacles(grid, density):
    size = len(grid)
    blocks = int(size * size * density)

    for _ in range(blocks):
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        grid[x][y] = 1

    return grid