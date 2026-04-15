"""
Złożoność obliczeniowa: O(nlogn) ZAWSZE SIE TYLE WYKONJE
Złożoność pamięciowa: O(n) bo musimy stworzyć n-elementową tablicę B
"""


def merge(T: list[int], B: list[int], p: int, q: int, r: int) -> None:
    i = k = p
    j = q
    while i < q and j < r:
        if T[i] <= T[j]:
            B[k] = T[i]
            i += 1
        else:
            B[k] = T[j]
            j += 1
        k += 1

    while i < q:
        B[k] = T[i]
        i += 1
        k += 1

    while j < r:
        B[k] = T[j]
        j += 1
        k += 1

    for i in range(p, r):
        T[i] = B[i]


def mergesort(T: list[int], B: list[int], p: int, r: int) -> None:
    if r - p > 1:
        q = (r + p) // 2
        mergesort(T, B, p, q)
        mergesort(T, B, q, r)
        merge(T, B, p, q, r)


def msort(T: list[int]) -> None:
    n = len(T)
    B = [0] * n
    mergesort(T, B, 0, n)
