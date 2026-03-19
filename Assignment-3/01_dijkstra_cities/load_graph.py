import csv
from collections import defaultdict

def load_graph(file_path):
    graph = defaultdict(list)

    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            c1 = row['city1']
            c2 = row['city2']
            dist = int(row['distance'])

            graph[c1].append((c2, dist))
            graph[c2].append((c1, dist))

    return graph