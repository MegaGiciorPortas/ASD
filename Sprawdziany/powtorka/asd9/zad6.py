from queue import Empty, PriorityQueue


def two_riders(G: list[list[tuple[int, int]]], start: int, meta: int):
    n = len(G)
    # Alicja = 0, Bob = 1
    pq = PriorityQueue()
    parent = [[(-1, -1), (-1, -1)] for _ in range(n)]
    dist = [[float("inf"), float("inf")] for _ in range(n)]
    pq.put((0, start, 0))
    pq.put((0, start, 1))
    dist[start] = [0, 0]

    while not pq.empty():
        cost, vert, kierowca = pq.get()
        nastepny_kierowca = (kierowca + 1) % 2

        if cost > dist[vert][kierowca]:
            continue

        for child, road in G[vert]:
            if kierowca == 1:
                road = 0
            if road + cost < dist[child][nastepny_kierowca]:
                dist[child][nastepny_kierowca] = road + cost
                parent[child][nastepny_kierowca] = (vert, kierowca)
                pq.put((road + cost, child, nastepny_kierowca))

    return min(dist[meta][0], dist[meta][1]), parent
