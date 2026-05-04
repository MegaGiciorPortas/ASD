def hamilton_path(G: list[list[int]]):
    n = len(G)
    topological_sort: list[int] = []
    visited = [False for _ in range(n)]

    def dfs(u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfs(v)

        topological_sort.append(u)

    for u in range(n):
        if not visited[u]:
            dfs(u)

    topological_sort = topological_sort[::-1]

    for i in range(n - 1):
        if topological_sort[i + 1] not in G[topological_sort[i]]:
            return False
    return True
