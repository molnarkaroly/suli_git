class Epulet:
  def __init__(self, sor):
    nev, varos, orszag, magassag, emelet, epult = sor.split(";")
    self.nev = nev
    self.varos = varos
    self.orszag = orszag
    self.magassag = float(magassag.replace(",","."))
    self.emelet = int(emelet)
    self.epult = int(epult)

epuletek= []
with open("ladatok.txt", "r", encoding="utf-8") as f:
  for sor in f.read().splitlines()[1:]:
    epuletek.append(Epulet(sor))

#for e in epuletek:
  #print(e.epult)

print(f"3.2 Feladat | Épületek száma: {len(epuletek)}")

szum = 0
for e in epuletek:
    szum += e.emelet
print(f"3.3 Feladat | Emeletek összege: {szum}")

legmagasabb = epuletek[0]
for e in epuletek:
    if e.magassag > legmagasabb.magassag:
        legmagasabb = e
print(f"3.4 Feladat | A legmagasabb épület adatai:")
print(f"\tNév: {legmagasabb.nev}")
print(f"\tVáros: {legmagasabb.varos}")
print(f"\tOrszág: {legmagasabb.orszag}")
print(f"\tMagasság: {legmagasabb.magassag} m")
print(f"\tEmeletek Száma: {legmagasabb.emelet}")
print(f"\tÉpítés éve: {legmagasabb.epult}")

"""
legmagasabb = max(epuletek, key = lambda x : x.magassag)
print(f"3.4 Feladat | A legmagasabb épület adatai:")
print(f"\tNév: {legmagasabb.nev}")
print(f"\tVáros: {legmagasabb.varos}")
print(f"\tOrszág: {legmagasabb.orszag}")
print(f"\tMagasság: {legmagasabb.magassag} m")
print(f"\tEmeletek Száma: {legmagasabb.emelet}")
print(f"\tÉpítés éve: {legmagasabb.epult}")
"""

van = False
for e in epuletek:
    if e.orszag == "Olaszország":
        van = True
        break
print(f"3.5 Feladat | {'Van' if  van else 'Nincs'} olasz épület az adatok között!")
