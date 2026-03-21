numop1 = 0


def merge(A: list[int], B: list[int], p: int, q: int, r: int) -> None:
    global numop1
    i: int = p;
    j: int = q;
    k: int = p

    while i < q and j < r:
        if A[i] <= A[j]:
            B[k] = A[i]
            numop1 += 1
            i += 1
        else:
            B[k] = A[j]
            numop1 += 1
            j += 1
        k += 1

    while i < q:
        B[k] = A[i]
        numop1 += 1
        k += 1
        i += 1
    while j < r:
        numop1 += 1
        B[k] = A[j]
        k += 1
        j += 1

    for t in range(p, r):
        numop1 += 1
        A[t] = B[t]
    return


def sort_help(A: list[int], B: list[int], p: int, r: int) -> None:
    global numop1
    if r - p > 1:
        numop1 += 1
        q = (p + r) // 2
        sort_help(A, B, p, q)
        sort_help(A, B, q, r)

        merge(A, B, p, q, r)


def mergesort(A: list[int]) -> tuple[list[int], int]:
    global numop1
    numop1 = 0
    n = len(A)
    B: list[int] = [0] * n
    numop1 += n
    C: list[int] = [0] * n

    for i in range(n): C[i] = A[i]

    sort_help(C, B, 0, n)

    return (C, numop1)
