'''
Írj egy Python függvényt, amely meghatározza egy adott számlistában található páratlan számok
szorzatát.
'''
import random

random.seed(55)
A = [random.randint(1, 100) for _ in range(0,20)]
print(*A)

def pazo(lista):
    szorzat = 1
    for e in lista:
        if e % 2 != 0:
            szorzat *= e
    return szorzat
    
    
print(f'egy adott számlistában található páratlan számok szorzata {pazo(A)}')



