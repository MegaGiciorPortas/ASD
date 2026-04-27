from collections import deque


def main_function(G: list[list[int]], s: int, t: int):
    n = len(G)
    visited = [False for _ in range(n + 1)]
    parent = [-1 for _ in range(n + 1)]
    dist = [-1 for _ in range(n + 1)]

    def bfs(visited, dist, s):
        Q = deque()
        Q.append(s)
        dist[s] = 0
        visited[s] = True

        while Q:
            u = Q.popleft()

            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    dist[v] = dist[u] + 1
                    Q.append(v)

    bfs(visited, dist, s)

    if not visited[t]:
        return False

    sciezka = [t]
    vert = parent[t]
    while vert != -1:
        sciezka.append(vert)
        vert = parent[vert]

    sciezka = sciezka[::-1]

    for i in range(len(sciezka) - 1):
        G[sciezka[i]].remove(sciezka[i + 1])
        G[sciezka[i + 1]].remove(sciezka[i])

        temp_visited = [False for _ in range(n + 1)]
        temp_dist = [-1 for _ in range(n + 1)]

        bfs(temp_visited, temp_dist, s)

        if not temp_visited[t] or temp_dist[t] > dist[t]:
            return True

        G[sciezka[i]].append(sciezka[i + 1])
        G[sciezka[i + 1]].append(sciezka[i])

    return False
