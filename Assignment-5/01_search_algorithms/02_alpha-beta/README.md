# Alpha-Beta Pruning Algorithm Implementation using Game Tree

## Overview

This project implements the **Alpha-Beta Pruning algorithm**, an optimized version of the **Minimax algorithm**, using a dynamically generated game tree. The program constructs an n-ary tree, assigns values to leaf nodes, and evaluates optimal decisions while eliminating unnecessary branches during traversal.

The implementation demonstrates important concepts of **Artificial Intelligence**, particularly adversarial search and optimization techniques used in game-playing agents.

---

## Problem Statement

Construct a game tree of given:

* Depth (root at depth 0)
* Branching factor (number of children per node)

Assign values to the leaf nodes and compute the optimal value at the root using the **Alpha-Beta Pruning algorithm**, assuming:

* One player is **MAX** (tries to maximize score)
* The other player is **MIN** (tries to minimize score)

The algorithm should optimize traversal by pruning branches that cannot affect the final decision.

---

## Constraints

* Leaf nodes contain user-provided integer values
* Internal nodes initially have `None`
* The tree is a full n-ary tree
* Alpha-Beta assumes:

  * Players alternate at each level
  * Root starts as MAX
* The algorithm recursively evaluates nodes while pruning unnecessary branches

---

## Approach

The solution follows a recursive Alpha-Beta strategy:

1. Build a full tree using depth and branching factor
2. Assign values only to leaf nodes
3. Traverse the tree recursively:

   * If MAX level → select maximum of children
   * If MIN level → select minimum of children
4. Maintain:

   * Alpha → best value MAX can guarantee
   * Beta → best value MIN can guarantee
5. Prune branches whenever:

```

alpha >= beta

````

6. Propagate computed values upward to the root

---

## Features

* Dynamic tree construction
* Supports any depth and branching factor
* Level-order (BFS) tree printing
* Efficient pruning of unnecessary branches
* Clear separation of concerns:

* Tree construction
* Value assignment
* Alpha-Beta evaluation
* Includes test cases and sample outputs
* Faster than standard Minimax for larger trees

---

## How to Run

1. Ensure Python is installed
2. Navigate to the project directory
3. Run:

```bash
python main.py
````

4. Provide inputs:

```text
Enter the depth(root- depth 0) for your alpha-beta tree:
Enter the Branching factor for your alpha-beta tree:
```

5. Enter values for all leaf nodes when prompted

---

## Output

The program prints:

* Tree before applying Alpha-Beta Pruning
* Tree after applying Alpha-Beta Pruning (with computed values)

Example:

```text
Tree before alpha-beta:
None
None None
3 5 2 9

Tree after alpha-beta:
5
5 9
3 5 2 9
```

The program may also display pruned branches during execution.

Example:

```text
Pruned subtree at node 7
```

---

## File Structure

```text
.
├── alphabeta.py        # Alpha-Beta Pruning implementation
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
* Alpha-Beta evaluation
* Proper pruning behavior

---

## Output Samples

Sample outputs are provided in the `output_samples/` directory to verify correctness of the implementation.

---

## Time Complexity

Without pruning (Minimax):

O(b^d)

With Alpha-Beta Pruning (best case):

O(b^{d/2})

where:

* ( b ) = branching factor
* ( d ) = depth of tree

Alpha-Beta significantly reduces the number of nodes evaluated.

---

## Limitations

* Performance still depends on tree size
* Best performance requires good move ordering
* Large inputs may require many manual entries
* No heuristic evaluation functions implemented
* Does not include advanced optimizations like:

  * Iterative Deepening
  * Monte Carlo Tree Search
  * Transposition Tables

---

## Conclusion

This project demonstrates a modular implementation of the **Alpha-Beta Pruning algorithm**, an optimized adversarial search technique widely used in Artificial Intelligence and game-playing systems.

By pruning branches that cannot affect the final decision, Alpha-Beta improves the efficiency of Minimax while preserving optimal decision-making.

```
```
