import array
import sys
from random import randint


def partition(A, p, r):
    # Losowy pivot chroni przed pesymistycznym czasem O(n^2)
    idx = randint(p, r)
    A[idx], A[r] = A[r], A[idx]

    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort_iterative(A, p, r):
    # Własny stos do przechowywania zakresów (zamiast rekurencji)
    stack = [(p, r)]

    while stack:
        p, r = stack.pop()
        if p < r:
            q = partition(A, p, r)
            # Dodajemy mniejszą część najpierw, aby stos nie urósł za bardzo
            if q - p < r - q:
                stack.append((q + 1, r))
                stack.append((p, q - 1))
            else:
                stack.append((p, q - 1))
                stack.append((q + 1, r))


def get_ints():
    for line in sys.stdin:
        for token in line.split():
            yield int(token)


def main() -> None:
    data_stream = get_ints()
    try:
        n = next(data_stream)
    except StopIteration:
        return

    # Wczytywanie bez tworzenia list pośrednich
    A = array.array("i", (next(data_stream) for _ in range(n)))

    q_count = next(data_stream)
    questions = array.array("i", (next(data_stream) for _ in range(q_count)))

    # Sortujemy tablicę raz ręcznie zaimplementowanym Quicksortem
    quicksort_iterative(A, 0, n - 1)

    # Odpowiedzi na zapytania
    for k in questions:
        print(A[n - k])


if __name__ == "__main__":
    main()
