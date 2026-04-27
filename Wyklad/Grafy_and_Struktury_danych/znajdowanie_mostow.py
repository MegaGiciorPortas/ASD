# Graf nieskierowany

# O(V + E)
# lista sasiedztwa
def find_bridges(G: list[list[int]]) -> list[tuple[int, int]]:
    n = len(G)

    curr_time = 0

    time_in = [0 for _ in range(n)]
    low = [0 for _ in range(n)]
    bridges: list[tuple[int, int]] = []

    def dfs(vert: int, parent: int):
        nonlocal time_in, curr_time, low, bridges, G

        curr_time += 1
        time_in[vert] = low[vert] = curr_time

        for child in G[vert]:
            if child == parent:
                continue
            if time_in[child] == 0:
                dfs(child, vert)
                low[vert] = min(low[vert], low[child])

                if low[child] == time_in[child]:
                    bridges.append((vert, child))
            else:
                low[vert] = min(low[vert], time_in[child])

    for vert in range(n):
        if time_in[vert] == 0:
            dfs(vert, -1)

    return bridges

