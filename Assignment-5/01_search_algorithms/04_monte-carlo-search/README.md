# Monte Carlo Tree Search (MCTS) Implementation using Game Tree

## Overview

This project implements the **Monte Carlo Tree Search (MCTS)** algorithm using a dynamically generated game tree. The program constructs an n-ary tree, assigns values to leaf nodes, and uses randomized simulations to estimate optimal decisions.

Unlike Minimax-based algorithms that systematically explore the entire tree, MCTS uses probabilistic simulations and statistical evaluation to determine promising moves efficiently.

The implementation demonstrates important concepts of **Artificial Intelligence**, including:

* Adversarial Search
* Probabilistic Decision-Making
* Simulation-Based Search
* Exploration vs Exploitation

---

## Problem Statement

Construct a game tree using:

* Depth (root at depth 0)
* Branching factor (number of children per node)

Assign values to leaf nodes and estimate the optimal value at the root using the **Monte Carlo Tree Search (MCTS)** algorithm.

The algorithm should:

* Perform repeated random simulations
* Explore promising nodes
* Statistically evaluate outcomes
* Approximate the best decision at the root

---

## Constraints

* Leaf nodes contain integer values
* Internal nodes initially contain `None`
* The tree is a full n-ary tree
* MCTS performs randomized traversal
* Results may vary between executions due to randomness
* Larger iteration counts improve approximation quality

---

## Approach

The implementation follows the standard Monte Carlo Tree Search procedure:

1. Build a complete game tree

2. Assign values to leaf nodes

3. Perform repeated MCTS iterations consisting of:

   * Selection
   * Expansion
   * Simulation
   * Backpropagation

4. Use statistical information to determine the most promising move

---

## MCTS Phases

### 1. Selection

Starting from the root, repeatedly select the best child node using the **UCT (Upper Confidence Bound applied to Trees)** formula until a leaf or expandable node is reached.

UCT Formula:

```text id="8qlm9t"
UCT = (wins / visits) + c * sqrt(ln(parent_visits) / visits)
```

where:

* `wins` = number of successful simulations
* `visits` = number of node visits
* `c` = exploration constant

---

### 2. Expansion

If the selected node has unexplored children:

* Expand the node
* Add new child nodes into the search tree

---

### 3. Simulation

Perform a random rollout from the selected node until a terminal leaf node is reached.

The leaf value represents the simulation result.

---

### 4. Backpropagation

Propagate the simulation result upward through the visited nodes by updating:

* Visit counts
* Win statistics

---

## Features

* Dynamic tree construction
* Supports any depth and branching factor
* Full Monte Carlo Tree Search implementation
* UCT-based node selection
* Randomized simulations
* Statistical backpropagation
* Level-order (BFS) tree printing
* Includes test cases and output samples
* Demonstrates probabilistic AI search techniques

---

## How to Run

1. Ensure Python is installed
2. Navigate to the project directory
3. Run:

```bash id="r0t5m8"
python main.py
```

4. Provide inputs:

```text id="9zvk9m"
Enter the depth(root- depth 0) for your monte-carlo tree:
Enter the Branching factor for your monte-carlo tree:
```

5. Enter values for all leaf nodes when prompted

---

## Output

The program prints:

* Tree before Monte Carlo Tree Search
* Simulation results
* Estimated optimal root value
* Tree after MCTS evaluation

Example:

```text id="yzz9yv"
Tree before monte-carlo:
None
None None
3 5 2 9

Simulation 1: Result = 5
Simulation 2: Result = 9
Simulation 3: Result = 2

Optimal value: 7.5

Tree after monte-carlo:
7.5
None None
3 5 2 9
```

---

## File Structure

```text id="ck7qgf"
.
├── monte_carlo.py      # Monte Carlo Tree Search implementation
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

Test cases are provided in the `testcases/` directory.

Each file contains:

* Tree depth
* Branching factor
* Leaf node values

These validate:

* Tree construction
* Correct MCTS traversal
* Statistical evaluation
* Proper simulation behavior

---

## Output Samples

Expected outputs are provided in the `output_samples/` directory for result verification.

Due to randomized simulations, outputs may vary slightly between runs.

---

## Time Complexity

The complexity of Monte Carlo Tree Search depends on:

* Number of iterations
* Tree depth
* Branching factor

Approximate complexity:

```text id="j4mnq5"
O(iterations × depth)
```

where:

* `iterations` = number of Monte Carlo simulations
* `depth` = tree depth

Increasing iterations generally improves decision quality.

---

## Advantages of MCTS

* Handles very large search spaces efficiently
* Does not require exhaustive search
* Balances exploration and exploitation
* Suitable for uncertain and probabilistic environments
* Used in modern AI systems such as AlphaGo

---

## Limitations

* Results are approximate, not guaranteed optimal
* Performance depends on iteration count
* Randomness may produce varying outputs
* Slower convergence for extremely large trees
* Requires many simulations for high accuracy

---

## Applications

Monte Carlo Tree Search is widely used in:

* Game AI
* Chess Engines
* Go (AlphaGo)
* Robotics
* Planning Systems
* Decision-Making Systems

---

## Conclusion

This project demonstrates a modular implementation of the **Monte Carlo Tree Search (MCTS)** algorithm using dynamically generated game trees.

By combining:

* Randomized simulations
* Statistical evaluation
* Exploration-exploitation balancing

MCTS efficiently approximates optimal decisions and represents one of the most important modern search techniques in Artificial Intelligence.
