# Assignment 4 – Constraint Satisfaction Problems (CSP)

## Overview

This assignment focuses on solving different problems using the Constraint Satisfaction Problem (CSP) framework. Each problem is modeled with variables, domains, and constraints, and solved using a backtracking approach.

## Objectives

* Understand the formulation of problems as CSPs
* Implement backtracking-based solutions
* Apply constraint checking to ensure valid assignments
* Solve real-world and logical problems using CSP techniques

## Contents

### 1. Australia Map Coloring (`01_csp_australia`)

* Assign colors to regions of Australia
* Ensure no adjacent regions have the same color

### 2. Telangana Map Coloring (`02_csp_telangana`)

* Similar to Australia map coloring
* Applied to districts of Telangana
* Ensures neighboring districts do not share the same color

### 3. Sudoku Solver (`03_csp_sudoku`)

* Solves a 9×9 Sudoku puzzle
* Ensures:

  * No repetition in rows
  * No repetition in columns
  * No repetition in 3×3 subgrids

### 4. Cryptarithmetic Puzzle (`04_csp_crypt-analysis`)

* Solves the equation:

  SEND + MORE = MONEY

* Assigns unique digits to each letter

* Ensures arithmetic correctness and constraint satisfaction

## Approach

All problems are solved using a common CSP strategy:

1. Define variables and domains
2. Select an unassigned variable
3. Assign a value from the domain
4. Check consistency with constraints
5. Recursively continue assignment
6. Backtrack when constraints are violated

## Requirements

* Python 3.x

## File Structure

```
Assignment-4/
│
├── 01_csp_australia/
├── 02_csp_telangana/
├── 03_csp_sudoku/
├── 04_csp_crypt-analysis/
└── README.md
```

## Conclusion

This assignment demonstrates how different types of problems can be effectively modeled and solved using CSP techniques. It highlights the flexibility of backtracking and constraint checking in solving structured problems.
