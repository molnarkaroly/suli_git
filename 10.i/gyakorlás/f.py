class beki:
  def __init__(self, sor):
    if sor:  # csak nem-üres sorokat dolgozunk fel
        ora, perc, szem = sor.split(";")
        self.ora = int(ora)
        self.perc = int(perc)
        self.szem = int(szem)

mozgasok = []
with open('adatok.txt', 'r', encoding="utf-8") as f:
    for sor in f.read().splitlines()[1:]:
      mozgasok.append(beki(sor))

lgtszem = mozgasok[0].szem
for e in mozgasok:
  if e.szem > lgtszem:
    lgtszem = e.szem

print(f' a legtöbb személy aki közlekedett az {lgtszem} db embr')
szum = 0
for e in mozgasok:
  szum += e.szem
print(f'átlagosan: {(szum / len(mozgasok)) :.0f} ember haladt át')

db = 0

for e in mozgasok:
  if e.szem > 10:
    db +=1 


print(f'összesen {db}-szer ment el 10-nél több ember')

db = 0
mikor = int(input("ora: "))
mikorment = []
for e in mozgasok:
  if mikor == e.ora:
      db += e.szem
      mikorment.append(e.perc)

print(f'{mikor} órakor {db} személy ment el')

