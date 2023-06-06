class Ágyások:
    def __init__(self, sor):
        elso, utolso, szin = sor.split(' ')
        self.elso   =   int(elso)
        self.utolso =   int(utolso)
        self.szin   =   szin

lista = []
with open ('oraifeladat0413\\felajanlas.txt', 'r', encoding='utf-8') as f:
    agyasszam = int(f.readline())
    for sor in f.read().splitlines():
        lista.append(Ágyások(sor))

print(f' 2. feladat \n A felajánlások száma: {len(lista)}')

print(f' 3. feladat \n A beadvány mindkét oldalán ültetők: ')

for i, e in enumerate(lista):
    if e.elso > e.utolso:
        print(i+1, end =' ')

print(f' 4. feladat')
sorszam = int(input("adja meg az ágyás sorszámát: "))
db = 0
szinek = set()
for e in lista:
    if e.elso <= sorszam <= e.utolso or( e.elso > e.utolso and (sorszam >= e.elso or sorszam <= e.utolso)):
        db += 1
        szinek.add(e.szin)
print(f'A felajánlók száma {db}')

elsoszin = ""
for e in lista:
    if e.elso <= sorszam <= e.utolso or( e.elso > e.utolso and (sorszam >= e.elso or sorszam <= e.utolso)):
        elsoszin += e.szin
        break
if elsoszin == "":
    print(f'Ezt az ágyást nem ültetik be')
else:
    print(f'A virágágyás szine ha csak az első ültet {elsoszin} ')

#kiválogatás set() = halmaz
print(f'A virágágysá szinei: ',  end=" ")
for e in szinek:
    print(e, end=" ")

ultetes = [0]*agyasszam
for e in lista:
    if e.elso <= e.utolso:
        for i in range(e.elso, e.utolso +1):
            ultetes[i-1]+= 1
    else:
        for i in range(e.elso, agyasszam):
            ultetes[i-1]+= 1

        for i in range(1, e.utolso + 1):
            ultetes[i-1]+= 1

print(f'\n 5. feladat')

van = False
for e in ultetes:
    if e == 0:
        van = True
        break

if not van:
    print("Minden ágyás beültwtésére van jelentkező")

elif sum(ultetes) >= agyasszam:
        print("Átrendezéssel megoldható")
else:
    print('A beültetés nem oldható meg')        

print('6.feladat')
