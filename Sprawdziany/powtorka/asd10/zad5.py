from math import ceil, sqrt

class FindUnion():
    def __init__(self,n:int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self,x):
        if x != self.parent[x]
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,a,b):
        a = self.find(a)
        b = self.finf(b)

        if a == b:
            return
        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[a] = b
            if self.rank[a] == self.rank[b]:
                self.rank[b] += 1


def problem_autostrad(cities:list[tuple[int,int]]):
    n = len(cities)
    edges = []

    for i in range(n):
        for j in range(i+1,n):
            odleglosc = ceil(sqrt( (cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2))
            edges.append((odleglosc,i,j))

    edges.sort()
    N = len(edges)
    result = float('inf')

    for i in range(N):
        fu = FindUnion(n)
        dlugosc_drzewa = 0
        for j in range(i,N):
            w_max,u,v = edges[j]
            if fu.find(u) != fu.find(v):
                fu.union(u,v)
                dlugosc_drzewa += 1

                if dlugosc_drzewa == n -1:
                    w_min = edges[i][0]
                    result = min(result,(w_max - w_min))
                    break
    return result

                


