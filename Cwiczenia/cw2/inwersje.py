# Zliczyć inwersje w tej tablicy tzn:
# i < j and A[i] > A[j]


def merge(T, B, p, q, r):
    i = k = p
    j = q
    inwersje = 0

    #  0  1  2  3    4  5
    # [] [] [] | [] [] [] r = 6
    while i < q and j < r:
        if T[i] > T[j]:
            inwersje += q - i
            B[k] = T[j]
            j += 1
        else:
            B[k] = T[i]
            i += 1
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

    return inwersje


def mergesort_ultra(T, B, p, r):
    inwersje = 0
    if r - p > 1:
        q = (r + p) // 2
        inwersje += mergesort_ultra(T, B, p, q)
        inwersje += mergesort_ultra(T, B, q, r)
        inwersje += merge(T, B, p, q, r)
    return inwersje


def ile_inwersji(T):
    n = len(T)
    B = [0] * n

    return mergesort_ultra(T, B, 0, n)
