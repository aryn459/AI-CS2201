from load_graph import load_graph
from dijkstra import dijkstra

graph = load_graph("../data/cities_distances.csv")

start = "Delhi"

dist = dijkstra(graph, start)

print("Shortest distances from", start)
for city in dist:
    print(city, ":", dist[city])