
szinek = ["piros", "kék", "zöld", "fekete", "fehér", "narancs", "piros", "kék", "zöld", "kék", "narancs", "fekete", "piros", "fehér", "zöld", "narancs", "fehér", "piros", "kék", "zöld", "narancs", "fekete", "piros", "kék", "zöld", "piros", "zöld", "fekete", "fehér", "narancs", "piros", "kék", "kék", "fehér", "piros", "fekete", "zöld", "fekete", "kék", "fehér", "piros", "zöld", "narancs", "fekete", "piros", "zöld", "fehér", "narancs", "fekete", "piros", "kék"]

szinekdb = {}

for item in szinek:
    try:
       szinekdb[item] += 1 
    except:
        szinekdb[item] = 1
        
print(szinekdb)

for d, v in szinekdb.items():
    if v == min(szinekdb.values()):
        print(f'{d} és {v}')
