class alloviz:
    def __init__(self,sor):
        id, nev, tipus, terulet, vizgyujto = sor.split(';')
        self.id = int(id)
        self.nev = nev
        self.tipus = tipus if tipus != "NULL" else ""
        self.terulet = float(terulet.replace(",","."))  if terulet != "NULL" else 0
        self.vizgyujto = int(vizgyujto) if vizgyujto != "NULL" else 0

lista = []
with open("alloviz.txt", 'r', encoding="utf-8") as f:
   for sor in f.read().splitlines()[1:]:
    lista.append(alloviz(sor))

print(f'Az adatbázisban {len(lista)} elemei szerepelnek')


osszeg = 0
db = 0
for e in lista:
    if e.terulet != 0:
        osszeg += e.terulet
        db += 1

print(f"Az állóvizek területének átlaga {osszeg /db :0.2f}")


db = []
for e in lista:
   if e.terulet > 3 and e.tipus =="bányató":
        db.append(e)

for e in db:
    print(e.nev)

print("feladat: igaz e hogy morvató több van mint bányató? oldja meg a feladatot egy fügvénnyel")

def melyiktobb(egyik,masik,lista): # melyiktobb("morvató","bányató",lista)
    edb = 0
    mdb = 0
    for e in lista:
        if e.tipus == egyik:
            edb += 1
        if e.tipus == masik:
            mdb += 1
    if egyik > masik:
        return True
    elif egyik == masik:
        return False
    else:
        return False
    

print(f'{"igaz" if melyiktobb("morvató","bányató",lista) else "Nem igaz" } hogy morvató több van mint bányató')

