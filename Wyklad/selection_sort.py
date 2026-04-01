"""
Złożoność obliczeniowa: O(n^2) a dokładniej 1/2 * n^2 - O(n)
Złożoność pamięciowa: O(1)
"""


def selectionsort(T: list[int]) -> None:
    n = len(T)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if T[j] < T[min_ind]:
                min_ind = j

        T[i], T[min_ind] = T[min_ind], T[i]
