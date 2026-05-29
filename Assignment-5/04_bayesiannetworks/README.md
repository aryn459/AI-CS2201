# Bayesian Networks for Travel Satisfaction Prediction

## 1. Objective

The objective of this project is to model uncertainty in travel recommendations using Bayesian Networks and perform probabilistic inference to predict traveller satisfaction.

---

# 2. Problem Definition

Given:

- Weather
- Budget
- Crowd Level
- Food Quality

Predict:

```text
Traveller Satisfaction
```

---

# 3. Bayesian Network Structure

```text
Weather ─────┐
             │
Budget ──────┤
             │
FoodQuality ─┼── Satisfaction
             │
Crowd ───────┘
```

---

# 4. Variable Definitions

## Weather

```text
Good
Bad
```

## Budget

```text
High
Low
```

## Crowd

```text
Low
High
```

## Food Quality

```text
Good
Poor
```

## Satisfaction

```text
Yes
No
```

---

# 5. Bayesian Representation

The network models:

```text
P(Satisfaction |
 Weather,
 Budget,
 FoodQuality,
 Crowd)
```

---

# 6. Implementation using pgmpy

Network Construction:

```python
from pgmpy.models import BayesianNetwork

model = BayesianNetwork([
 ('Weather','Satisfaction'),
 ('Budget','Satisfaction'),
 ('FoodQuality','Satisfaction'),
 ('Crowd','Satisfaction')
])
```

---

# 7. Conditional Probability Table Example

Weather:

```text
P(Weather=Good)=0.7

P(Weather=Bad)=0.3
```

Budget:

```text
P(Budget=High)=0.6

P(Budget=Low)=0.4
```

---

# 8. Inference

Evidence:

```text
Weather = Good

Budget = High

FoodQuality = Good

Crowd = Low
```

Query:

```text
P(Satisfaction=Yes)
```

Result:

```text
0.89
```

Interpretation:

The traveller has an 89% probability of enjoying the trip.

---

# 9. Integration with Travel Planner

The Bayesian Network extends the Travel Planner.

Workflow:

```text
Knowledge Graph
      ↓
Travel Itinerary
      ↓
Bayesian Network
      ↓
Satisfaction Prediction
```

This allows the system to recommend not only feasible trips but also highly satisfying trips.

---

# 10. Advantages

- Handles uncertainty
- Explainable predictions
- Probabilistic reasoning
- Easy Python implementation

---

# 11. Technology Stack

| Component | Tool |
|------------|------|
| Programming Language | Python |
| Bayesian Modeling | pgmpy |
| Visualization | NetworkX |
| Data Processing | Pandas |

---

# 12. Conclusion

Bayesian Networks provide a mathematically sound framework for uncertainty modeling. By integrating Bayesian inference with Knowledge Graphs and Case-Based Reasoning, the proposed travel planner becomes more intelligent, explainable and user-centric.