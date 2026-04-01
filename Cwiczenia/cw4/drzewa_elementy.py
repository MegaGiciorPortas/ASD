# znajdź i-ty co do wieklości element w drzewie


class Node:
    def __init__(self, value):
        self.val: int = value
        self.left: None | Node = None
        self.right: None | Node = None


def znajdz_ity_element(root: Node, i: int) -> "int | None":
    licznik = [0]
    wynik: list[None | Node] = [None]

    def in_order(wezel: "Node | None"):
        if wezel is None or wynik[0] is not None:
            return

        in_order(wezel.left)

        if wynik[0] is None:
            licznik[0] += 1

            if licznik[0] == i:
                wynik[0] = wezel
                return

        in_order(wezel.right)

    in_order(root)

    if wynik[0] is not None:
        return wynik[0].val
    return None


def in_orderv2(root: Node | None, x: int, counter: list | None = None) -> int | None:
    # 1. Inicjalizacja "wskaźnika" na starcie (unikamy mutowalnych argumentów domyślnych)
    if counter is None:
        counter = [0]

    # Warunek stopu
    if root is None:
        return None

    # 2. Idziemy w lewo i ŁAPIEMY ewentualny wynik
    lewy_wynik = in_orderv2(root.left, x, counter)

    # Jeśli coś wraca z lewej strony, to znaczy, że znaleźliśmy odpowiedź!
    # Przerywamy dalsze szukanie i natychmiast zwracamy to wyżej.
    if lewy_wynik is not None:
        return lewy_wynik

    # 3. Przetwarzamy nasz obecny węzeł
    counter[0] += 1
    if counter[0] == x:
        return root.val

    # 4. Idziemy w prawo (zwracamy cokolwiek tam znajdziemy)
    prawy_wynik = in_orderv2(root.right, x, counter)
    return prawy_wynik


# zwróc który co do wielkości jest to węzeł


def ktory_to_jest_wezel(root: Node | None, value: int) -> int | None:
    licznik = 0
    wynik = None

    def find_it(wezel: Node | None, value: int) -> None:
        nonlocal licznik, wynik
        if wezel is None or wynik is not None:
            return

        find_it(wezel.left, value)

        if wynik is not None:
            return

        licznik += 1
        if wezel.val == value:
            wynik = licznik
            return

        find_it(wezel.right, value)

    find_it(root, value)

    if wynik is not None:
        return wynik
    return None
