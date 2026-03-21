def counting_sort(A,m):
    n = len(A)
    B = [0] * n
    C = [0] * m

    for i in range(n):
        C[A[i]] += 1

    for i in range(1,m):
        C[i] = C[i-1] + C[i]

    for i in range(n-1,-1,-1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    return B