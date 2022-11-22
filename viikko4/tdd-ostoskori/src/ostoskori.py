from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.sisalto = []

    def tavaroita_korissa(self):
        maara = 0

        for ostos in self.sisalto:
            maara+=ostos.lukumaara()

        return maara

    def hinta(self):
        hinta = 0
        for ostos in self.sisalto:
            hinta+=ostos.hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.sisalto:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return

        ostos = Ostos(lisattava)
        self.sisalto.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.sisalto:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.sisalto
