"""
Złożoność obliczeniowa: O(nlogn) natomiast kiedy np do quicksorta dosatnie sie posortwana tablica to złożoność wzrasta do n^2
dlatego napisna jest druga funkcja partition, ktora zmniejsza prawdopodobieństwo skwadracenia się tego algorytmu
Złożoność pamięciowa: O(1)
NIE JEST TO ALGORYTM STABILNY
"""

from random import randint


def random_partition(T: list[int], p: int, r: int) -> int:
    rand_pivot = randint(p, r)
    x = T[rand_pivot]
    T[r], T[rand_pivot] = T[rand_pivot], T[r]
    i = p - 1
    for j in range(p, r + 1):
        if T[j] <= x:
            i += 1
            T[j], T[i] = T[i], T[j]
    return x


def partition(T: list[int], p: int, r: int) -> int:
    x = T[r]
    i = p - 1
    for j in range(p, r + 1):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    return i


def qsort(T: list[int], p: int, r: int) -> None:
    if p < r:
        q = partition(T, p, r)
        qsort(T, p, q - 1)
        qsort(T, q + 1, r)
