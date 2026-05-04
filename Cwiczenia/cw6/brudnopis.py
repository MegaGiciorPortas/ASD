from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int | float:

        G = defaultdict(list)
        for u, v, cost in flights:
            G[u].append((cost, v))

        dist = [float("inf")] * n
        dist[src] = 0

        Q = deque()
        Q.append((src, 0, 0))

        while Q:
            vert, cost, stops = Q.popleft()

            if stops > k:
                continue

            for price, city in G[vert]:
                if price + cost < dist[city]:
                    dist[city] = price + cost
                    Q.append((city, price + cost, stops + 1))

        return dist[dst] if dist[dst] != float("inf") else -1
