import sys
from math import ceil, log10


def countingsort(T: list[list[int]], shift: int) -> None:
    n = len(T)
    cnt = [0] * 256
    res = [None] * n

    for i in range(n):
        ind = (T[i][0] >> (shift * 8)) & 255
        cnt[ind] += 1

    for i in range(1, 256):
        cnt[i] += cnt[i - 1]

    for i in range(n - 1, -1, -1):
        ind = (T[i][0] >> (shift * 8)) & 255
        cnt[ind] -= 1
        res[cnt[ind]] = T[i]  # type: ignore

    T[:] = res  # type: ignore


def radixsort(T: list[list[int]]) -> None:
    max_bits = ceil(18 / log10(2))
    max_bits = max_bits // 8 + 2
    for shift in range(0, max_bits):
        countingsort(T, shift)


def function(T: list[list[int]]) -> tuple[int, int]:
    current = 0
    max_snieg = 0
    max_indeks = 0
    n = len(T)

    for indeks, element in enumerate(T):
        current += element[1]

        if indeks == n - 1 or element[0] != T[indeks + 1][0]:
            if current > max_snieg:
                max_snieg = current
                max_indeks = element[0]

    return max_snieg, max_indeks


def main() -> None:
    tablica = list(map(int, sys.stdin.read().split()))
    T = []
    for i in range(2, len(tablica), 2):
        T.append([tablica[i], 1])
        T.append([tablica[i + 1] + 1, -1])
    #    radixsort(T)
    T.sort()
    results = function(T)
    print(results[0], results[1])


if __name__ == "__main__":
    main()
