# Minimax Algorithm Implementation using Game Tree

## Overview

This project implements the **Minimax algorithm** using a dynamically generated game tree. The program constructs an n-ary tree, assigns values to leaf nodes, and evaluates optimal decisions by propagating values upward based on Minimax strategy.

The implementation demonstrates core concepts of **Artificial Intelligence**, particularly decision-making in adversarial environments.

---

## Problem Statement

Construct a game tree of given:

* Depth (root at depth 0)
* Branching factor (number of children per node)

Assign values to the leaf nodes and compute the optimal value at the root using the **Minimax algorithm**, assuming:

* One player is **MAX** (tries to maximize score)
* The other player is **MIN** (tries to minimize score)

---

## Constraints

* Leaf nodes contain user-provided integer values
* Internal nodes initially have `None`
* The tree is a full n-ary tree
* Minimax assumes:

  * Players alternate at each level
  * Root starts as MAX
* The algorithm must recursively evaluate all nodes

---

## Approach

The solution follows a recursive Minimax strategy:

1. Build a full tree using depth and branching factor
2. Assign values only to leaf nodes
3. Traverse the tree recursively:

   * If MAX level → select maximum of children
   * If MIN level → select minimum of children
4. Propagate computed values upward to the root

---

## Features

* Dynamic tree construction
* Supports any depth and branching factor
* Level-order (BFS) tree printing
* Clear separation of concerns:

  * Tree construction
  * Value assignment
  * Minimax evaluation
* Includes test cases and sample outputs

---

## How to Run

1. Ensure Python is installed
2. Navigate to the project directory
3. Run:

```
python main.py
```

4. Provide inputs:

```
Enter the depth(root- depth 0) for your minmax tree:
Enter the Branching factor for your minmax tree:
```

5. Enter values for all leaf nodes when prompted

---

## Output

The program prints:

* Tree before applying Minimax
* Tree after applying Minimax (with computed values)

Example:

```
Tree before minmax:
None
None None
3 5 2 9

Tree after minmax:
5
5 9
3 5 2 9
```

---

## File Structure

```
.
├── minimax.py          # Minimax algorithm implementation
├── tree.py             # Tree creation, assignment, and printing
├── main.py             # Main execution file
├── testcases/          # Input test cases
│   ├── test1.txt
│   ├── test2.txt
├── output_samples/     # Expected outputs
├── README.md           # Documentation
```

---

## Test Cases

Test cases are provided in the `testcases/` folder:

* Each file contains:

  * Depth
  * Branching factor
  * Leaf node values

These validate correctness of:

* Tree construction
* Minimax evaluation

---

## Output Samples

Sample outputs are provided in the `output_samples/` directory to verify correctness of the implementation.

---

## Limitations

* Time complexity grows exponentially:
  [
  O(b^d)
  ]
  where:

  * ( b ) = branching factor
  * ( d ) = depth

* No optimization techniques like:

  * Alpha-Beta pruning
  * Heuristics

* Large inputs may require many manual entries

---

## Conclusion

This project demonstrates a clear and modular implementation of the **Minimax algorithm** using recursion and tree structures. It highlights fundamental AI concepts such as adversarial search and decision-making.


---
