from queue import PriorityQueue
from math import ceil


def przewodnik_turystyczny(T: list[tuple[int, int, int]], A: int, B: int, K: int):
    max_vert = -1
    for u, v, w in T:
        max_vert = max(max_vert, u, v)

    G = [[] for _ in range(max_vert + 1)]

    for u, v, w in T:
        G[u].append((v, w))
        G[v].append((u, w))

    pq = PriorityQueue()
    pq.put((-float("inf"), A))
    parent = [-1 for _ in range(max_vert + 1)]
    rekordy: list[float | int] = [-1 for _ in range(max_vert + 1)]
    rekordy[A] = float("inf")

    while not pq.empty():
        pojemnosc, vert = pq.get()
        pojemnosc = abs(pojemnosc)

        if pojemnosc < rekordy[vert]:
            continue

        for child, aktualna_pojemnosc in G[vert]:
            propozycja = min(pojemnosc, aktualna_pojemnosc)
            if propozycja > rekordy[child]:
                rekordy[child] = propozycja
                parent[child] = vert
                pq.put((-propozycja, child))
    path = []
    current = B
    while current != -1:
        path.append(current)
        current = parent[current]

    return ceil((K + 1) / rekordy[B]), path[::-1]
