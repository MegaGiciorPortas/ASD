"""
Złożoność obliczeniowa: O(n+m)
Złożoność pamięciowa: O(n+m)
"""


def countingsort(T: list[int]) -> None:
    n = len(T)
    m = max(T)
    cnt = [0] * (m + 1)
    C = [0] * n

    for i in range(n):
        cnt[T[i]] += 1

    for i in range(1, m):
        cnt[i] += cnt[i - 1]

    for i in range(n - 1, -1, -1):
        cnt[T[i]] -= 1
        C[cnt[T[i]]] = T[i]

    for i in range(n):
        T[i] = C[i]
