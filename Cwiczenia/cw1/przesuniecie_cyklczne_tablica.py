"""
Przesuniecie cykliczne tablicy
T[n] w miejscu
T[i] -> T[(i+k)%n]
"""


def rev(T, s, f):
    while s < f:
        T[s], T[f] = T[f], T[s]
        s += 1
        f -= 1


def move_cyclic(T, k):
    n = len(T)
    l = k % n

    rev(T, 0, n - 1)
    rev(T, 0, l - 1)
    rev(T, l, n - 1)
