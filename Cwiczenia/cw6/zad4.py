# O((V+E)+(V+E)) = O(2*(V+E))
#  O(V+E)


def main_function(G: list[list[tuple[int, int]]], start: int):
    n = len(G)
    result: list[int] = []
    dist: list[int | float] = [float("inf") for _ in range(n + 1)]

    def topological_sort(start: int):
        nonlocal n
        visited = [False for _ in range(n + 1)]

        def dfs(u):
            visited[u] = True
            for cost, v in G[u]:
                if not visited[v]:
                    dfs(v)

            result.append(u)

        dfs(start)

    topological_sort(start)
    result = result[::-1]
    dist[start] = 0

    for vert in result:
        for cost, v in G[vert]:
            if dist[vert] + cost < dist[v]:
                dist[v] = dist[vert] + cost

    return dist
