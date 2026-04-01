# Quicksort o maksymalnie O(logn) pamięci
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            qsort(A, p, q - 1)
            qsort(A, q + 1, r)
        else:
            qsort(A, q + 1, r)
            qsort(A, p, q - 1)


# Znalezienie w nieposorotwanej tablicy
# k-ty co do wielkości element
def find_k_ty(A, p, r, k):
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return find_k_ty(A, q + 1, r, k)
        else:
            return find_k_ty(A, p, q - 1, k)
    return
