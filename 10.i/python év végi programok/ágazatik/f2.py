
def negyzetszamv(szam):
    negyzet = (szam * szam) - 1
    szoveg = str(negyzet) 
    if len(szoveg) != 4:
        return False
    else:
        if szoveg[0] == szoveg[1] and szoveg[2] == szoveg[3]:
            return True
        else:
            return False
    
hatvanhetesuton = negyzetszamv(67) #true
print(hatvanhetesuton) #True
print(negyzetszamv(32)) #False

print(f'{"Igaz" if negyzetszamv(67) else "Nem igaz"} hogy a megadott szám...' )
print(f'{"Igaz" if negyzetszamv(32) else "Nem igaz"} hogy a megadott szám...' )

db = 0
for e in range(10,100):
    if negyzetszamv(e):
        db += 1

print(f'{db}')

# XXYY
# 4488
