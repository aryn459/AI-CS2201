from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

with driver.session() as session:

    session.run("""
    MATCH (n)
    DETACH DELETE n
    """).consume()

    session.run("""
    CREATE (:User {
        name:'Peter'
    })
    """).consume()

    session.run("""
    CREATE (:Activity {name:'History'})
    """).consume()

    session.run("""
    CREATE (:Activity {name:'Art'})
    """).consume()

    session.run("""
    CREATE (:Activity {name:'Architecture'})
    """).consume()

    session.run("""
    CREATE (:Activity {name:'Photography'})
    """).consume()

    # Create City
    session.run("""
    CREATE (:City {
        name:'Paris'
    })
    """).consume()

    session.run("""
    CREATE (:TouristPlace {
        name:'Louvre Museum',
        rating:4.8,
        entry_fee:20
    })
    """).consume()

    session.run("""
    CREATE (:TouristPlace {
        name:'Eiffel Tower',
        rating:4.9,
        entry_fee:30
    })
    """).consume()

    session.run("""
    CREATE (:TouristPlace {
        name:'Notre Dame Cathedral',
        rating:4.7,
        entry_fee:15
    })
    """).consume()

    session.run("""
    CREATE (:TouristPlace {
        name:'Versailles Palace',
        rating:4.8,
        entry_fee:25
    })
    """).consume()

    session.run("""
    CREATE (:Restaurant {
        name:'French Delight',
        rating:4.6,
        price:25
    })
    """).consume()

    session.run("""
    MATCH (u:User {name:'Peter'}),
          (a:Activity {name:'History'})
    CREATE (u)-[:LIKES]->(a)
    """).consume()

    session.run("""
    MATCH (u:User {name:'Peter'}),
          (a:Activity {name:'Art'})
    CREATE (u)-[:LIKES]->(a)
    """).consume()

    session.run("""
    MATCH (p:TouristPlace {name:'Louvre Museum'}),
          (a:Activity {name:'Art'})
    CREATE (p)-[:HAS_ACTIVITY]->(a)
    """).consume()

    session.run("""
    MATCH (p:TouristPlace {name:'Louvre Museum'}),
          (a:Activity {name:'History'})
    CREATE (p)-[:HAS_ACTIVITY]->(a)
    """).consume()

    session.run("""
    MATCH (p:TouristPlace {name:'Eiffel Tower'}),
          (a:Activity {name:'Photography'})
    CREATE (p)-[:HAS_ACTIVITY]->(a)
    """).consume()

    session.run("""
    MATCH (p:TouristPlace {name:'Eiffel Tower'}),
          (a:Activity {name:'Architecture'})
    CREATE (p)-[:HAS_ACTIVITY]->(a)
    """).consume()

    session.run("""
    MATCH (p:TouristPlace {name:'Notre Dame Cathedral'}),
          (a:Activity {name:'History'})
    CREATE (p)-[:HAS_ACTIVITY]->(a)
    """).consume()

    session.run("""
    MATCH (p:TouristPlace {name:'Notre Dame Cathedral'}),
          (a:Activity {name:'Architecture'})
    CREATE (p)-[:HAS_ACTIVITY]->(a)
    """).consume()

    session.run("""
    MATCH (p:TouristPlace {name:'Versailles Palace'}),
          (a:Activity {name:'History'})
    CREATE (p)-[:HAS_ACTIVITY]->(a)
    """).consume()

    session.run("""
    MATCH (p:TouristPlace {name:'Versailles Palace'}),
          (a:Activity {name:'Art'})
    CREATE (p)-[:HAS_ACTIVITY]->(a)
    """).consume()


    session.run("""
    MATCH (p:TouristPlace),
          (c:City {name:'Paris'})
    CREATE (p)-[:LOCATED_IN]->(c)
    """).consume()

    session.run("""
    MATCH (r:Restaurant),
          (c:City {name:'Paris'})
    CREATE (r)-[:LOCATED_IN]->(c)
    """).consume()

    print("Knowledge Graph Created Successfully!\n")

    count = session.run("""
    MATCH (n)
    RETURN count(n) AS total
    """).single()["total"]

    print(f"Total Nodes: {count}\n")

    result = session.run("""
    MATCH (u:User)-[:LIKES]->(a:Activity)
    MATCH (p:TouristPlace)-[:HAS_ACTIVITY]->(a)

    RETURN DISTINCT
           p.name AS place,
           p.rating AS rating,
           p.entry_fee AS fee

    ORDER BY rating DESC
    """)

    print("===== RECOMMENDED TOURIST PLACES =====\n")

    for record in result:
        print(f"Place      : {record['place']}")
        print(f"Rating     : {record['rating']}")
        print(f"Entry Fee  : ${record['fee']}")
        print("-" * 40)

driver.close()