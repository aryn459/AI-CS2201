# Dynamic UGV Path Planning

This module simulates a UGV navigating in a dynamic environment where obstacles change during movement.

---

## Description

* Initial path is computed using A*
* The agent moves step-by-step
* Obstacles are updated dynamically
* Path is recalculated from current position

---

## Features

* Dynamic obstacle simulation
* Continuous replanning
* Real-time visualization
* GIF generation

---

## Run

```
python main.py
```

---

## Approach

* Compute path from current position to goal
* Move one step along the path
* Update environment
* Recompute path

---

## Limitation

* Replanning is done from scratch each time
* More efficient algorithms like D* Lite can be used

---

## Output

* Moving agent on grid
* Changing path due to obstacles
* Animated simulation
* GIF saved in outputs

---

## Conclusion

Dynamic environments require continuous adaptation.
This implementation demonstrates a basic replanning approach using A*.
