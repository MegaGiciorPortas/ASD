"""
1)
a) Scalanie dwoch list jednokierunkowych
b) mergesort na seriach naturalnych

2) wstawianie do kopca binarnego

3) Posortuj tablice k-chaotyczna
T[i] --> T_sorted[j]
j nalezy { i-k, i+k}

4) Posortowana tablica A[n]
i liczba x. Znajdź i,j takie ze
a) A[i] - A[j] = x
b) A[i] = A[j] = x

# te dwa zadania 5,6 to sa bardziej jako ciekawostki
# raczej trzeba sie skupic na zrobieniu zadania 2 i 3 oraz po prostu robienie zadan ze szkopul
5) struktura danych
- wlozyc element O(logn)
- insert
-remove Min
-remove Max

6) struktura danych
- wlozyc element O(logn)
- insert
- remove Median

---------------

7) Zliczyc inwersje
i < j , A[i] > A[j]   - to jest to kiedy jest inwersja

8) scalic k posortowanych list o łacznie n elementach
w O(nlogk)

"""


class Node():
    def __init__(self, value):
        self.val = value
        self.next = None


# a)
def scalanie(head1, head2):
    head = Node()
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


# b)
def roz(A):
    cur = A

    while cur.next is not None and cur.val < cur.next.val:
        cur = cur.next

    j = cur.next
    cur.next = None
    return A, j


def mergesort(A):
    while True:
        result = Node()
        i = result
        counter = 0
        while A is not None:
            a, A = roz(A)
            b, A = roz(A)
            d = scalanie(a, b)
            i.next = d

            while i.next is not None:
                i = i.next
            counter += 1
        if counter == 1:
            break
        A = result.next
    return result.next


# 2)


# 3)


# 4)
def gasieinca_odejmowanie(T, x):
    N = len(T)
    j = 1
    i = 0
    while i < N:
        if T[i] - T[j] == x:
            return j, i
        elif T[i] - T[j] < x:
            i += 1
        else:
            j += 1
    return None, None


def gasienica_dodawanie(T, x):
    N = len(T)
    i = 0
    j = N - 1

    while i < j:
        if T[i] + T[j] == x:
            return i,j
        elif T[i] + T[j] < x:
            i += 1
        else:
            j -= 1
    return None, None
