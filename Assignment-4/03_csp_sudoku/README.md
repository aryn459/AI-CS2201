# Sudoku Solver using Constraint Satisfaction Problem (CSP)

## Overview

This project implements a Sudoku solver using the Constraint Satisfaction Problem (CSP) approach. The solution is based on a backtracking search algorithm that assigns values to empty cells while ensuring all constraints are satisfied.

## Problem Description

Sudoku is a 9×9 grid puzzle where the objective is to fill the grid such that:

* Each row contains numbers from 1 to 9 without repetition
* Each column contains numbers from 1 to 9 without repetition
* Each 3×3 subgrid contains numbers from 1 to 9 without repetition

Empty cells are represented by `0`.

## Approach

The solver uses a basic CSP backtracking approach:

1. Select an unassigned cell
2. Try assigning values from 1 to 9
3. Check if the assignment satisfies all constraints
4. Recursively continue with the next cell
5. Backtrack if a conflict occurs

## Features

* Simple and clear implementation
* Uses only consistency checking and backtracking
* Works for any valid 9×9 Sudoku puzzle

## How to Run

1. Ensure Python is installed on your system
2. Copy the code into a `.py` file (e.g., `sudoku.py`)
3. Run the file using:

   ```
   python sudoku.py
   ```

## Input Format

* The Sudoku board is defined as a 2D list
* Empty cells are represented by `0`

Example:

```
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    ...
]
```

## Output

* The completed Sudoku grid is printed to the console
* If no solution exists, an appropriate message is displayed

## File Structure

* `sudoku.py` – Main implementation file

## Limitations

* Does not include advanced optimizations (e.g., heuristics or constraint propagation)
* Performance may be slower for complex puzzles

## Conclusion

This implementation demonstrates a fundamental CSP-based solution to Sudoku using backtracking and constraint validation. It is suitable for understanding the core concept of constraint satisfaction problems.
