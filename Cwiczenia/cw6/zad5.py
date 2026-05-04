from math import log


# tablica n*n jezeli jest tam wartosc -1 to wtedy nie istnieje wymiana
def money_maker(table: list[list[float]]):
    n = len(table)
    graph: list[list[tuple[int, float]]] = [[] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if i == j or table[i][j] == -1:
                continue
            graph[i].append((j, -log(table[i][j])))

    start = n
    for i in range(n):
        graph[start].append((i, 0))

    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    parent: list[int] = [-1] * (n + 1)

    for _ in range(n):
        changed = False
        for vert in range(n + 1):
            for child, cost in graph[vert]:
                if dist[child] > cost + dist[vert]:
                    dist[child] = cost + dist[vert]
                    parent[child] = vert
                    changed = True
        if not changed:
            break

    cycle_node = -1
    for vert in range(n + 1):
        for child, cost in graph[vert]:
            if dist[child] > cost + dist[vert]:
                cycle_node = child
                break

    if cycle_node == -1:
        return False, []

    for _ in range(n + 1):
        cycle_node = parent[cycle_node]

    cycle: list[int] = []
    curr = cycle_node
    while True:
        cycle.append(curr)
        curr = parent[curr]
        if curr == cycle_node:
            break
    cycle.append(cycle_node)

    return True, cycle


table = [[1.0, 0.25], [4.10, 1.0]]

print(money_maker(table))
