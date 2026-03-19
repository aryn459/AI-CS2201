# Dijkstra Algorithm on Road Network

This module implements Dijkstra’s algorithm to compute shortest distances from a selected city to all other cities.

---

## Description

* The graph is loaded from a CSV file
* Each row represents a road between two cities
* The graph is undirected
* Distances are treated as edge weights

---

## Dataset

```
../data/india_road_network.csv
```

Format:

```
city1,city2,distance
Delhi,Mumbai,1420
Delhi,Kolkata,1530
```

---

## Run

```
python main.py
```

---

## Working

* Uses a priority queue
* Expands node with minimum distance
* Updates distances for neighbors

---

## Output

Prints shortest distances from the chosen start city.

---

## Conclusion

Dijkstra’s algorithm guarantees optimal shortest paths for graphs with non-negative edge weights.
