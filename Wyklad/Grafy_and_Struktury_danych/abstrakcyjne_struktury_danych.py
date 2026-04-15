from collections import deque


class Node:
    def __init__(self, value):
        self.val = value
        self.next: "Node | None" = None


class StosTablicowy:
    def __init__(self):
        self.stos = []

    def push(self, value):
        self.stos.append(value)

    def pop(self):
        if len(self.stos) > 0:
            return self.stos.pop()
        return None


class StosListowy:
    def __init__(self):
        self.head = None

    def push(self, value):
        nowy_wezel = Node(value)
        nowy_wezel.next = self.head
        self.head = nowy_wezel

    def pop(self):
        if self.head is None:
            return None
        wezel = self.head
        self.head = self.head.next
        return wezel.val


# Kolejka
class KolejkaTablicowa:
    def __init__(self):
        self.kolejka = deque()

    def enqueue(self, value):
        self.kolejka.append(value)

    def dequeue(self):
        if self.kolejka:
            return self.kolejka.popleft()
        return None


class KolejkaListowa:
    def __init__(self):
        self.przod = None
        self.tyl = None

    def enqueue(self, value):
        nowy_wezel = Node(value)
        if self.tyl is None:
            self.tyl = self.przod = nowy_wezel
        else:
            self.tyl.next = nowy_wezel
            self.tyl = nowy_wezel

    def dequeue(self):
        if self.przod is None:
            return None
        wezel = self.przod
        self.przod = self.przod.next

        if self.przod is None:
            self.tyl = None
        return wezel.val


class KolejkaPriorytetowaOdZera:
    def __init__(self):
        self.kopiec = []

    def wstaw(self, priorytet, wartosc):
        self.kopiec.append((priorytet, wartosc))

        index_obecny = len(self.kopiec) - 1
        self._przesun_w_gore(index_obecny)

    def pobierz(self):
        if not self.kopiec:
            return None
        if len(self.kopiec) == 1:
            return self.kopiec.pop()[1]  # Zwracamy samą wartość

        najlepszy = self.kopiec[0]

        self.kopiec[0] = self.kopiec.pop()

        self._przesun_w_dol(0)

        return najlepszy[1]

    def _przesun_w_gore(self, index):
        rodzic = (index - 1) // 2

        # Dopóki nie jesteśmy na szczycie i nasz priorytet jest mniejszy niż rodzica
        while index > 0 and self.kopiec[index][0] < self.kopiec[rodzic][0]:
            self.kopiec[index], self.kopiec[rodzic] = (
                self.kopiec[rodzic],
                self.kopiec[index],
            )

            index = rodzic
            rodzic = (index - 1) // 2

    def _przesun_w_dol(self, index):
        rozmiar = len(self.kopiec)

        while True:
            lewe_dziecko = 2 * index + 1
            prawe_dziecko = 2 * index + 2
            najmniejszy = index
            # Sprawdzamy, czy lewe dziecko istnieje i czy jest mniejsze
            if (
                lewe_dziecko < rozmiar
                and self.kopiec[lewe_dziecko][0] < self.kopiec[najmniejszy][0]
            ):
                najmniejszy = lewe_dziecko

            # Sprawdzamy, czy prawe dziecko istnieje i czy jest mniejsze od "dotychczasowego najmniejszego"
            if (
                prawe_dziecko < rozmiar
                and self.kopiec[prawe_dziecko][0] < self.kopiec[najmniejszy][0]
            ):
                najmniejszy = prawe_dziecko

            # Jeśli okazało się, że któreś z dzieci jest mniejsze, zamieniamy się z nim
            if najmniejszy != index:
                self.kopiec[index], self.kopiec[najmniejszy] = (
                    self.kopiec[najmniejszy],
                    self.kopiec[index],
                )
                index = najmniejszy  # Skaczemy w dół i pętla kręci się dalej
            else:
                # Jeśli nikt pod nami nie jest mniejszy, to znaczy, że jesteśmy we właściwym miejscu
                break
