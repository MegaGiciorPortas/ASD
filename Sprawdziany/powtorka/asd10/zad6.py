from collections import deque


def drzewo(G: list[list[tuple[int, int]]]):
    n = len(G)

    dist = [float("inf") for _ in range(n)]
    dist[0] = 0
    Q = deque()
    Q.append(0)

    while Q:
        u = Q.popleft()

        for cost, v in G[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + cost
                Q.append(v)

    A = dist.index(max(dist))

    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]

    dist[A] = 0
    Q.append(A)

    while Q:
        u = Q.popleft()

        for cost, v in G[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + cost
                parent[v] = u
                Q.append(v)

    B = dist.index(max(dist))

    total_cost = dist[B]
    current = B

    best_index = -1
    best_value = float("inf")

    while current != -1:
        kandydat = max(dist[current], total_cost - dist[current])

        if kandydat < best_value:
            best_value = kandydat
            best_index = current

        current = parent[current]

    return best_index
