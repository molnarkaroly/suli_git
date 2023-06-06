import random

N = 20
random.seed(100)
A = [random.randint(1, 100) for _ in range(0,N)]
print(*A)

#  sorozat számítás algoritmusa
## összegzés
i = 0
szum = 0
while i < N:
    szum += A[i]
    i += 1
print(f'\n1, A sorozat elemeinek összege {szum}')

szum = 0
for i in range(0,N):
    szum += A[i]
print(f'\n2, A sorozat elemeinek összege {szum}')

szum = 0
for e in A:
    szum += e

print(f'\n3, A sorozat elemeinek összege {szum}')

#csak py-ban müködik a 4. és 5.
print(f'\n4, A sorozat elemeinek összege {sum(e for e in A)}')
print(f'\n5, A sorozat elemeinek összege {sum(A)}')

## Szorzás

szum = 1
for e in A:
    szum *= e
print(f'\n1, A sorozat elemeinek szorzata {szum}')

##Összefűzés
B = ["a", "l", "m", "a", "f", "a",]

szum = ""
for e in B:
    szum += e

print(f'\n1, B sorozat elemeinek összefűzése {szum}')

print("\n eldöntés")
#eldöntés algotitmussa
i = 0
van = False
while i < N and not van:
    if A[i] % 3 == 0:
        van = True
    i += 1
print(f'1, {"Van" if van else "Nincs"} az A sorozatban 3mal osztható elem ')

van = False
for e in A:
    if e % 3 == 0:
        van = True
        break

print(f'\n 2, {"Van" if van else "Nincs"} az A sorozatban 3mal osztható elem ')

while i < N:
    if A[i] % 3 == 0:
        break
    i += 1
    
print(f'\n 3, {"Van" if i < N else "Nincs"} az A sorozatban 3mal osztható elem ')

"""------------------------------------------------------------------------------------------------------------"""

#kiválasztás tétele
i = 0
while A[i] % 2 != 0:
    i += 1
print(f'\n 1, Az első páros szám {A[i]} indexe {i}')

for i in range(len(A)):
    if A[i] % 2 == 0:
        break
print(f'\n 2, Az első páros szám {A[i]} indexe {i}')

# lineáris keresés algoritmusa

i = 0
van = False
while i < N and not van:
    if A[i] % 3 == 0:
        van = True
    i += 1
if van:
    print(f'\n 3, Az első hárommal osztható szám {A[i-1]}') # mert z i +=1 akkor is le fut
else:
    print(f'\n3, Nincs hárommal osztható szám a sorozatban')

van = False
for i in range(N):
    if A[i] % 3 == 0: #10-nél a nincs lehetőséget kell ki írnika 
        van = True
        break
if van:
    print(f'\n 4, Az első hárommal osztható szám {A[i]}') # itt nem történik meg az inek a növelése, nem kell a -1
else:
    print(f'\n4, Nincs hárommal osztható szám a sorozatban')

#---------------------------önálló munka 
#utolsó 3mal osztható elem
van = False
for i in range(N-1, 0, -1): # reversed(range(N))
    if A[i] % 3 == 0: #10-nél a nincs lehetőséget kell ki írnika 
        van = True
        break
if van:
    print(f'\n 4, Az utolsó hárommal osztható szám {A[i]}') # itt nem történik meg az inek a növelése, nem kell a -1
else:
    print(f'\n4, Nincs hárommal osztható szám a sorozatban')

# van e olyan szám aminek mindkét szomszédja pozitív e

