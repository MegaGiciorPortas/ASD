def good_start(G: list[list[int]]):
    n = len(G)
    visited = [False] * n
    topological_sort = []

    def dfs(u, true_key=True):
        visited[u] = true_key

        for v in G[u]:
            if visited[v] != true_key:
                dfs(v, true_key)
        if true_key:
            topological_sort.append(u)

    for u in range(n):
        if not visited[u]:
            dfs(u)

    kandydat = topological_sort[-1]

    dfs(kandydat, False)

    return True not in visited
