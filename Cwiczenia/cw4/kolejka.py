# Kolejka zbudowana na dwóch stosach


class KolejkaNaStosach:
    def __init(self):
        self.stos_wejsciowy = []
        self.stos_wyjsciowy = []

    def dodaj(self, element):
        self.stos_wejsciowy.append(element)

    def pobierz(self):
        if not self.stos_wejsciowy and not self.stos_wyjsciowy:
            return None

        if not self.stos_wyjsciowy:
            while self.stos_wejsciowy:
                element = self.stos_wejsciowy.pop()
                self.stos_wyjsciowy.append(element)

        return self.stos_wyjsciowy.pop()
