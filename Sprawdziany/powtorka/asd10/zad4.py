def problem_azacha(miasta: list[tuple[int, int]], start: int):
    n = max(max(m) for m in miasta) + 1
    G = [[] for _ in range(n)]
    start_oaza = 0
    for i in range(len(miasta)):
        x = miasta[i][0]
        y = miasta[i][1]

        if i == start:
            start_oaza = y

        G[x].append((y, i))
        G[y].append((x, i))

    visited_cities = [False for _ in range(len(miasta))]
    cycle = []

    def dfs(u):
        while G[u]:
            v, city = G[u].pop()

            if not visited_cities[city]:
                visited_cities[city] = True
                dfs(v)
        cycle.append(u)

    dfs(start_oaza)
    return len(cycle) == len(miasta) + 1
