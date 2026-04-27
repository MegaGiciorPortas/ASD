# BFS na grafie wazonym gdzie wagi to relatywnie male liczby naturalne
# Lista sasiedztwa
# O((V + E) * d)

from collections import deque


def bfs_split(G: list[list[tuple[int, int]]], vert: int) -> list[int]:
    n = len(G)

    Q: deque[tuple[int, int, int]] = deque()
    Q.append((vert, 0, 0))

    dist: list[int] = [0 for _ in range(n)]
    vis: list[bool] = [False for _ in range(n)]

    while len(Q) > 0:
        curr, delay, curr_dist = Q.popleft()
        if delay > 0:
            Q.append((curr, delay - 1, curr_dist + 1))
            continue

        if vis[curr]:
            continue

        vis[curr] = True
        dist[curr] = curr_dist

        for child, w in G[curr]:
            if not vis[child]:
                Q.append((child, w - 1, curr_dist + 1))

    return dist
