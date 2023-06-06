class Kamera:
    def __init__(self,sor):
        ora, perc, azonosito, irany = sor.split(';')
        self.ora = int(ora)
        self.perc = int(perc)
        self.azonosito = int(azonosito)
        self.irany = irany

data = []
with open('kamera.txt', 'r') as f:
    for sor in f.read().splitlines()[0:]:
        data.append(Kamera(sor))

# hányan mentek ki?
db = 0
for e in data:
    if e.irany == "ki":
        db += 1

print(f"{db} ember ment ki")

# hányan jött be?
db = 0
for e in data:
    if e.irany == "be":
        db += 1

print(f"{db} ember jött be")

print(f'{len(data)} ki és bemenet volt')

#hány ember ment ki 8 órakor?
emberek = []
db = 0
for e in data:
    if e.ora == 23 and e.irany == "ki":
        db += 1
        emberek.append(e.azonosito)

print(f'{db} ember ment ki 8 órakor {emberek}')

#a 7es azonosítojú ember hányszor ment ki 22 órakor?
db = 0
kihetesperc = []
for e in data:
    if e.ora == 22 and e.irany == "ki" and e.azonosito == 7:
        db += 1
        kihetesperc.append(e.perc)

print(f'7es azonosítojú ember {db}-szer ment ki 22 órakor \n{kihetesperc} percekkor')

#7es azonosítojú ember hányszor jött be 22 órakor?
db = 0
behetesperc = []
for e in data:
    if e.ora == 22 and e.irany == "be" and e.azonosito == 7:
        db += 1
        behetesperc.append(e.perc)


print(f'7es azonosítojú ember {db}-szer jött be 22 órakor \n{behetesperc}-kor')

# hány ember járkált be és ki 8 és 12 ora közt?
        
db = 0
azonositok = []
for e in data:
    if e.ora > 8 and e.ora < 12 and e.azonosito not in azonositok:
            db +=1
            azonositok.append(e.azonosito)

print(f'{db} ember járkált be és ki 8 és 12 ora közt {azonositok}')


