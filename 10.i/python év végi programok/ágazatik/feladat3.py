def ibetuk(szoveg):
    db = 0
    for b in szoveg:
        if b == "i":
            db += 1
    return db

print(ibetuk("ribizli"))

honapok = ["január", "február", "március", ]

max = honapok[0]

for e in honapok:
    if ibetuk(max) < ibetuk(e):
        max = e

print(f'A legtöbb "i" betű a {max}-ban van ')

