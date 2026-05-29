# AI-Based Travel Planner using Knowledge Graphs and Case-Based Reasoning

## Overview

This project implements an AI-Based Travel Planner that combines Knowledge Graphs and Case-Based Reasoning (CBR) to generate personalized travel recommendations.

The system stores tourism knowledge using a Neo4j Knowledge Graph and reuses previous travel experiences to create customized travel plans. It also performs cost assessment to ensure that recommendations satisfy user budget constraints.

---

# Objectives

The objectives of this project are:

* Represent tourism knowledge using a Knowledge Graph.
* Reuse existing travel experiences through Case-Based Reasoning.
* Generate personalized travel recommendations.
* Adapt travel plans according to user preferences.
* Estimate travel costs and validate budget constraints.

---

# System Architecture

```text id="lmn5kv"
User Query
     ↓
Knowledge Graph
     ↓
Case Retrieval
     ↓
Case Adaptation
     ↓
Cost Assessment
     ↓
Travel Plan
```

---

# Knowledge Graph Design

## Entity Types

```text id="z5x35e"
User
City
TouristPlace
Restaurant
Activity
```

## Relationship Types

```text id="djlwmv"
LIKES
HAS_ACTIVITY
LOCATED_IN
```

### Example Graph Structure

```text id="dy7vfr"
(Peter)
    |
  LIKES
    |
(History)

(History)
    |
HAS_ACTIVITY
    |
(Eiffel Tower)

(Eiffel Tower)
    |
LOCATED_IN
    |
(Paris)
```

---

# Case-Based Reasoning

The system follows the classical CBR cycle:

```text id="5n9eyv"
Retrieve
Reuse
Revise
Retain
```

Example stored case:

```json id="m4a7c3"
{
  "case_id": 101,
  "destination": "Paris",
  "days": 5,
  "budget": 1600,
  "diet": "Non-Vegetarian",
  "interest": "History"
}
```

The most similar case is retrieved and adapted to the current user's requirements.

---

# Similarity Function

The similarity score is calculated using:

```text id="kw4b90"
Similarity

=
0.30 × DestinationSimilarity

+
0.25 × BudgetSimilarity

+
0.20 × DietSimilarity

+
0.25 × InterestSimilarity
```

The case with the highest similarity score is selected for adaptation.

---

# Adaptation Strategy

Example:

Original recommendation:

```text id="is71f9"
Lunch:
Beef Steak
```

User preference:

```text id="fxdd6u"
Vegetarian
```

Adapted recommendation:

```text id="u4c0k9"
Lunch:
Vegetarian Lasagna
```

This demonstrates how existing solutions can be modified to satisfy new constraints.

---

# Cost Assessment

Trip cost is calculated using:

```text id="ubig0c"
TotalCost

=
FlightCost
+
HotelCost
+
FoodCost
+
TransportCost
+
EntryFees
```

Example:

```text id="v0cwqb"
Flights = €400

Hotels = €700

Food = €200

Transport = €100

Entry Fees = €45

Total = €1445
```

Constraint:

```text id="2vl50x"
TotalCost ≤ UserBudget
```

---

# Technologies Used

| Component                | Technology           |
| ------------------------ | -------------------- |
| Programming Language     | Python               |
| Graph Database           | Neo4j                |
| Query Language           | Cypher               |
| Knowledge Representation | Knowledge Graph      |
| Reasoning Technique      | Case-Based Reasoning |
| Cost Assessment          | Python               |

---

# Installation

Install the required dependency:

```bash id="rzk3th"
pip install neo4j
```

Configure the Neo4j connection in `main.py`:

```python id="btrwjr"
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "yourpassword"
```

Ensure that the Neo4j database is running before executing the program.

---

# Running the Project

```bash id="5df0eb"
python main.py
```

---

# Sample Output

```text id="n4vl3m"
=== AI Travel Planner ===

User Query
Paris
Budget = 1500
Vegetarian

Retrieved Case
101

Similarity Score
0.93

Adapted Travel Plan

Day 1: Eiffel Tower
Day 2: Louvre Museum

Lunch Recommendation
Vegetarian Lasagna

Cost Assessment
Estimated Cost = 1445

Within Budget
```

---

# Features Implemented

* Knowledge Graph Creation using Neo4j
* Tourism Entity Modeling
* Relationship Representation
* Case-Based Reasoning Retrieval
* Similarity Calculation
* Case Adaptation
* Personalized Recommendations
* Cost Assessment
* Budget Validation

---

# Future Improvements

* Integration with Wikidata
* Integration with OpenStreetMap
* FoodOn Ontology Support
* Stanford Wine Ontology Support
* Dynamic Flight and Hotel Pricing
* Route Optimization using OR-Tools
* Web Interface using Flask

---

# Conclusion

This project demonstrates the use of Knowledge Graphs and Case-Based Reasoning in the travel domain. The system reuses existing travel knowledge, adapts recommendations according to user preferences, and evaluates travel costs to generate personalized travel plans.
