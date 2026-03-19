import matplotlib.pyplot as plt
from grid import create_grid
from obstacles import add_obstacles
from astar import astar
import imageio.v2 as imageio
import os
os.makedirs("../outputs", exist_ok=True)

size = 70
grid = create_grid(size)
grid = add_obstacles(grid, 0.2)

start = (0, 0)
goal = (65, 65)
grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

path = astar(grid, start, goal)

frames = []
plt.figure()

if path:
    for i in range(len(path)):
        plt.clf()
        plt.imshow(grid, cmap='binary')

        x = [p[1] for p in path[:i+1]]
        y = [p[0] for p in path[:i+1]]
        plt.plot(x, y)

        plt.scatter(start[1], start[0])
        plt.scatter(goal[1], goal[0])

        plt.title("Static UGV Path Planning (A*)")
        plt.savefig("temp.png")
        frames.append(imageio.imread("temp.png"))

    imageio.mimsave("../outputs/static1.gif", frames, duration=0.2)

plt.show()