from kol2_test import runtests
from queue import PriorityQueue

"""
    Mateusz Portka 432101   O( mlog(m) )

1) Znajduje największy wierzchołek w grafie aby móc stworzyć graf w reprezentacji listy sąsiedztwa   O(m)

2) Buduje graf G przechodząc po wszystkich krawędziach  O(m)

3) Tworzę zbiór poczty_set ponieważ sprawdzanie czy element należy do zbioru jest stałe a nie liniowe  O(1)

4) Uruchamiam algorytm Dijkstry O(mlog(m)), zaczyjąc od wierzchołka startowego s. Tablica changed to jest dwuwymiarowa (typowo tablica dist) która zmienią swoją wartość zależnie od tego 
jaka była poprzednia krawędź. Z racji tego, że korzystamy z kolejki pryriorytetowej to wiemy, że pierwsza wyspa na której jest poczta, to jest poprawny wynik danego przykładu.

Złożoność obliczeniowa: O( m + m + mlog(m) ) -> O( mlog(m) )

"""


def change(mosty: list[tuple[int, int, str]], poczty: list[int], s: int):
    n = 0
    for u, v, _ in mosty:
        n = max(u, v, n)
    n += 1

    poczty_set = set(poczty)

    G = [[] for _ in range(n)]
    for u, v, grupa in mosty:
        if grupa == "F":
            G[u].append((v, 0))
            G[v].append((u, 0))
        else:
            G[u].append((v, 1))
            G[v].append((u, 1))

    pq = PriorityQueue()

    #                                       Frontasi , Bakusi
    changed: list[list[int | float]] = [[float("inf"), float("inf")] for _ in range(n)]
    changed[s] = [0, 0]
    pq.put((0, s, -1))

    while not pq.empty():
        liczba_zmian, vert, poprzednia_krawedz = pq.get()

        if poprzednia_krawedz == -1:
            for child, wladca_mostu in G[vert]:
                changed[child][wladca_mostu] = 0
                pq.put((0, child, wladca_mostu))

        if liczba_zmian > changed[vert][poprzednia_krawedz]:
            continue

        if vert in poczty_set:
            return liczba_zmian

        for child, aktualna_krawedz in G[vert]:
            if aktualna_krawedz == poprzednia_krawedz:
                if changed[child][aktualna_krawedz] > liczba_zmian:
                    changed[child][aktualna_krawedz] = liczba_zmian
                    pq.put((liczba_zmian, child, aktualna_krawedz))
            else:
                if changed[child][aktualna_krawedz] > liczba_zmian + 1:
                    changed[child][aktualna_krawedz] = liczba_zmian + 1
                    pq.put((liczba_zmian + 1, child, aktualna_krawedz))

    return -1


runtests(change, all_tests=True)
