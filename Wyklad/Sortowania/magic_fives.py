def selectionsort(T):
    n = len(T)

    for i in range(n - 1):
        indeks = i
        for j in range(i + 1, n):
            if T[j] < T[indeks]:
                indeks = j

        T[i], T[indeks] = T[indeks], T[i]


def magiczne_piatki(tablica, k):
    if len(tablica) <= 5:
        selectionsort(tablica)
        return tablica[k]

    mediany = []
    for i in range(0, len(tablica), 5):
        grupa = tablica[i : i + 5]
        selectionsort(grupa)
        mediana_grupy = grupa[len(grupa) // 2]
        mediany.append(mediana_grupy)

    indeks_srodkowy = len(mediany) // 2
    mediana_z_median = magiczne_piatki(mediany, indeks_srodkowy)

    print(mediana_z_median, mediany)

    mniejsze = [x for x in tablica if x < mediana_z_median]
    rowne = [x for x in tablica if x == mediana_z_median]
    wieksze = [x for x in tablica if x > mediana_z_median]

    if k < len(mniejsze):
        return magiczne_piatki(mniejsze, k)
    elif k < len(mniejsze) + len(rowne):
        return mediana_z_median
    else:
        nowe_k = k - len(mniejsze) - len(rowne)
        return magiczne_piatki(wieksze, nowe_k)


dane = [25, 21, 98, 100, 76, 22, 43, 60, 89, 87, 12, 1, 3, 5, 4]

wynik = magiczne_piatki(dane, 10)
print(f"Zwrócony element: {wynik}")
