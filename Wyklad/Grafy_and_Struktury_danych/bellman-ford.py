# O(V*E)


def bellford(G: list[list[tuple[int, int]]], start: int):
    n = len(G)
    dist = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[start] = 0

    for _ in range(n - 1):
        changed = False

        for vert in range(n):
            if dist[vert] == float("inf"):
                continue

            for child, w in G[vert]:
                if dist[vert] + w < dist[child]:
                    dist[child] = dist[vert] + w
                    parent[child] = vert
                    changed = True
        if not changed:
            break

    changed = False
    for vert in range(n):
        for child, w in G[vert]:
            if dist[vert] + w < dist[child]:
                changed = True

        if changed:
            break

    if changed:
        print("Cykl ujemny w grafie")
        return [], []

    return dist, parent
