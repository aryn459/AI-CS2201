from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "yourpassword"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

travel_cases = [
    {
        "case_id": 101,
        "destination": "Paris",
        "days": 5,
        "budget": 1600,
        "diet": "Non-Vegetarian",
        "interest": "History",
        "itinerary": [
            "Eiffel Tower",
            "Louvre Museum"
        ],
        "lunch": "Beef Steak",
        "rating": 4.8
    }
]

user_query = {
    "destination": "Paris",
    "days": 5,
    "budget": 1500,
    "diet": "Vegetarian",
    "interest": "History"
}


def create_knowledge_graph():

    with driver.session() as session:

        session.run("""
        MATCH (n)
        DETACH DELETE n
        """)

        session.run("""

        CREATE (c:City {
            name:'Paris'
        })

        CREATE (a:Activity {
            name:'History'
        })

        CREATE (p1:TouristPlace {
            name:'Eiffel Tower',
            entry_fee:25
        })

        CREATE (p2:TouristPlace {
            name:'Louvre Museum',
            entry_fee:20
        })

        CREATE (r:Restaurant {
            name:'Vegetarian Delight',
            cuisine:'Vegetarian',
            meal_cost:25
        })

        CREATE (p1)-[:HAS_ACTIVITY]->(a)
        CREATE (p2)-[:HAS_ACTIVITY]->(a)

        CREATE (p1)-[:LOCATED_IN]->(c)
        CREATE (p2)-[:LOCATED_IN]->(c)

        CREATE (r)-[:LOCATED_IN]->(c)

        """)


def destination_similarity(a, b):
    return 1 if a == b else 0


def budget_similarity(a, b):
    return 1 - abs(a - b) / max(a, b)


def diet_similarity(a, b):
    return 1 if a == b else 0


def interest_similarity(a, b):
    return 1 if a == b else 0


def retrieve_case(query):

    best_case = None
    best_score = -1

    for case in travel_cases:

        score = (
            0.30 * destination_similarity(
                query["destination"],
                case["destination"]
            )
            +
            0.25 * budget_similarity(
                query["budget"],
                case["budget"]
            )
            +
            0.20 * diet_similarity(
                query["diet"],
                case["diet"]
            )
            +
            0.25 * interest_similarity(
                query["interest"],
                case["interest"]
            )
        )

        if score > best_score:
            best_score = score
            best_case = case

    return best_case, round(best_score, 2)


def adapt_case(case, query):

    adapted = case.copy()

    if query["diet"] == "Vegetarian":

        if adapted["lunch"] == "Beef Steak":

            adapted["lunch"] = "Vegetarian Lasagna"

    adapted["budget"] = query["budget"]

    return adapted


def calculate_cost():

    flight_cost = 400
    hotel_cost = 700
    food_cost = 200
    transport_cost = 100
    entry_fees = 45

    total = (
        flight_cost
        + hotel_cost
        + food_cost
        + transport_cost
        + entry_fees
    )

    return total


create_knowledge_graph()
case, similarity = retrieve_case(user_query)
adapted_case = adapt_case(case, user_query)
total_cost = calculate_cost()

print("\n=== AI Travel Planner ===")

print("\nUser Query")
print(user_query)

print("\nRetrieved Case")
print(case["case_id"])

print("\nSimilarity Score")
print(similarity)

print("\nAdapted Travel Plan")

for day, place in enumerate(
        adapted_case["itinerary"],
        start=1):

    print(f"Day {day}: {place}")

print("\nLunch Recommendation")
print(adapted_case["lunch"])

print("\nCost Assessment")
print("Estimated Cost =", total_cost)

if total_cost <= user_query["budget"]:
    print("Within Budget")
else:
    print("Budget Exceeded")

driver.close()