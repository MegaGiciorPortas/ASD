# Czy podane napisy to sa anagramy

# alfabet łaciński
def zadanie_5a(A, B, k):
    N = [0] * k
    n = len(A)

    if len(A) != len(B):
        return False

    for i in range(n):
        N[ord(A[i]) - 65] += 1
        N[ord(B[i]) - 65] -= 1

    for element in N:
        if element != 0:
            return False
    return True


# uni_code
def zadanie_5b(A, B, T):
    n = len(A)

    for i in range(n):
        T[A[i]] = 0
        T[B[i]] = 0

    for i in range(n):
        T[A[i]] += 1
        T[B[i]] -= 1

    for i in range(n):
        if T[A[i]] or T[B[i]]:
            return False
    return True
