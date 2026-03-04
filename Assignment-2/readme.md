# Uninformed Search Algorithms in Python

### BFS, DFS, DLS and IDDFS using the Milk and Water Jug Problem

## Overview

This project demonstrates the implementation of **Uninformed Search algorithms** using the **Milk and Water Jug Problem** as a search problem.

The algorithms implemented are:

* Breadth First Search (BFS)
* Depth First Search (DFS)
* Depth Limited Search (DLS)
* Iterative Deepening Depth First Search (IDDFS)

These algorithms explore the **state space of the problem** to reach a goal state.

The implementation is written in **Python** as a single file console program.

---

# Problem Description

The **Milk and Water Jug Problem** is a classic Artificial Intelligence search problem.

We are given:

* Jug A capacity = **5 liters**
* Jug B capacity = **3 liters**
* Initial state = **(0, 0)** (both jugs empty)

Goal:

Measure **exactly 4 liters** in one of the jugs.

A state is represented as:

(jug_a, jug_b)

Example:

(3, 0) means Jug A contains 3 liters and Jug B contains 0 liters.

---

# Allowed Operations

From any state the following operations can be performed:

1. Fill Jug A
2. Fill Jug B
3. Empty Jug A
4. Empty Jug B
5. Pour Jug A → Jug B
6. Pour Jug B → Jug A

These operations generate the **successor states** used by the search algorithms.

---

# Project Structure

```
uninformed_milk-jug.py       — single file containing all algorithms and main
```

Description:

* **successors()**
  Generates all valid next states from the current state by applying all 6 operations. Filters out no-op moves where the state does not change.

* **bfs()**
  Breadth First Search using a deque as a queue. Stores the full path to each state.

* **dfs()**
  Depth First Search using a list as a stack. Stores the full path to each state.

* **dls()**
  Depth Limited Search using recursion. Uses the path itself to avoid cycles — no separate visited set needed.

* **iddfs()**
  Iterative Deepening DFS calling DLS with increasing depth limits from 0 to 20.

* **main()**
  Runs all four algorithms and prints their solution paths.

---

# Running the Project

Run:

```
python uninformed_milk-jug.py
```

Example output:

```
BFS  : [(0,0), (5,0), (2,3), (2,0), (0,2), (5,2), (4,3)]
DFS  : [(0,0), (0,3), (3,0), (3,3), (5,1), (0,1), (1,0), (1,3), (4,0)]
DLS  : [(0,0), (0,3), (3,0), (3,3), (5,1), (0,1), (1,0), (1,3), (4,0)]
IDDFS: [(0,0), (5,0), (2,3), (2,0), (0,2), (5,2), (4,3)]
```

---

# Algorithms Implemented

## 1. Breadth First Search (BFS)

BFS explores the search space **level by level**.

It uses a **deque** from Python's `collections` module as a queue storing the full path to each node.

Properties:

* Complete — always finds a solution if one exists
* Optimal — guarantees the shortest path
* Higher memory usage due to queue storage

---

## 2. Depth First Search (DFS)

DFS explores the **deepest branch first** before backtracking.

It uses a **list as a stack** storing the full path to each node.

Properties:

* Low memory usage
* May find a solution faster
* Does not guarantee the optimal solution

---

## 3. Depth Limited Search (DLS)

DLS is a recursive DFS that **stops at a fixed depth limit**.

Uses `if nxt not in path` to avoid cycles — the path list itself acts as the visited tracker so no separate set is needed.

Properties:

* Avoids infinite loops with a depth cap
* Complete only if the depth limit is set at or above the solution depth
* Does not guarantee the optimal solution

---

## 4. Iterative Deepening DFS (IDDFS)

IDDFS calls DLS repeatedly with **increasing depth limits** starting from 0.

Example:

```
Depth = 0
Depth = 1
Depth = 2
...
Depth = 6  →  Goal found
```

Properties:

* Memory efficient like DFS
* Finds optimal depth like BFS
* Re-explores nodes across iterations

---

# Performance Comparison

| Algorithm | Path Length            | Optimality             | Memory Usage |
| --------- | ---------------------- | ---------------------- | ------------ |
| BFS       | 7 states (optimal)     | Yes                    | High         |
| DFS       | 9 states               | Not guaranteed optimal | Low          |
| DLS       | 9 states (at limit=10) | Not guaranteed optimal | Low          |
| IDDFS     | 7 states (optimal)     | Yes                    | Low          |


| Algorithm | Time Complexity | Space Complexity | 
|-----------|-----------------|------------------|
| BFS       | O(b^d)          | O(b^d)           |
| DFS       | O(b^m)          | O(bm)            | 
| DLS       | O(b^l)          | O(bl)            |
| IDS       | O(b^d)          | O(bd)            | 

*b = branching factor , d = solution depth, l = depth limit, m = maximum depth of search tree

### Observations

**BFS**

* Explores nodes level by level
* Guarantees the shortest path of 7 states
* Requires more memory to store all paths in the queue

**DFS**

* Explores deep paths first
* Finds a valid solution but not necessarily the shortest
* Uses very little memory

**DLS**

* Behaves like DFS but cuts off at the given depth limit of 10
* Finds a solution within the limit but not guaranteed optimal
* Path list used directly for cycle detection — no extra visited set needed

**IDDFS**

* Combines the advantages of BFS and DFS
* Finds the optimal solution matching BFS path length
* Re-explores nodes across iterations resulting in higher total node expansions

---

# Conclusion

This project demonstrates how different **uninformed search strategies** explore the same problem space.

Key insights:

* BFS guarantees optimal solutions but uses more memory.
* DFS uses less memory but may produce non-optimal solutions.
* DLS depends on choosing the right depth limit.
* IDDFS provides optimal solutions with lower memory usage at the cost of repeated node exploration.

These algorithms form the foundation for many **Artificial Intelligence search techniques**.

---
