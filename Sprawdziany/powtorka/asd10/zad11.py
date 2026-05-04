from queue import PriorityQueue


def malejace_krawedzie_dijkstra_2d(
    G: list[list[tuple[int, int]]], start: int, meta: int
):
    n = len(G)

    max_edge = 0
    for u in range(n):
        for _, weight in G[u]:
            if weight > max_edge:
                max_edge = weight

    START_EDGE = max_edge + 1

    dist = [[float("inf") for _ in range(START_EDGE + 1)] for _ in range(n)]

    pq = PriorityQueue()

    pq.put((0, START_EDGE, start))
    dist[start][START_EDGE] = 0

    while not pq.empty():
        cost, prev_edge, vert = pq.get()

        if vert == meta:
            return cost

        if cost > dist[vert][prev_edge]:
            continue

        for child, edge in G[vert]:
            if edge >= prev_edge:
                continue

            nowy_koszt = cost + edge

            if nowy_koszt < dist[child][edge]:
                dist[child][edge] = nowy_koszt
                pq.put((nowy_koszt, edge, child))

    return float("inf")


def malejace_krawedzie_optymalnie(
    E: list[tuple[int, int, int]], V: int, start: int, meta: int
):
    # E to lista krawędzi w formacie (waga, u, v)
    dist = [float("inf")] * V
    dist[start] = 0

    # Sortujemy malejąco po wadze krawędzi (element 0 w krotce)
    E.sort(key=lambda edge: edge[0], reverse=True)

    # Przechodzimy przez wszystkie krawędzie dokładnie jeden raz!
    for waga, u, v in E:
        if dist[u] != float("inf"):
            if dist[u] + waga < dist[v]:
                dist[v] = dist[u] + waga

    return dist[meta]
