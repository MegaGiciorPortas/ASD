# Types
weighted_edge_list = list[tuple[int, int, int]]
#                                u    v   cost


class FindUnion:
    def __init__(self, n: int):
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n

    def find(self, a: int) -> int:
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[a] = b
            if self.rank[a] == self.rank[b]:
                self.rank[b] += 1


# O( E log V)
def kruskal_find_MST(
    num_verticies: int, edges: weighted_edge_list
) -> weighted_edge_list:
    mst: weighted_edge_list = []

    edges.sort(key=lambda edge: edge[2])

    fu = FindUnion(num_verticies)

    for u, v, weight in edges:
        if fu.find(u) != fu.find(v):
            mst.append((u, v, weight))
            fu.union(u, v)

            if len(mst) == num_verticies - 1:
                break

    return mst
