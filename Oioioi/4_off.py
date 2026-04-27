import sys
import heapq
from math import log
from collections import deque  # DODANO IMPORT KOLEJKI

sys.set_int_max_str_digits(0)


def main():
    # ... (cała pierwsza część kodu zostaje bez zmian, aż do algorytmu Dijkstry) ...
    dane = sys.stdin.read().split()
    if not dane:
        return

    n, m, k = int(dane[0]), int(dane[1]), int(dane[2])
    G = [[] for _ in range(n + 1)]

    idx = 3
    for _ in range(m):
        u, v, waga = int(dane[idx]), int(dane[idx + 1]), int(dane[idx + 2])
        log_waga = log(waga)
        G[u].append((v, log_waga, waga))
        G[v].append((u, log_waga, waga))
        idx += 3

    najciekawsze = [int(dane[idx + i]) for i in range(k)]

    parent = [(-1, -1) for _ in range(n + 1)]
    dist = [[-1, -1] for _ in range(n + 1)]

    Q = []
    heapq.heappush(Q, (0.0, 1, 1))
    dist[1] = [0.0, 1]

    EPS = 1e-9

    while Q:
        obecny_czas, obecne_schroniska, u = heapq.heappop(Q)

        if obecny_czas > dist[u][0] + EPS or (
            abs(obecny_czas - dist[u][0]) < EPS and obecne_schroniska > dist[u][1]
        ):
            continue

        for v, log_waga, prawdziwa_waga in G[u]:
            nowy_czas = obecny_czas + log_waga
            nowe_schroniska = obecne_schroniska + 1

            if (
                dist[v][0] == -1
                or nowy_czas < dist[v][0] - EPS
                or (abs(nowy_czas - dist[v][0]) < EPS and nowe_schroniska < dist[v][1])
            ):
                dist[v] = [nowy_czas, nowe_schroniska]
                parent[v] = (u, prawdziwa_waga)
                heapq.heappush(Q, (nowy_czas, nowe_schroniska, v))

    # --- NOWA, ZOPTYMALIZOWANA KOŃCÓWKA ---
    for cel in najciekawsze:
        if dist[cel][0] == -1:
            continue

        sciezka = []
        obecny = cel

        # Zamiast mnożyć na bieżąco, zbieramy wagi do kolejki
        kolejka_wag = deque()

        while obecny != -1:
            sciezka.append(obecny)
            rodzic, waga_krawedzi = parent[obecny]

            if rodzic != -1:
                # Dodajemy do kolejki zamiast mnożyć
                kolejka_wag.append(waga_krawedzi)

            obecny = rodzic

        sciezka.reverse()

        # Twój pomysł z wyciąganiem z kolejki w praktyce:
        if not kolejka_wag:
            calkowity_czas = 1
        else:
            # Dopóki w kolejce jest więcej niż jedna liczba...
            while len(kolejka_wag) > 1:
                # ...bierzemy dwie z lewej...
                a = kolejka_wag.popleft()
                b = kolejka_wag.popleft()
                # ...mnożymy i wrzucamy na prawą.
                kolejka_wag.append(a * b)

            # Ostatnia liczba w kolejce to nasz wynik
            calkowity_czas = kolejka_wag[0]

        wynik = [str(len(sciezka))] + [str(x) for x in sciezka] + [str(calkowity_czas)]
        print(" ".join(wynik))


if __name__ == "__main__":
    main()
