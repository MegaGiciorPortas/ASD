import array
import sys
from random import randint

sys.setrecursionlimit(2000000)


def partition(A, p, r):
    q = randint(p, r)
    A[q], A[r] = A[r], A[q]
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
        elif q > k:
            find_kty(A, p, q - 1, k)
        else:
            find_kty(A, q + 1, r, k)
    return


def main_function(A, Q):
    n = len(A)
    for k in Q:
        p = 0
        r = n - 1
        print(find_kty(A, p, r, n - k))


def get_ints():
    """Generator, który czyta wejście bez zapychania pamięci."""
    for line in sys.stdin:
        for token in line.split():
            yield int(token)


def main() -> None:
    data_stream = get_ints()

    n = next(data_stream)
    A = array.array("i", (next(data_stream) for _ in range(n)))
    q = next(data_stream)
    questions = array.array("i", (next(data_stream) for _ in range(q)))
    main_function(A, questions)


if __name__ == "__main__":
    main()
