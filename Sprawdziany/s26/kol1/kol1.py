"""
Mateusz Portka 432101

Złożonośc algorytmu to jest niestety O(n^2)

Algorytm działa w następujący sposób:
1) Generuje tabliczke mnożenia dla wszystkich liczb w złożoności O(n^2)
2) Wyszukuje k-ty element w tej tablicy w złożoności O(n) za pomocą algorytmu quick select
"""

from kol1_test import runtests


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


def find_kty(A, p, r, k):
    if p <= r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return find_kty(A, q + 1, r, k)
        else:
            return find_kty(A, p, q - 1, k)


def k_big(A, k):
    T = []
    n = len(A)
    for i in range(n):
        for j in range(n):
            T.append(A[i] * A[j])
    return find_kty(T, 0, len(T) - 1, len(T) - k)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(k_big, all_tests=True)
