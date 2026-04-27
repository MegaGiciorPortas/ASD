# napisać Dijkstrę dla treningu
# G: list[list[tuple[int,int]]]
#                   weight, v

import heapq


# O((V+E)logV)
def dijkstra(G: list[list[tuple[int, int]]], start: int):
    # dodajemy przedstawienie grafu ważonego oraz wierzchołek od którego zaczynamy algorytm
    n = len(G)
    Q = []
    dist = [float("inf") for _ in range(n + 1)]
    parent = [-1 for _ in range(n + 1)]

    dist[start] = 0
    heapq.heappush(Q, [0, start])

    while Q:
        weight, u = heapq.heappop(Q)

        if weight > dist[u]:
            continue

        for cost, child in G[u]:
            if cost + dist[u] < dist[child]:
                dist[child] = cost + dist[u]
                parent[child] = u
                heapq.heappush(Q, [dist[child], child])
    return dist, parent
