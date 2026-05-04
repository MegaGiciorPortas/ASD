from kol2testy import runtests
from queue import PriorityQueue


def lets_roll(start_city, flights, resorts):
    n = max(max(lot[0], lot[1]) for lot in flights) + 1
    G = [[] for _ in range(n)]

    resorts_set = set(resorts)

    for u, v, w in flights:
        G[u].append((w, v))
        G[v].append((w, u))

    dist = [float("inf") for _ in range(n)]
    dist[start_city] = 0

    pq = PriorityQueue()
    pq.put((0, start_city))

    result = 0

    while not pq.empty():
        cost, vert = pq.get()
        if cost > dist[vert]:
            continue

        if vert in resorts_set:
            result += 2 * cost
            continue

        for child_cost, child in G[vert]:
            if dist[child] > child_cost + cost:
                dist[child] = child_cost + cost
                pq.put((cost + child_cost, child))

    return result


runtests(lets_roll, all_tests=True)
