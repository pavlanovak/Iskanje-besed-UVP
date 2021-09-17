PRAVILNO_MESTO_IN_CRKA = 'x'
NEPRAVILO_MESTO_IN_CRKA = '-'

import random 
import json

class Igra:
    def __init__(self, beseda, ugibanja, stanje, tocke):
        self.beseda = beseda
        self.ugibanja = []
        self.stanje = ZACETEK, IGRA, ZADEL, PORAZ
        'self.tocke = '

    def pokazi_crke_in_dolzino(self):
        crke = []
        for i in beseda:
            if i not in crke:
                crke.append(i)
            else:
                continue
        return crke




with open('/Users/pavlanovak/Desktop/uvp 2021/Iskanje-besed-UVP/Besede.txt', 'r') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]


    def nova_igra():
        beseda = random.choice(bazen_besed)
        return Igra(beseda, [])