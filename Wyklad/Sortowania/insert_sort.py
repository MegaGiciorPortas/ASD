"""
Złożoność obliczeniowa: O(n^2) a dokładniej 1/2 n^2 + O(n)
Złożoność pamięciowa: O(1)
"""


def insertsort(T: list[int]) -> None:
    n = len(T)
    for i in range(1, n):
        j = i - 1
        key = T[i]
        while j >= 0 and key < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
