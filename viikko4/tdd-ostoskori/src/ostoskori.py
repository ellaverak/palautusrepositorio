from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []

    def tavaroita_korissa(self):
        maara = 0

        for ostos in self.ostokset:
            maara+=ostos.lukumaara()

        return maara

    def hinta(self):
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if len(self.ostokset) != 0:
            for ostos in self.ostokset:
                if ostos.tuotteen_nimi() == lisattava.nimi():
                    ostos.muuta_lukumaaraa(1)
        else:
            ostos = Ostos(lisattava)
            self.ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
