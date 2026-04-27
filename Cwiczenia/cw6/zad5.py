from math import log


def main_function(G: list[list[tuple[int, int]]]):
    NG: list[list[tuple[float, int]]] = []
    n = len(G)
    for i in range(n):
        NG.append([])
        for cost, v in G[i]:
            NG[i].append((-log(cost), v))

    def bellman_ford(start: int):
        n = len(G)
        dist: list[int | float] = [0 for _ in range(n)]

        for _ in range(n - 1):
            changed = False

            for vert in range(n):
                if dist[vert] == float("inf"):
                    continue

                for cost, v in NG[vert]:
                    if dist[vert] + cost < dist[v]:
                        dist[v] = dist[vert] + cost
                        changed = True

            if not changed:
                break

        changed = False
        for vert in range(n):
            for cost, v in NG[vert]:
                if dist[vert] + cost < dist[v]:
                    changed = True

            if changed:
                break

        if changed:
            print("Cykl ujemny w grafie")
            return True

        return False
