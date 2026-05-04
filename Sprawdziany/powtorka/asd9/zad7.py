from queue import PriorityQueue


def problem_with_gas_station(
    G: list[list[tuple[int, int]]],
    ceny_paliw: list[float],
    start: int,
    meta: int,
    D: int,
):
    n = len(G)
    pq = PriorityQueue()
    total_cost = [[float("inf") for _ in range(D + 1)] for _ in range(n)]
    total_cost[start][0] = 0
    parent = [-1 for _ in range(n)]

    pq.put((0, start, 0))

    while not pq.empty():
        koszt, vert, fuel = pq.get()

        if vert == meta:
            return koszt

        if koszt > total_cost[vert][fuel]:
            continue

        if fuel < D:
            nowy_koszt = koszt + ceny_paliw[vert]
            nowe_paliwo = fuel + 1

            if nowy_koszt < total_cost[vert][nowe_paliwo]:
                total_cost[vert][nowe_paliwo] = nowy_koszt
                pq.put((nowy_koszt, vert, nowe_paliwo))

        for child, road in G[vert]:
            if fuel >= road:
                nowy_koszt = koszt
                nowe_paliwo = fuel - road

                if nowy_koszt < total_cost[child][nowe_paliwo]:
                    total_cost[child][nowe_paliwo] = nowy_koszt
                    pq.put((nowy_koszt, child, nowe_paliwo))

    return float("inf")
