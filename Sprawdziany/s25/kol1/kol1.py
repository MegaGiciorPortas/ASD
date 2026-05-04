from kol1testy import runtests


def insertionsort(T):
    n = len(T)
    for i in range(1, n):
        j = i - 1
        key = T[i]
        while j >= 0 and key < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def sprawdzenie_kubelka(T, D) -> int:
    counter = 0
    n = len(T)
    for i in range(1, n):
        if T[i] - T[i - 1] >= D:
            counter += 1
    return counter


# najzwyklejsze sortwanie każdego kubełka za pomocą insertionsort
def sortowanie(T):
    n = len(T)
    for i in range(n):
        insertionsort(T[i])


def ogrodzenie(M, D, T) -> int:
    n = len(T)
    buckets = [[] for _ in range(n)]

    # dodawanie liczb do kubełków
    for value in T:
        ind = int((value / M) * (n - 1))
        buckets[ind].append(value)

    # sprawdzenie czy w jednym kubełku może zajść przypadek, że kombajn się zmieści
    flaga = False
    if M / n >= D:
        flaga = True
        sortowanie(buckets)

    # wyznaczenie pierwszego niepustego kubełka
    licznik = 0
    i = 0
    while buckets[i] == []:
        i += 1

    # jezeli kombajn moze sie zmiescic w jednym kubelku to sprawdzam czy zachodzi to w pierwszym kubelku
    if flaga:
        licznik += sprawdzenie_kubelka(buckets[i], D)

    for j in range(i + 1, n):
        # jezeli kubełek jest pusty to pomijam
        if buckets[j] == []:
            continue

        # jezeli moze zajsc sutacja ze kombajn zmiesci sie w jednym kubelki to sprawdzam czy tutaj tak jest
        if flaga:
            licznik += sprawdzenie_kubelka(buckets[j], D)

        # sprawdzenie czy odstep miedzy sąsiednimi kbełkami jest wystarczający aby kombajn się zmieścił
        if min(buckets[j]) - max(buckets[i]) >= D:
            licznik += 1

        i = j

    return licznik


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ogrodzenie, all_tests=True)
