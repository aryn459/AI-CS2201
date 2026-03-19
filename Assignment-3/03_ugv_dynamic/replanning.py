import sys
sys.path.append("../02_ugv_static")

from astar import astar

def replan(grid, start, goal):
    return astar(grid, start, goal)
    