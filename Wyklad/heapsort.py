
numop = 0

def parent(i: int) -> int: return (i - 1) // 2
def left(i: int) -> int: return 2*i + 1
def right(i: int) -> int: return 2*i + 2


def heapify(A:list[int], i:int, n:int) -> None:
    global numop
    max_ind:int = i
    if left(i) < n and A[left(i)] > A[max_ind]:
        max_ind = left(i)
        numop += 1

    if right(i) < n and A[right(i)] > A[max_ind]:
        max_ind = right(i)
        numop += 1

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        numop += 1
        heapify(A, max_ind, n)

def build_heap(A:list[int]) -> None:
    global numop
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, i, n)

def heap_sort(A:list[int]) -> tuple[list[int], int]:
    global numop
    numop = 0
    n = len(A)

    C = [0] * n

    for i in range(n):
        C[i] = A[i]

    build_heap(C)

    for i in range(0, n-1):
        C[0], C[n-i-1] = C[n-i-1], C[0]
        numop += 1
        heapify(C, 0, n-i-1)
    return (C, numop)