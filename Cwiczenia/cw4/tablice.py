# T[n] tablica, dla każdego T[i] należy do (0,N)
# nie ma dwoch takich samych wartosci w tablicy
# znalexc takie wartosci w tablicy ze T[i+1] - T[i] bedzie najwieksze


def zadanie1(T: list[int]) -> int | float:
    n = len(T)
    if n < 2:
        return 0

    min_val, max_val = min(T), max(T)
    if (
        min_val == max_val
    ):  # oznacza to ze cala talblica skalada sie z jednej i tej smaej liczby i jest ich conjamniej 2
        return 0

    buckets_min = [float("inf")] * (n + 1)
    buckets_max = [float("-inf")] * (n + 1)

    for num in T:
        ind = int(((num - min_val) / (max_val - min_val)) * n)
        buckets_min[ind] = min(buckets_min[ind], num)
        buckets_max[ind] = max(buckets_max[ind], num)

    max_gap = 0
    prev = buckets_max[0]

    for i in range(1, n + 1):
        if buckets_max[i] != float("-inf"):
            max_gap = max(max_gap, buckets_min[i] - prev)
            prev = buckets_max[i]

    return max_gap


# T[n] dl każdego T[i] należy do { 0 ..  k-1 }
# znajdz i,j T[i:j] zawiera wszystkie wartości
def zadanie2(T: list[int], k: int) -> tuple[int, int]:
    n = len(T)
    min_len = float("inf")
    counter = 0
    cnt = [0] * k
    i = 0
    best_i, best_j = -1, -1

    for j in range(n):
        if cnt[T[j]] == 0:
            counter += 1
        cnt[T[j]] += 1

        while counter == k:
            obecna_dlugosc = j - i + 1
            if obecna_dlugosc < min_len:
                min_len = obecna_dlugosc
                best_i, best_j = i, j

            cnt[T[i]] -= 1

            if cnt[T[i]] == 0:
                counter -= 1

            i += 1

    return best_i, best_j
