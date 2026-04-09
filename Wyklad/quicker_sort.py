import random


def quick_sort_3way(arr):
    _quick_sort_3way(arr, 0, len(arr) - 1)


def _quick_sort_3way(arr, low, high):
    if low >= high:
        return

    pivot_idx = random.randint(low, high)
    pivot = arr[pivot_idx]

    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]

    lt = low  # (Less Than) Koniec przedziału elementów mniejszych od pivota
    i = low  # Aktualnie sprawdzany element
    gt = high  # (Greater Than) Początek przedziału elementów większych od pivota

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    _quick_sort_3way(arr, low, lt - 1)
    _quick_sort_3way(arr, gt + 1, high)
