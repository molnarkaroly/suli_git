import random

class Szelveny:
    def __init__(self,sor):
        elso, masodik, harmadik, negyedik, otodik, = sor.split(";")
        self.elso = int(elso)
        self.alap = sor
        self.masodik = int(masodik)
        self.harmadik = int(harmadik)
        self.negyedik = int(negyedik)
        self.otodik = int(otodik)

    def __repr__(self):
        return sor.replace(";"," ")

szelvenyek = []
with open('lottoadatok.txt', 'r', encoding='utf-8') as f:
    for sor in f.read().splitlines()[0:]:
      szelvenyek.append(Szelveny(sor))

for e in szelvenyek:
    if e.elso > e.masodik and e.masodik > e.harmadik and e.harmadik > e.negyedik and e.negyedik > e.otodik:
        print(e.elso, e.masodik, e.harmadik, e.negyedik, e.otodik)
        print(e.alap.replace(";"," "))

nyertes = random.choice(szelvenyek)
darab = 0
for e in szelvenyek:
    if e == nyertes:
        darab += 1

print(f'a nyertes lapszelvény számai: {nyertes}')
print(f'{darab} darab nyertes szelvény van a listában')

lgn = 0
for e in szelvenyek:
    if (e.elso + e.masodik + e.harmadik + e.negyedik + e.otodik) > lgn:
        lgn = (e.elso + e.masodik + e.harmadik + e.negyedik + e.otodik)

print(f'{lgn} a legnagyobb szelvényen kihúzott számok összege')

dik = 0
for e in szelvenyek:
    if (e.elso + e.masodik + e.harmadik + e.negyedik + e.otodik) == lgn:
        print(f'ez a {dik}. szelvény ami a {e.alap}')
        break
    else:
        dik += 1

