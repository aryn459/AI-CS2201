# Tourism Knowledge Graph using Neo4j

## Overview

This project demonstrates the implementation of a Tourism Knowledge Graph using Neo4j.

The graph represents tourism-related entities such as users, activities, cities, restaurants, and tourist attractions, along with the relationships between them.

The project demonstrates:

* Knowledge Graph Modeling
* Entity and Relationship Representation
* Graph Traversal
* Cypher Queries
* Recommendation Generation

---

## Knowledge Graph Structure

### Entities

```text
User
Activity
TouristPlace
City
Restaurant
```

### Relationships

```text
LIKES
HAS_ACTIVITY
LOCATED_IN
```

---

## Example Graph

```text
(Peter)
  │
LIKES
  │
 ├── History
 │      │
 │      ├── Louvre Museum
 │      ├── Notre Dame Cathedral
 │      └── Versailles Palace
 │
 └── Art
        │
        ├── Louvre Museum
        └── Versailles Palace

All Tourist Places
        │
   LOCATED_IN
        │
      Paris
```

---

## Technologies Used

| Component            | Technology     |
| -------------------- | -------------- |
| Programming Language | Python         |
| Graph Database       | Neo4j          |
| Query Language       | Cypher         |
| Graph Model          | Property Graph |

---

## Installation

Install dependencies:

```bash
pip install neo4j
```

Update the Neo4j credentials inside `main.py`:

```python
URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"
```

---

## Running the Project

```bash
python main.py
```



## Sample Output

```text
Knowledge Graph Created Successfully!

Total Nodes: 11

===== RECOMMENDED TOURIST PLACES =====

Place      : Louvre Museum
Rating     : 4.8
Entry Fee  : $20
----------------------------------------

Place      : Versailles Palace
Rating     : 4.8
Entry Fee  : $25
----------------------------------------

Place      : Notre Dame Cathedral
Rating     : 4.7
Entry Fee  : $15
----------------------------------------
```


## Features Implemented

* Knowledge Graph Creation
* Node Creation
* Relationship Creation
* Property Graph Representation
* Cypher Query Execution
* Tourism Recommendation Query

---

## Conclusion

This project demonstrates how Neo4j can be used to model tourism knowledge as a graph and retrieve recommendations through graph traversal and Cypher queries.
