from kol2testy import runtests
from collections import deque
from queue import PriorityQueue


from kol2testy import runtests


def warrior(G, s, t):
    n = max([max(u, v) for u, v, w in G] + [s, t]) + 1
    NG = [[] for _ in range(n)]

    for u, v, w in G:
        NG[u].append((v, w))
        NG[v].append((u, w))

    dist = [[float("inf") for _ in range(17)] for _ in range(n)]
    dist[s][16] = 0

    buckets = [[] for _ in range(17)]

    buckets[0].append((s, 16))

    items_in_buckets = 1
    current_time = 0

    while items_in_buckets > 0:
        bucket_idx = current_time % 17

        while buckets[bucket_idx]:
            u, stamina = buckets[bucket_idx].pop()
            items_in_buckets -= 1

            if current_time > dist[u][stamina]:
                continue

            if u == t:
                return current_time

            if stamina < 16:
                czas_po_snie = current_time + 8

                if dist[u][16] > czas_po_snie:
                    dist[u][16] = czas_po_snie

                    docelowy_kubelek = czas_po_snie % 17
                    buckets[docelowy_kubelek].append((u, 16))
                    items_in_buckets += 1

            for v, weight in NG[u]:
                if stamina >= weight:
                    czas_po_drodze = current_time + weight

                    if dist[v][stamina - weight] > czas_po_drodze:
                        dist[v][stamina - weight] = czas_po_drodze

                        docelowy_kubelek = czas_po_drodze % 17
                        buckets[docelowy_kubelek].append((v, stamina - weight))
                        items_in_buckets += 1

        current_time += 1

    return -1


runtests(warrior, all_tests=True)
