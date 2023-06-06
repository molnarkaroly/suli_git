class Tanulo:
    def __init__(self,sor):
        tanulokod, nev, micsoport, acsoport, nyelv, nem, egyuttlakok, testverek = sor.split(';')
        self.tanulokod = int(tanulokod)
        self.nev = nev
        self.micsoport = micsoport
        self.acsoport = acsoport
        self.nyelv = nyelv
        self.nem = nem
        self.egyuttlakok = int(egyuttlakok)
        self.testverek = int(testverek)

tanulok = []
with open("gyakorlás\gyak0426.txt", "r")as f:
    for sor in f.read().splitlines()[0:]:
        tanulok.append(Tanulo(sor))
