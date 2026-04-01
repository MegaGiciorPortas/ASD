"""
Złożoność obliczeniowa: O(nlogn) ZAWSZE TAK SIE WYKONUJE
Złożoność pamięciowa: O(1) bo srotujemy tablice na niej samej (sortowanie w miejscu)
"""


def parent(i):
    return (i - 1) // 2


def left(i):
    return i * 2 + 1


def right(i):
    return i * 2 + 2


def heapify(T: list[int], n: int, i: int) -> None:
    max_ind = i
    if left(i) < n and T[left(i)] > T[max_ind]:
        max_ind = left(i)
    if right(i) < n and T[right(i)] > T[max_ind]:
        max_ind = right(i)
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, n, max_ind)


def build_heap(T: list[int]) -> None:
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, n, i)


def hsort(T: list[int]) -> None:
    build_heap(T)
    n = len(T)
    for i in range(0, n - 1):
        T[0], T[n - 1 - i] = T[n - 1 - i], T[0]
        heapify(T, n - 1 - i, 0)
