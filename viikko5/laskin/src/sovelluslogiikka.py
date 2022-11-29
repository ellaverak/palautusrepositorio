class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.edellinen_tulos = 0
        self.tulos = tulos

    class Summa:
        def __init__(self, sovelluslogiikka, lue_syote):
            self.sovelluslogiikka = sovelluslogiikka
            self.lue_syote = lue_syote

        def suorita(self):
            self.sovelluslogiikka.edellinen_tulos = self.sovelluslogiikka.tulos
            self.sovelluslogiikka.tulos += int(self.lue_syote())

    class Erotus:
        def __init__(self, sovelluslogiikka, lue_syote):
            self.sovelluslogiikka = sovelluslogiikka
            self.lue_syote = lue_syote

        def suorita(self):
            self.sovelluslogiikka.edellinen_tulos = self.sovelluslogiikka.tulos
            self.sovelluslogiikka.tulos -= int(self.lue_syote())

    class Nollaus:
        def __init__(self, sovelluslogiikka, lue_syote):
            self.sovelluslogiikka = sovelluslogiikka
            self.lue_syote = lue_syote

        def suorita(self):
            self.sovelluslogiikka.edellinen_tulos = self.sovelluslogiikka.tulos
            self.sovelluslogiikka.tulos = 0

    class Kumoa:
        def __init__(self, sovelluslogiikka, lue_syote):
            self.sovelluslogiikka = sovelluslogiikka
            self.lue_syote = lue_syote

        def suorita(self):
            self.sovelluslogiikka.tulos = self.sovelluslogiikka.edellinen_tulos

