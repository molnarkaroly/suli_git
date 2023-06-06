lista =[]

for e in range(1,11):
    if e % 2 == 0:
        lista.append(e)

print(f'A számsorozatban {len(lista)} páros szám van')
print(f'Ezek aszámok pedig a:', end=" ")

for e in lista:
    print(e, end= " ")