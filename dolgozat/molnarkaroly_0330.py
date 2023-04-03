class Telepules:
    def __init__(self, sor):
        azonosító, neve, rangja, besorolása, területe, népessége, lakások = sor.split(';')
        self.telepules =int(azonosító)
        self.neve = neve
        self.rangja = rangja
        self.besorolás = besorolása
        self.területe = int(területe)
        self.népessége = int(népessége)
        self.lakások = int(lakások)

telepulesek = []
with open("telepules.txt", "r", encoding="utf-8") as f:
  for sor in f.read().splitlines()[0:]:
    telepulesek.append(Telepules(sor))

# Hány város rangú település található?
db = 0
for e in telepulesek:
   if e.rangja == "város":
      db += 1

print(f'\n{db} város rangú település található?')

#Van-e falu rangú település?
van = False
for e in telepulesek:
    if e.rangja == "falu":
        van = True
        break
print(f'\n{"Van " if van else "Nincs"} falu rangú település')
print('\n')
#Írja ki a község rangú települések közül az 1000 főnél népesebb települések nevét és népességét!

for e in telepulesek:
    if e.rangja == "község" and e.népessége > 1000:
        print(f'{e.neve} és a népessége {e.népessége} fő')
        
#Igaz-e, hogy minden Kisteleki kistérségű település lélekszáma kisebb, mint 10000?
van = True
for e in telepulesek:
    if e.besorolás == "Kisteleki" and e.népessége > 10000:
        van = False
        break

print(f'\n{"Igaz" if van else "Nem igaz"} hogy minden Kisteleki kistérségű település lélekszáma kisebb, mint 10000 \n')