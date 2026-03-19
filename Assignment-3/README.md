# Dijkstra Algorithm & UGV Path Planning (static/Dynamic) 

This project is part of an Artificial Intelligence assignment. It focuses on implementing different search algorithms for solving path planning problems in both graph-based and grid-based environments.

The project is divided into three parts:

* Dijkstra’s Algorithm on a road network of Indian cities
* A* Algorithm for path planning in a static grid
* Dynamic path planning using replanning in a changing environment

---

## Project Structure

```
ugv_path_planning/
│
├── 01_dijkstra_cities/
├── 02_ugv_static/
├── 03_ugv_dynamic/
│
├── data/
│   └── cities_distances.csv
│
└── outputs/
```

---

## Requirements

Install required libraries using:

```
pip install -r requirements.txt
```

---

## How to Run

### 1. Dijkstra Algorithm

```
cd 01_dijkstra_cities
python main.py
```

### 2. Static UGV (A*)

```
cd 02_ugv_static
python main.py
```

### 3. Dynamic UGV

```
cd 03_ugv_dynamic
python main.py
```

---

## Outputs

* Shortest path distances in terminal (Dijkstra)
* Grid-based visualization using matplotlib
* Animated path simulation
* GIF files saved in the `outputs/` folder

---

## Algorithms Used

| Problem      | Algorithm          |
| ------------ | ------------------ |
| Road network | Dijkstra           |
| Static grid  | A*                 |
| Dynamic grid | A* with replanning |

---

## Summary

This project demonstrates how different search algorithms behave in:

* Weighted graphs
* Static environments
* Dynamic environments

It also highlights the limitations of basic approaches in dynamic conditions.
