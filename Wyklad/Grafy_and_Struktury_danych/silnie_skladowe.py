# Szukanie silnie spojnych skladowych
# Zalozenie : Graf skierowany

# O(V + E)
# lista sasiedztwa
def sss(G: list[list[int]]):
    n = len(G)

    out_colleciton: list[int] = []
    vis = [False] * n

    def dfs(G: list[list[int]], vert: int, spojna: list[int], true_key: bool = True):
        vis[vert] = true_key
        for child in G[vert]:
            if vis[child] != true_key:
                dfs(G, child, spojna, true_key)

        if true_key:
            out_colleciton.append(vert)
        else:
            spojna.append(vert)

    G_T: list[list[int]] = [[] for _ in range(n)]

    for vert in range(n):
        for child in G[vert]:
            G_T[child].append(vert)

    spojna = []
    for vert in range(n):
        if not vis[vert]:
            dfs(G, vert, spojna)

    spojne: list[list[int]] = []
    for i in range(n - 1, -1, -1):
        vert = out_colleciton[i]
        if vis[vert]:
            spojna: list[int] = []
            dfs(G_T, vert, spojna, False)
            spojne.append(spojna)

    return spojne
