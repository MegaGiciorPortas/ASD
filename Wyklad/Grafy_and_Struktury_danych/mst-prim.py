from heapq import heappop as pq_pop, heappush as pq_push

graph_neighbor_weighted = list[list[tuple[int, int]]]


# O ((V + E)log V)
def prim_find_mst(Graph: graph_neighbor_weighted, start: int) -> list[int]:
    n = len(Graph)

    parent: list[int] = [-1] * n
    queue_weights: list[int | float] = [float("inf") for _ in range(n)]
    vis: list[bool] = [False] * n

    pq: list[tuple[int, int]] = [(0, start)]
    queue_weights[start] = 0

    while pq:
        _, vert = pq_pop(pq)

        if vis[vert]:
            continue
        vis[vert] = True

        for child, cost in Graph[vert]:
            if not vis[child] and queue_weights[child] > cost:
                queue_weights[child] = cost
                parent[child] = vert
                pq_push(pq, (cost, child))
    return parent
