import random 


DATOTEKA_Z_BESEDAMI = "./Besede.txt"

class Igra:
    """"Razred Igra
        Hrani stanje trenutne igre (beseda, st ugibanj, pomesano besedo)
    """
    def __init__(self):
        self.beseda = self.izberi_besedo()
        self.ugibanja = 0
        self.pomesana = self.vrni_pomesane()
        self.pomoc = 0

    def izberi_besedo(self):
        with open(DATOTEKA_Z_BESEDAMI, 'r', encoding="utf-8") as f: # odpri datoteko z besedami in jo shrani v spremenljivko f
            bazen_besed = [beseda.strip().upper() for beseda in f.readlines()] # formatiranje ter shranjevanje 

        return random.choice(bazen_besed)

    def vrni_pomesane(self):
        return ''.join(random.sample(self.beseda, len(self.beseda)))
    
    def daj_pomoc(self):
        if self.pomoc >= len(self.beseda):
            self.pomoc = self.pomoc - (self.pomoc//len(self.beseda))*len(self.beseda)
        self.pomoc += 1
        dvojec1 = (self.pomoc, self.beseda[self.pomoc - 1])
        return dvojec1

    def poraz(self):
        return self.ugibanja >= 11
    
    def zmaga(self, ugibana_beseda):
        return self.beseda == ugibana_beseda


    def ugibaj(self, ugibana_beseda):
        ugibana_beseda = ugibana_beseda.upper()
        if self.beseda != ugibana_beseda:
            self.ugibanja += 1
            return False
        else:
            return True