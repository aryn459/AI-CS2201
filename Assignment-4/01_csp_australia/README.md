# Map Coloring using CSP (Australia)

This project implements the Map Coloring problem using a Constraint Satisfaction Problem (CSP) approach in Python.

The objective is to assign colors to each state of Australia such that no two neighboring states share the same color.

---

## States Considered

* WA (Western Australia)
* NT (Northern Territory)
* Q (Queensland)
* SA (South Australia)
* NSW (New South Wales)
* V (Victoria)
* T (Tasmania)

---

## Colors Used

* Red
* Green
* Blue

---

## Constraints

Adjacent states must not have the same color.

Examples:

* WA is adjacent to NT and SA
* SA is adjacent to WA, NT, Q, NSW, and V
* NSW is adjacent to Q, SA, and V

---

## Approach

* Each state is treated as a variable
* Colors represent the domain of possible values
* Constraints ensure that neighboring states have different colors
* A backtracking algorithm is used to find a valid assignment

---

## How to Run

1. Ensure Python is installed
2. Save the code in a `.py` file
3. Run the file using:

```bash
python main.py
```

---

## Sample Output

```
WA: Red
NT: Green
Q: Red
SA: Blue
NSW: Green
V: Red
T: Red
```

---

## Notes

* This is a basic implementation of CSP using backtracking
* It does not include optimizations such as heuristics or forward checking
* The output may vary depending on the order of assignments
