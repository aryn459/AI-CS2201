# Knowledge Graphs and Tools for Building Knowledge Graphs

## 1. Introduction

A Knowledge Graph (KG) is a graph-based representation of entities and relationships that models real-world knowledge.

Unlike relational databases, knowledge graphs emphasize semantic relationships and allow efficient traversal between connected entities.

---

# 2. Knowledge Graph Structure

A KG consists of:

## Entities

```text
Paris
Eiffel Tower
Restaurant
Hotel
```

## Relationships

```text
LOCATED_IN
SERVES
LIKES
VISITS
```

## Properties

```text
name
rating
entry_fee
price
```

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

---

# 4. Neo4j Property Graph Model

Node:

```cypher
CREATE (:TouristPlace {
    name:"Louvre Museum",
    rating:4.8
})
```

Relationship:

```cypher
MATCH (u:User)-[:LIKES]->(a:Activity)

MATCH (p:TouristPlace)-[:HAS_ACTIVITY]->(a)

RETURN p.name
```

This query retrieves attractions matching user interests.

---

# 5. Tools for Building Knowledge Graphs

## Graph Databases

### Neo4j

Advantages:

- Property Graph Model
- Cypher Query Language
- Visualization
- Python Integration

### Memgraph

Advantages:

- In-memory architecture
- Streaming graph analytics

### JanusGraph

Advantages:

- Distributed storage
- Massive-scale graphs

### GraphDB

Advantages:

- RDF Triple Store
- Semantic Web support

---

# 6. Knowledge Extraction Tools

## LangChain

Used to:

- Parse documents
- Extract entities
- Build graph structures

## LlamaIndex

Used to:

- Connect external data sources
- Organize retrieved knowledge

## GliNER

Used for:

- Named Entity Recognition
- Zero-shot extraction

Example:

```text
"Eiffel Tower is located in Paris"

Entity 1:
Eiffel Tower

Entity 2:
Paris

Relationship:
LOCATED_IN
```

---

# 7. Ontology Modeling Tools

## Protégé

Used for:

- OWL ontology creation
- Reasoning
- Ontology visualization

Example:

```text
TouristPlace

├── HistoricalPlace
├── Museum
├── Monument
```

---

# 8. Visualization Tools

## Gephi

Graph analytics and visualization.

## Linkurious

Interactive Neo4j graph exploration.

---

# 9. Tool Selection Analysis

Based on assignment requirements:

| Criteria | Neo4j |
|-----------|--------|
| Ease of Use | High |
| Visualization | Excellent |
| Python Support | Excellent |
| Recommendation Systems | Excellent |
| Learning Curve | Low |

Therefore Neo4j was selected.

---

# 10. Conclusion

Knowledge Graphs provide a flexible mechanism for representing interconnected information. Neo4j was chosen because it offers strong visualization, simple querying, and excellent support for recommendation systems.