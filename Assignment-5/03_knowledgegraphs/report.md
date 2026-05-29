# Knowledge Graphs and Tools for Building Knowledge Graphs

## 1. Introduction

A Knowledge Graph (KG) is a graph-based representation of entities and relationships that models real-world knowledge.

Unlike relational databases, Knowledge Graphs emphasize semantic relationships and enable efficient traversal between connected entities.

Knowledge Graphs are widely used in recommendation systems, search engines, intelligent assistants, healthcare systems, and travel planning applications.

---

# 2. Knowledge Graph Structure

A Knowledge Graph consists of:

## Entities

Entities represent real-world objects.

Examples:

* Paris
* Louvre Museum
* Restaurant
* Hotel
* User

---

## Relationships

Relationships connect entities.

Examples:

* LOCATED_IN
* HAS_ACTIVITY
* LIKES
* SERVES
* VISITS

---

## Properties

Properties store additional information about entities.

Examples:

* name
* rating
* entry_fee
* price

---

# 3. Tourism Knowledge Graph Example

```text
(User)
   |
LIKES
   |
(History)

(History)
   |
HAS_ACTIVITY
   |
(Louvre Museum)

(Louvre Museum)
   |
LOCATED_IN
   |
(Paris)
```

This structure enables personalized recommendations by traversing relationships between users, activities, and attractions.

---

# 4. Neo4j Property Graph Model

Node Example:

```cypher
CREATE (:TouristPlace {
    name:"Louvre Museum",
    rating:4.8,
    entry_fee:20
})
```

Relationship Example:

```cypher
MATCH (u:User)-[:LIKES]->(a:Activity)

MATCH (p:TouristPlace)-[:HAS_ACTIVITY]->(a)

RETURN p.name
```

---

# 5. Tools for Building Knowledge Graphs

## Graph Databases

### Neo4j

* Property Graph Model
* Cypher Query Language
* Visualization Support
* Python Integration

### Memgraph

* In-memory graph database
* Real-time graph processing

### JanusGraph

* Distributed graph database
* Massive-scale graph storage

### GraphDB

* RDF Triple Store
* Semantic Web support

---

# 6. Knowledge Extraction Tools

### LangChain

Used for:

* Entity Extraction
* Relationship Extraction
* Knowledge Graph Construction

### LlamaIndex

Used for:

* Data Indexing
* Knowledge Organization

### GliNER

Used for:

* Named Entity Recognition
* Zero-shot Entity Extraction

Example:

"Eiffel Tower is located in Paris"

Entities:

* Eiffel Tower
* Paris

Relationship:

* LOCATED_IN

---

# 7. Ontology Modeling Tools

### Protégé

Used for:

* OWL Ontology Creation
* Ontology Visualization
* Reasoning

Example:

```text
TouristPlace

├── Museum
├── HistoricalPlace
├── Monument
```

---

# 8. Visualization Tools

### Gephi

Graph analytics and visualization.

### Linkurious

Interactive Neo4j graph exploration.

---

# 9. Tool Selection Analysis

| Criteria               | Neo4j     |
| ---------------------- | --------- |
| Ease of Use            | High      |
| Visualization          | Excellent |
| Python Support         | Excellent |
| Recommendation Systems | Excellent |
| Learning Curve         | Low       |

Therefore Neo4j was selected for implementation.

---

# 10. Implementation

The implemented system contains:

Entities:

* User
* Activity
* TouristPlace
* City
* Restaurant

Relationships:

* LIKES
* HAS_ACTIVITY
* LOCATED_IN

The graph is stored in Neo4j and queried using Cypher.

---

# 11. Results

Example Query:

```cypher
MATCH (u:User)-[:LIKES]->(a)

MATCH (p:TouristPlace)-[:HAS_ACTIVITY]->(a)

RETURN p.name
```

Output:

```text
Louvre Museum
```

---

# 12. Conclusion

Knowledge Graphs provide a powerful mechanism for representing interconnected information. Neo4j was selected because of its flexibility, visualization capabilities, and strong support for recommendation systems.
