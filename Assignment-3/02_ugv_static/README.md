# Static UGV Path Planning using A*

This module simulates a UGV navigating a grid with fixed obstacles.

---

## Description

* Environment is represented as a 2D grid
* Obstacles are randomly generated
* Start and goal positions are predefined
* A* algorithm finds the shortest path

---

## Features

* Grid generation
* Obstacle placement
* Pathfinding using A*
* Visualization using matplotlib
* Animated simulation
* GIF output

---

## Run

```
python main.py
```

---

## Algorithm

A* uses:

f(n) = g(n) + h(n)

* g(n): cost from start
* h(n): Manhattan distance to goal

---

## Output

* Grid with obstacles
* Shortest path visualization
* Animation of path

---

## Conclusion

A* is efficient for static environments where all obstacles are known beforehand.
