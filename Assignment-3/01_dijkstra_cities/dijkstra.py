import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    while pq:
        curr_dist, node = heapq.heappop(pq)

        for neigh, weight in graph[node]:
            new_dist = curr_dist + weight

            if new_dist < dist[neigh]:
                dist[neigh] = new_dist
                heapq.heappush(pq, (new_dist, neigh))

    return dist