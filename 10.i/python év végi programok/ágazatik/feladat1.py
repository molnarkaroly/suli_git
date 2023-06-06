'''
Írjon függvényt, ami igaz értéket ad vissza, ha egy paraméterül kapott szám négyzetéből 1-et
kivonva XXYY alakú számot kapunk. A függvény felhasználásával keressük meg és írassuk ki
az összes ilyen számot.
'''

#4488

def negyzet(szam):
    negyzet = szam * szam
    szoveg = str(negyzet - 1)
    if len(szoveg) != 4:
        return False
    else:
        if szoveg[0] == szoveg[1] and szoveg[2] == szoveg[3]:
            return True
        else:
            return False
        
print(negyzet(67))
print(negyzet(34))
print(negyzet(32))


