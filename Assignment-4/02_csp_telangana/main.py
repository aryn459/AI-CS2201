import networkx as nx
import matplotlib.pyplot as plt
from all_districts import districts, neighbors

colors = ["red", "green", "blue", "yellow"]

def ok(district, color, assignment):
    for neighbor in neighbors.get(district, []):
        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False
    return True


def solve(assignment):
    if len(assignment) == len(districts):
        return assignment

    for district in districts:
        if district not in assignment:
            break

    for color in colors:
        if ok(district, color, assignment):
            assignment[district] = color

            result = solve(assignment)
            if result is not None:
                return result

            del assignment[district]

    return None

ans = solve({})
G = nx.Graph()

for district in districts:
    G.add_node(district)

for district in neighbors:
    for neighbor in neighbors[district]:
        G.add_edge(district, neighbor)


node_colors = []
for district in G.nodes():
    node_colors.append(ans[district])

plt.figure(figsize=(18,14))

pos = nx.spring_layout(G, k=1.2, seed=10)
nx.draw_networkx_edges(G, pos, edge_color="#888", width=1.2)

nx.draw_networkx_nodes(
    G, pos,
    node_color=node_colors,
    node_size=1100,
    edgecolors="black",
    linewidths=1
)

nx.draw_networkx_labels(
    G, pos,
    font_size=7,
    font_family="sans-serif"
)

plt.title("Telangana District Graph Coloring (CSP)", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.show()