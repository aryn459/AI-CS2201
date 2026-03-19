import matplotlib.pyplot as plt
import sys
sys.path.append("../02_ugv_static")

from grid import create_grid
from obstacles import add_obstacles
from astar import astar
from dynamic_obstacles import move_obstacles

import imageio.v2 as imageio
import os

os.makedirs("../outputs", exist_ok=True)

size = 70
grid = create_grid(size)
grid = add_obstacles(grid, 0.2)

start = (0, 0)
goal = (66, 66)

grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

current = start
frames = []
plt.figure()
plt.ion()

while current != goal:
    path = astar(grid, current, goal)
    if not path or len(path) < 2:
        print("No path available")
        break

    next_step = path[1]
    current = next_step

    grid = move_obstacles(grid)

    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    plt.clf()
    plt.imshow(grid, cmap='binary')
    x = [p[1] for p in path]
    y = [p[0] for p in path]
    plt.plot(x, y)

    plt.scatter(current[1], current[0])
    plt.scatter(goal[1], goal[0])

    plt.title("Dynamic UGV Path Planning")
    plt.pause(0.1)
    plt.savefig("temp.png")
    frames.append(imageio.imread("temp.png"))

if frames:
    imageio.mimsave("../outputs/dynamic.gif", frames, duration=0.2)
plt.ioff()
plt.show()