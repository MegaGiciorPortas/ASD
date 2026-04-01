# Posortowania tablica T[n], znjajdź takie x, że:
# A[i] - A[j] = x
# A[i] + A[j] = x


def gasieinca_odejmowanie(T, x):
    N = len(T)
    j = 1
    i = 0
    while j < N:
        if T[j] - T[i] == x:
            return i, j
        elif T[j] - T[i] < x:
            j += 1
        else:
            i += 1
    return None, None


def gasienica_dodawanie(T, x):
    N = len(T)
    i = 0
    j = N - 1

    while i < j:
        if T[i] + T[j] == x:
            return i, j
        elif T[i] + T[j] < x:
            i += 1
        else:
            j -= 1
    return None, None
