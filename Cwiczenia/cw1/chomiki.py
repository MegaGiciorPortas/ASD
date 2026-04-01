"""
Chomiki
[a1,b1],[a2,b2],[a3,b3]....[an,bn]
a1 < b1 < a2 < b2 < ... < an < bn
pytamy o minimalna najwieksza odleglosc jak mozemy rozlozyc chomiki
"""


def hamsters(array, amount):
    if amount <= 1:
        return 0

    left = 0
    right = array[-1][1] - array[0][0]
    result = 0

    while left <= right:
        period = (left + right) // 2

        remain = amount - 1
        current = array[0][0]
        idx_nory = 0
        possible = True

        while remain > 0:
            target = current + period

            while idx_nory < len(array) and array[idx_nory][1] < target:
                idx_nory += 1

            if idx_nory == len(array):
                possible = False
                break

            current = max(target, array[idx_nory][0])
            remain -= 1

        if possible:
            result = period
            left = period + 1
        else:
            right = period - 1

    return result
