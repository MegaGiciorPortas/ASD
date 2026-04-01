"""
Złożoność obliczeniowa: O(d*(n+k))
Złożoność pamięciowa: O(n+k)
"""

from math import log2, ceil


def countingsort_radixInt(A: list[int], indeks: int) -> None:
    n = len(A)
    res = [0] * n
    cnt = [0] * 10

    for i in range(n):
        ind = (A[i] // indeks) % 10
        cnt[ind] += 1

    for i in range(1, 10):
        cnt[i] += cnt[i - 1]

    for i in range(n - 1, -1, -1):
        ind = (A[i] // indeks) % 10
        cnt[ind] -= 1
        res[cnt[ind]] = A[i]

    for i in range(n):
        A[i] = res[i]


def radix_sort_int(A: list[int]) -> list[int]:
    B = [i for i in A]

    maksymalny = max(B)
    indeks = 1
    while maksymalny // indeks >= 1:
        countingsort_radixInt(B, indeks)
        indeks *= 10
    return B


def countingsort_radixStr(A: list[str], indeks: int) -> None:
    n = len(A)
    res = ["" for _ in range(n)]
    cnt = [0] * 128

    for i in range(n):
        if indeks < len(A[i]):
            p = ord(A[i][indeks])
        else:
            p = 0
        cnt[p] += 1

    for i in range(1, 128):
        cnt[i] += cnt[i - 1]

    for i in range(n - 1, -1, -1):
        p = ord(A[i][indeks])
        cnt[p] -= 1
        res[cnt[p]] = A[i]

    for i in range(n):
        A[i] = res[i]


def radix_sort_string(A: list[str]) -> list[str]:
    B = [i for i in A]
    max_len = max([len(a) for a in B]) - 1
    while max_len > -1:
        countingsort_radixStr(B, max_len)
        max_len -= 1
    return B


def countingsort_radixBit(A: list[int], bit: int) -> None:
    n = len(A)
    res = [0] * n
    cnt = [0] * 2
    for i in range(n):
        ind = (A[i] >> bit) & 1
        cnt[ind] += 1
    cnt[1] += cnt[0]

    for i in range(n - 1, -1, -1):
        ind = (A[i] >> bit) & 1
        cnt[ind] -= 1
        res[cnt[ind]] = A[i]

    for i in range(n):
        A[i] = res[i]


def radix_sort_bit(A: list[int]) -> list[int]:
    max_num = max(A)
    B = [a for a in A]

    max_bits = ceil(log2(max_num))
    bit = 0
    while bit <= max_bits:
        countingsort_radixBit(B, bit)
        bit += 1
    return B
