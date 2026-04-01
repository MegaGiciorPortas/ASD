# sortowanie n słów w czasie liniowym po ich długości


def counting_sort_str(tablica: list[str], ind: int) -> list[str]:
    n = len(tablica)
    if n == 0:
        return []

    res = [""] * n

    cnt = [0] * 128

    for element in tablica:
        p = ord(element[ind])
        cnt[p] += 1

    for i in range(1, 128):
        cnt[i] += cnt[i - 1]

    for i in range(n - 1, -1, -1):
        p = ord(tablica[i][ind])
        cnt[p] -= 1
        res[cnt[p]] = tablica[i]

    return res


def dodawanie_do_tablicy(A: list[str], K: list[str]) -> list[str]:
    result = K
    result.extend(A)
    return result


def sortowanie_n_slow(tablica: list[str]):
    if not tablica:
        return []

    max_len = max(len(element) for element in tablica)
    kubelki = [[] for _ in range(max_len + 1)]

    for napis in tablica:
        kubelki[len(napis)].append(napis)

    aktywne_slowa = []

    for i in range(max_len - 1, -1, -1):
        aktywne_slowa = dodawanie_do_tablicy(aktywne_slowa, kubelki[i + 1])
        aktywne_slowa = counting_sort_str(aktywne_slowa, i)

    for i in range(len(aktywne_slowa)):
        tablica[i] = aktywne_slowa[i]
