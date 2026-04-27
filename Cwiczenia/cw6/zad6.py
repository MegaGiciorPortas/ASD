import heapq


def main_function(G: list[list[tuple[int, int]]], start: int, meta: int):
    n = len(G)

    dist = [[float("inf"), float("inf")] for _ in range(n)]
    dist[start] = [0, float("inf")]

    Q = []
    heapq.heappush(Q, (0, start, 0))

    while Q:
        baza, u, kierowca = heapq.heappop(Q)

        if baza > dist[u][kierowca]:
            continue

        for cost, v in G[u]:
            aktualny_koszt = cost if kierowca == 0 else 0
            # jezeli jedzie kierowca A to koszt sie liczy, natomiast jezeli jedzie kierowca B to koszt nie ma znaczenia:w

            nastepny_kierowca = (kierowca + 1) % 2

            if baza + aktualny_koszt < dist[v][nastepny_kierowca]:
                dist[v][nastepny_kierowca] = baza + aktualny_koszt
                heapq.heappush(Q, (dist[v][nastepny_kierowca], v, nastepny_kierowca))

    return dist[meta][0]
