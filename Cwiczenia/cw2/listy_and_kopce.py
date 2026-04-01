# scalanie dwóch posortowanych list jednokierunkowych
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def scalanie(head1, head2):
    head = Node(0)
    tail = head

    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1 is not None:
        tail.next = head1

    if head2 is not None:
        tail.next = head2

    return head.next


# mergesort na seriach naturalnych
def roz(A):
    cur = A

    while cur.next is not None and cur.val < cur.next.val:
        cur = cur.next

    j = cur.next
    cur.next = None
    return A, j


def mergesort(A):
    while True:
        result = Node(0)
        i = result
        counter = 0
        while A is not None:
            a, A = roz(A)
            if A is not None:
                b, A = roz(A)
            else:
                b = None
            d = scalanie(a, b)
            i.next = d

            while i.next is not None:
                i = i.next
            counter += 1
        if counter == 1:
            break
        A = result.next
    return result.next


# scalić k posortowanych list o łacznie n elementach w O(nlogk)
def parent(i):
    return (i - 1) // 2


def right(i):
    return (i * 2) + 2


def left(i):
    return (i * 2) + 1


def heapify(A, n, i):
    min_ind = i
    if left(i) < n and A[left(i)].val < A[min_ind].val:
        min_ind = left(i)

    if right(i) < n and A[right(i)].val < A[min_ind].val:
        min_ind = right(i)

    if min_ind != i:
        A[min_ind], A[i] = A[i], A[min_ind]
        heapify(A, n, min_ind)


def build_heap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def zadanie_8(tablica):
    A = []
    for element in tablica:
        if element is not None:
            A.append(element)

    build_heap(A)
    rozmiar = len(A)
    T = []
    while rozmiar > 0:
        T.append(A[0].val)

        if A[0].next is not None:
            A[0] = A[0].next
            heapify(A, rozmiar, 0)
        else:
            A[0] = A[rozmiar - 1]
            rozmiar -= 1
            heapify(A, rozmiar, 0)


# posortować tablice k-chaotyczna
def heapify_chaotyczne(tablica: list[int], n: int, i: int) -> None:
    max_ind = i
    if left(i) < n and tablica[left(i)] < tablica[max_ind]:
        max_ind = left(i)
    if right(i) < n and tablica[right(i)] < tablica[max_ind]:
        max_ind = right(i)

    if max_ind != i:
        tablica[max_ind], tablica[i] = tablica[i], tablica[max_ind]
        heapify(tablica, n, max_ind)


def build_heap_chaotyczne(tablica: list[int]) -> None:
    n = len(tablica)
    for i in range(parent(n - 1), -1, -1):
        heapify_chaotyczne(tablica, n, i)


def sortowanie_chaotyczne(tablica: list[int]) -> list[int]:
    n = len(tablica)
    build_heap_chaotyczne(tablica)
    for i in range(n - 1):
        tablica[0], tablica[n - 1 - i] = tablica[n - 1 - i], tablica[0]
        heapify(tablica, n - 1 - i, 0)
    return tablica


def tablica_k_chaotyczna(tablica: list[int], k: int) -> None:
    n = len(tablica)
    if n == 0:
        return

    rozmiar_kopca = min(k + 1, n)
    kopiec = tablica[:rozmiar_kopca]
    build_heap_chaotyczne(kopiec)

    indeks = 0

    for i in range(rozmiar_kopca, n):
        tablica[indeks] = kopiec[0]
        indeks += 1

        kopiec[0] = tablica[i]

        heapify_chaotyczne(kopiec, rozmiar_kopca, 0)

    while rozmiar_kopca > 0:
        tablica[indeks] = kopiec[0]
        indeks += 1

        kopiec[0] = kopiec[rozmiar_kopca - 1]
        rozmiar_kopca -= 1
        heapify_chaotyczne(kopiec, rozmiar_kopca, 0)
