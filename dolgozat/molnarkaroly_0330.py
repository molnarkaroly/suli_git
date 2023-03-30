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
with open("/workspaces/suli/dolgozat/telepules.txt", "r") as f:
  for sor in f.read().splitlines()[1:]:
    telepulesek.append(Telepules(sor))

db = 0
for e in telepulesek:
   if e.rang == "város":
      db += 1

print(db)
