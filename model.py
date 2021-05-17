

import random 
import json

#VSA STANJA
ZACETEK = "Z"
KONEC = "K"
ZMAGA = "w"
PORAZ = "L"
IGRANJE = 'I'

ZACETNE_TOCKE = 100
PRAVILNO_MESTO_IN_CRKA = 'x'
NEPRAVILO_MESTO_IN_CRKA = '-'
# 

class Igra:
    def __init__(self, beseda, ugibanja=None, stanje=ZACETEK, tocke=ZACETNE_TOCKE):
        self.beseda = beseda
        self.ugibanja = ugibanja or []
        self.stanje = stanje
        self.tocke = tocke


    def pokazi_crke_in_dolzino(self):
        crke = []
        for i in self.beseda:
            if i not in crke:
                crke.append(i)
        return (crke, len(self.beseda))



    def ugibaj(self, ugibana_beseda):
        ugibana_beseda = ugibana_beseda.upper()
        zadetki = 0
        for i in range(len(self.beseda)):
            if ugibana_beseda[i] == self.beseda[i]:
                zadetki += 1
        
        self.ugibanja.append((ugibana_beseda, zadetki))
        self.tocke -= 10
        if ugibana_beseda == self.beseda:
            self.stanje = ZMAGA
            return ZMAGA
        elif self.tocke < 0:
            self.stanje = PORAZ
            return PORAZ
        else:
            self.stanje = IGRANJE
            return IGRANJE

                










with open('/Users/pavlanovak/Desktop/uvp 2021/Iskanje-besed-UVP/Besede.txt', 'r') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]


    def nova_igra():
        beseda = random.choice(bazen_besed)
        return Igra(beseda, [])