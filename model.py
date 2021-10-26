<<<<<<< HEAD
PRAVILNO_MESTO_IN_CRKA = 'x'
NEPRAVILO_MESTO_IN_CRKA = '-'
=======

>>>>>>> 80858d2af68bead28a54e3714cc7cd06b1d21285

import random 
import json

<<<<<<< HEAD
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
=======
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

                






>>>>>>> 80858d2af68bead28a54e3714cc7cd06b1d21285




with open('/Users/pavlanovak/Desktop/uvp 2021/Iskanje-besed-UVP/Besede.txt', 'r') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]


    def nova_igra():
        beseda = random.choice(bazen_besed)
<<<<<<< HEAD
        return Igra(beseda, [])
=======
        return Igra(beseda)

class Ugibanje:
    def __init__(self, stanje, datoteka_z_besedami):
        self.igre = {}
        self.datoteka_s_stanjem = stanje
        self.datoteka_z_besedami = datoteka_z_besedami
    
    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        with open(self.datoteka_z_besedami, 'r') as f:
            bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]
        igra = nova_igra()
        beseda = random.choice(bazen_besed)
        igra = Igra(beseda)
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igro_v_datoteko()
        return id_igre

    def zapisi_igro_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w') as f:
            igre_predelano = {id_igre : ((igra.beseda, igra.ugibanja, igra.stanje, igra.tocke), stanje) for (id_igre, (igra, stanje)) in self.igre.items()}
            json.dump(igre_predelano, f)
    
    def nalozi_igre_iz_datoteke(self):
            with open(self.datoteka_s_stanjem, 'r') as f:
                igre_predelano = json.load(f)
                self.igre = { int(id_igre): (Igra(beseda, ugibanja, stanje, tocke), stanje) for (id_igre, ((beseda, ugibanja, stanje, tocke), stanje)) in igre_predelano.items()}
            
    def ugibaj(self, id_igre, beseda):
        self.nalozi_igre_iz_datoteke()
        (igra, _) = self.igre[id_igre]
        stanje = igra.ugibaj(beseda)
        self.igre[id_igre] = (igra, stanje)
        self.zapisi_igro_v_datoteko()
>>>>>>> 80858d2af68bead28a54e3714cc7cd06b1d21285
