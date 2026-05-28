# Heuristic Alpha-Beta Pruning Algorithm Implementation using Game Tree

## Overview

This project implements the **Heuristic Alpha-Beta Pruning algorithm**, an optimized version of the **Minimax algorithm** enhanced with **heuristic evaluation functions**. The program constructs a dynamic n-ary game tree, assigns values to nodes, and evaluates optimal decisions while reducing unnecessary computation using Alpha-Beta pruning and heuristic-based cutoff evaluation.

The implementation demonstrates important concepts of **Artificial Intelligence**, particularly:

* Adversarial Search
* Game Tree Evaluation
* Optimization Techniques
* Heuristic Decision-Making

---

## Problem Statement

Construct a game tree using:

* Depth (root at depth 0)
* Branching factor (number of children per node)

Assign values to the leaf nodes and determine the optimal value at the root using the **Heuristic Alpha-Beta Pruning algorithm**, assuming:

* One player is **MAX** (tries to maximize score)
* One player is **MIN** (tries to minimize score)

The algorithm should:

* Prune unnecessary branches
* Use heuristic evaluation at cutoff depth instead of exploring the entire tree

---

## Constraints

* Leaf nodes contain integer values
* Internal nodes initially contain `None`
* The tree is a full n-ary tree
* Root node starts as MAX
* MAX and MIN alternate at every level
* Search may terminate early using cutoff depth
* Heuristic values estimate node utility for incomplete search

---

## Approach

The implementation follows a recursive Heuristic Alpha-Beta strategy:

1. Build a complete game tree using depth and branching factor
2. Assign values to leaf nodes
3. Traverse recursively:

   * MAX node → choose maximum value
   * MIN node → choose minimum value
4. Maintain:

   * Alpha → best value MAX can guarantee
   * Beta → best value MIN can guarantee
5. Prune unnecessary branches whenever:

```text
alpha >= beta
```

6. If cutoff depth is reached:

   * Apply heuristic function
   * Estimate node utility instead of exploring deeper

7. Propagate computed values upward to determine the optimal root value

---

## Heuristic Function

The heuristic function estimates node quality using:

* Average child node values
* Depth-based adjustment

Formula:

```text
heuristic = average(child_values) - depth
```

This heuristic:

* Estimates future outcomes
* Prefers faster winning paths
* Reduces search complexity
* Produces near-optimal decisions without full traversal

---

## Features

* Dynamic tree construction
* Supports any depth and branching factor
* Alpha-Beta pruning optimization
* Heuristic evaluation support
* Cutoff depth search
* Level-order (BFS) tree printing
* Detection and printing of pruned/ignored subtrees
* Modular implementation
* Includes test cases and output samples

---

## How to Run

1. Ensure Python is installed
2. Navigate to the project directory
3. Run:

```bash
python main.py
```

4. Provide inputs:

```text
Enter the depth(root- depth 0) for your alpha-beta tree:
Enter the Branching factor for your alpha-beta tree:
```

5. Enter values for all leaf nodes when prompted

---

## Output

The program prints:

* Tree before applying heuristic Alpha-Beta pruning
* Heuristic evaluations at cutoff nodes
* Pruned/ignored subtrees
* Tree after evaluation

Example:

```text
Tree before alpha-beta heuristic:
None 
None None 
None None None None 
1 2 3 4 5 6 7 8 
Heuristic value at node = 1
Heuristic value at node = 2
Heuristic value at node = 3
Pruned subtree at node 3
Heuristic value at node = 5
Heuristic value at node = 6
Heuristic value at node = 7
Pruned subtree at node 7
Tree after alpha-beta heuristic:
6 
2 6 
2 3 6 7 
1 2 3 4 5 6 7 8 
```

---

## File Structure

```text
.
├── alphabeta.py        # Heuristic Alpha-Beta implementation
├── tree.py             # Tree construction and printing
├── main.py             # Main execution file
├── testcases/          # Test case files
│   ├── test1.txt
│   ├── test2.txt
├── output_samples/     # Expected outputs
├── README.md           # Documentation
```

---

## Test Cases

Test cases are included in the `testcases/` directory.

Each test case contains:

* Tree depth
* Branching factor
* Leaf node values
* Heuristic cutoff depth

These validate:

* Tree construction
* Correct heuristic evaluation
* Proper Alpha-Beta pruning
* Correct propagation of optimal values

---

## Output Samples

Expected outputs are included in the `output_samples/` folder for verification and comparison.

---

## Time Complexity

### Standard Minimax

```text
O(b^d)
```

### Alpha-Beta Pruning (Best Case)

```text
O(b^(d/2))
```

### Heuristic Alpha-Beta

Effective complexity is further reduced because:

* Search terminates early
* Heuristic evaluation avoids full traversal

where:

* `b` = branching factor
* `d` = depth of tree

---

## Advantages of Heuristic Alpha-Beta

* Faster than standard Minimax
* Reduces unnecessary computation
* Handles larger search trees efficiently
* Produces near-optimal decisions
* Practical for real-world AI systems

---

## Limitations

* Heuristic evaluation may not always produce exact optimal results
* Accuracy depends on heuristic quality
* Poor heuristics can reduce decision quality
* Large trees may still require significant computation

---

## Future Improvements

Possible extensions include:

* Better heuristic functions
* Move ordering optimization
* Iterative Deepening
* Monte Carlo Tree Search
* Transposition Tables
* Real game implementations (Chess, Tic-Tac-Toe, Connect Four)

---

## Conclusion

This project demonstrates an efficient implementation of the **Heuristic Alpha-Beta Pruning algorithm** using dynamically generated game trees.

By combining:

* Minimax decision-making
* Alpha-Beta pruning
* Heuristic evaluation

the algorithm significantly reduces computational complexity while still producing intelligent decisions, making it highly suitable for Artificial Intelligence applications and adversarial search problems.
