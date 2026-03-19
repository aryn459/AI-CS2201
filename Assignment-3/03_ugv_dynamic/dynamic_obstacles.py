import random

def move_obstacles(grid):
    size = len(grid)

    for _ in range(5):
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        grid[x][y] = 0

    for _ in range(5):
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        grid[x][y] = 1

    return grid