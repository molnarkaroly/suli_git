class macska:
    def __init__(self, nev, harciero, eletero):
        self.nev = nev
        self.harciero = harciero
        self.eletero = eletero
    
    def harcol(self,macs):
        while self.eletero > 0 and macs.eletero > 0:
            macs.eletero -= self.harciero
            if macs.eletero <= 0:
                print(f"{self.nev} nyert a harcban.")
                break
            self.eletero -= macs.harciero
            if self.eletero <= 0:
                print(f"{macs.nev} nyert a harcban.")
                break

cica1 = macska("Tibi", 50, 100)
cica2 = macska("Szotyi", 60, 110)

cica1.harcol(cica2)