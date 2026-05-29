# AI-Based Travel Planner using Knowledge Graphs, Ontologies and Case-Based Reasoning

## 1. Objective

The objective of this project is to design an AI-based Travel Planner that reuses existing knowledge bases in the tourism domain rather than manually encoding travel knowledge.

The planner combines:

- Knowledge Graphs
- Ontologies
- Case-Based Reasoning (CBR)
- Constraint Optimization
- Cost Assessment

to generate personalized travel itineraries.

---

# 2. Motivation

Travel planning requires integrating multiple domains:

- Tourist attractions
- Hotels
- Restaurants
- Transportation
- Weather
- Budget constraints
- User preferences

These domains already have curated knowledge bases such as:

| Domain | Knowledge Source |
|----------|------------------|
| Attractions | Wikidata |
| Geographic Data | OpenStreetMap |
| Food Knowledge | FoodOn |
| Wine Pairing | Stanford Wine Ontology |
| User Preferences | Local Database |

Instead of rebuilding this information, the system reuses these knowledge sources.

---

# 3. System Architecture

```text
User Query
     ↓
Intent & Constraint Extraction
     ↓
Knowledge Graph Retrieval
     ↓
Case-Based Reasoning
     ↓
Itinerary Optimization
     ↓
Cost Assessment
     ↓
Travel Plan
```

Example Query:

```text
5-Day Paris Trip
Budget: €1500
Diet: Vegetarian
Interest: History
Pace: Moderate
```

---

# 4. Knowledge Graph Design

## Entity Types

```text
User
City
TouristPlace
Hotel
Restaurant
FoodType
Activity
Transport
```

## Relationship Types

```text
LOCATED_IN
HAS_ACTIVITY
SERVES
LIKES
VISITS
CONNECTED_BY
NEAR
```

### Neo4j Representation

```cypher
CREATE (:TouristPlace {
    wikidata_id:"Q243",
    name:"Eiffel Tower",
    category:"Monument",
    entry_fee:25
})
```

```cypher
MATCH (p:TouristPlace),
      (c:City)

WHERE p.name='Eiffel Tower'
AND c.name='Paris'

CREATE (p)-[:LOCATED_IN]->(c)
```

---

# 5. Knowledge Reuse

## Wikidata Retrieval

Tourist attractions are retrieved using SPARQL.

```sparql
SELECT ?place ?placeLabel
WHERE {
  ?place wdt:P31 wd:Q570116 .

  SERVICE wikibase:label {
      bd:serviceParam wikibase:language "en"
  }
}
LIMIT 20
```

Explanation:

```text
P31 → Instance Of

Q570116 → Tourist Attraction
```

---

## OpenStreetMap Retrieval

Nearby attractions:

```sql
[out:json];

(
 node["tourism"="attraction"]
 (around:5000,48.8584,2.2945);
);

out body;
```

This retrieves attractions within 5 km of the Eiffel Tower.

---

## Ontology Reuse

The Stanford Wine Ontology is reused rather than manually encoding wine-food pairings.

Example:

```ttl
:CabernetSauvignon rdf:type wine:RedWine .

:RedMeatDish
food:recommendedWine
:CabernetSauvignon .
```

Inference:

```text
IF user selects Red Meat Dish

THEN recommend Cabernet Sauvignon
```

---

# 6. Case-Based Reasoning

The planner follows the classical CBR cycle.

```text
Retrieve
Reuse
Revise
Retain
```

## Case Representation

```json
{
  "case_id":101,

  "problem":{
    "destination":"Paris",
    "days":5,
    "budget":1500,
    "diet":"Vegetarian",
    "interest":["History"]
  },

  "solution":{
    "day1":["Eiffel Tower"],
    "day2":["Louvre Museum"]
  },

  "rating":4.8
}
```

---

# 7. Retrieval Strategy

Similarity function:

```text
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

Example:

```text
Query:
Paris
Budget=1500

Case:
Paris
Budget=1600

Similarity=0.93
```

The case is retrieved and adapted.

---

# 8. Adaptation

Original Case:

```text
Lunch:
Beef Steak
```

User Constraint:

```text
Vegetarian
```

Adapted Solution:

```text
Lunch:
Vegetarian Lasagna
```

FoodOn ontology provides equivalent food recommendations.

---

# 9. Cost Assessment

The total trip cost is calculated as:

```text
TotalCost

=
FlightCost

+
HotelCost

+
FoodCost

+
EntryFees

+
TransportCost
```

Example:

```text
Flights = €400

Hotels = €700

Food = €200

Transport = €100

Entry Fees = €80

Total = €1480
```

Constraint:

```text
TotalCost ≤ UserBudget
```

---

# 10. Itinerary Optimization

Objective:

```text
Minimize

TravelTime
+
BudgetDeviation
-
PreferenceScore
```

Constraints:

```text
TotalCost ≤ Budget

TravelTimePerDay ≤ 8 Hours

AtLeastOneHotelPerCluster

AtLeastTwoMealsPerDay
```

Implemented using Google OR-Tools.

---

# 11. Technology Stack

| Layer | Tool |
|---------|--------|
| Graph Database | Neo4j |
| Ontology Engine | RDFLib |
| Ontology Design | Protégé |
| Knowledge Sources | Wikidata, OSM, FoodOn |
| Backend | Python |
| Optimization | OR-Tools |
| Storage | SQLite |

---

# 12. Conclusion

The proposed Travel Planner demonstrates how Knowledge Graphs, Ontologies, Case-Based Reasoning and Optimization can be combined to create an intelligent and explainable travel recommendation system.