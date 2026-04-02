# Telangana Map Coloring using CSP

## Overview

This project solves the map coloring problem for the 33 districts of Telangana using a Constraint Satisfaction Problem (CSP) approach. Each district is treated as a node in a graph, and edges represent adjacency between districts. The goal is to assign colors to each district such that no two adjacent districts share the same color.

## Problem Statement

Given a set of regions (districts) and their neighboring relationships, assign colors to each region using a limited number of colors so that adjacent regions have different colors.

## Approach

The problem is solved using backtracking:

* Each district is assigned a color from a predefined set.
* Before assigning a color, it checks whether any neighboring district already has the same color.
* If a conflict occurs, it tries a different color.
* If no valid color is found, the algorithm backtracks.

## Technologies Used

* Python
* networkx
* matplotlib

## How It Works

1. A list of all 33 districts is defined in all_districts.py .
2. An adjacency list represents which districts are neighbors.
3. A backtracking algorithm assigns colors while satisfying constraints.
4. The graph is created using networkx.
5. The final colored graph is displayed using matplotlib.

## How to Run

1. Install required libraries:

   ```
   pip install networkx matplotlib
   ```
2. Run the Python script:

   ```
   python main.py
   ```

## Output

The program displays a graph where:

* Each node represents a district
* Edges represent adjacency
* Node colors represent assigned colors satisfying CSP constraints

## Key Concepts

* Constraint Satisfaction Problem (CSP)
* Backtracking Algorithm
* Graph Representation

## Notes

* The adjacency list is based on approximate district boundaries.
* The solution uses four colors, following the four color theorem.


