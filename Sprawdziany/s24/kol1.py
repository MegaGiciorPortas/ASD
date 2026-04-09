from kol1testy import runtests


class Node:
    def __init__(self, value):
        self.val = value
        self.ranked = 0


def mergesort(A, B, p, q, r):
    i = k = p
    j = q
    wziete_lewa = 0

    while i < q and j < r:
        if A[i].val < A[j].val:
            B[k] = A[i]
            wziete_lewa += 1
            i += 1
        else:
            A[j].ranked += wziete_lewa
            B[k] = A[j]
            j += 1
        k += 1

    while i < q:
        B[k] = A[i]
        k += 1
        i += 1

    while j < r:
        A[j].ranked += wziete_lewa
        B[k] = A[j]
        k += 1
        j += 1

    for i in range(p, r):
        A[i] = B[i]


def merge(A, B, p, r):
    if r - p > 1:
        q = (p + r) // 2
        merge(A, B, p, q)
        merge(A, B, q, r)
        mergesort(A, B, p, q, r)


def maxrank(T):
    n = len(T)
    A = [Node(x) for x in T]
    B = [0 for _ in range(n)]

    merge(A, B, 0, n)

    return max(object.ranked for object in A)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxrank, all_tests=False)
