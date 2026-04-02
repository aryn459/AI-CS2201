# Cryptarithmetic Puzzle Solver using CSP

## Overview

This project implements a solver for a cryptarithmetic puzzle using a Constraint Satisfaction Problem (CSP) approach. The goal is to assign digits to letters such that the arithmetic equation is satisfied.

## Problem Statement

Solve the following puzzle:

TWO + TWO = FOUR

Each letter represents a unique digit from 0 to 9.

## Constraints

* Each letter must be assigned a distinct digit
* Digits range from 0 to 9
* Leading letters cannot be zero:

  * T ≠ 0
  * F ≠ 0
* The arithmetic equation must hold true:

  TWO + TWO = FOUR

## Approach

The solution uses a backtracking-based CSP approach:

1. Select an unassigned variable (letter)
2. Assign a value from the domain (0–9)
3. Check if the assignment is consistent with constraints
4. Recursively continue assigning values
5. Backtrack if a constraint is violated

## Features

* Simple and clear CSP formulation
* Uses only backtracking and consistency checking
* No heuristics or optimizations included

## How to Run

1. Ensure Python is installed on your system
2. Save the code in a file (e.g., `crypt_solver.py`)
3. Run the program using:

   ```
   python crypt_solver.py
   ```

## Output

* Displays the digit assigned to each letter if a solution is found
* Prints verification of the equation
* Prints a message if no solution exists

## File Structure

* `crypt_solver.py` – Main implementation file

## Limitations

* Does not use advanced techniques like heuristics or constraint propagation
* May take longer for more complex puzzles

## Conclusion

This implementation demonstrates a basic CSP-based solution to a cryptarithmetic problem using backtracking and constraint validation.
