from math import log


def wymiana_walut(K: list[list[float]]):
    n = len(K)
    for i in range(n):
        for j in range(n):
            K[i][j] = -log(K[i][j])
        K[i].append(float("inf"))
    K.append([0] * (n + 1))

    dist = [float("inf") for _ in range(n)]
    dist.append(0.0)

    for _ in range(n):
        changed = False

        for vert in range(n + 1):
            if dist[vert] == float("inf"):
                continue

            for child in range(n + 1):
                if vert == child:
                    continue
                if dist[child] > dist[vert] + K[vert][child]:
                    dist[child] = dist[vert] + K[vert][child]
                    changed = True

    changed = False

    for vert in range(n + 1):
        for child in range(n + 1):
            if vert == child:
                continue
            if dist[child] > dist[vert] + K[vert][child]:
                changed = True
        if changed:
            break

    return changed
