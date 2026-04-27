import heapq
from collections import deque
from math import ceil


def rozwiazanie_dijkstra(T: list[tuple[int, int, int]], K: int, A: int, B: int):
    n = 0
    for u, v, cost in T:
        n = max(n, u, v)

    G = [[] for _ in range(n + 1)]

    for u, v, cost in T:
        G[u].append((cost, v))
        G[v].append((cost, u))

    dist: list[int | float] = [-1 for _ in range(n + 1)]
    dist[A] = float("inf")
    q = []
    q.append((-float("inf"), A))

    while q:
        autokar, vert = heapq.heappop(q)
        autokar *= -1

        if autokar < dist[vert]:
            continue

        for cost, child in G[vert]:
            result = min(dist[vert], cost)

            if result > dist[child]:
                dist[child] = result
                heapq.heappush(q, (result * -1, child))

    return ceil((K + 1) / dist[B])


def rozwiazanie_bfs_binsearch(T: list[tuple[int, int, int]], K: int, A: int, B: int):
    n = 0
    for u, v, cost in T:
        n = max(n, u, v)

    G = [[] for _ in range(n + 1)]
    pojemnosci = []

    for u, v, cost in T:
        G[u].append((cost, v))
        G[v].append((cost, u))
        pojemnosci.append(cost)

    def bfs(G: list[list[int]], A: int, B: int, autokar: int):
        q = deque()
        q.append(A)
        dist = [-1 for _ in range(len(G) + 1)]
        dist[A] = 0
        visited = [False for _ in range(n + 1)]
        visited[A] = True

        while q:
            u = q.popleft()

            for cost, v in G[u]:
                if not visited[v] and cost >= autokar:
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    q.append(v)

        return dist[B] != -1

    pojemnosci = list(set(pojemnosci))
    pojemnosci.sort()

    left = 0
    right = len(pojemnosci) - 1
    najlepszy_wynik = 0

    while left <= right:
        pivot = (left + right) // 2
        if bfs(G, A, B, pojemnosci[pivot]):
            najlepszy_wynik = pojemnosci[pivot]
            left = pivot + 1
        else:
            right = pivot - 1

    return ceil((K + 1) / najlepszy_wynik)
