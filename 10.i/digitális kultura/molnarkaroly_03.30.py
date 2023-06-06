#1. feldadat
kor =  0
kor = int(input("Hány évesnek? "))

könyvek = ['Totyogóknak a kettes számrendszerről', 'Hackeljük meg az óvodát!', 'Felhőtechnológia a menzán','Big data a középiskolában' ]

if kor < 3 :
    print(könyvek[0])

elif kor >= 3 and kor <= 6 :
    print(könyvek[1])

elif kor >= 7 and kor <= 14 :
    print(könyvek[2])

elif kor >= 15 and kor <= 18 :
    print(könyvek[3])
   
#2.feladat
johet_vanilias_cukor = True
johet_tortareszelek = True
johet_fahej = True
johet_tejszinhab = True

def bananos_nyaflaty(johet_vanilias_cukor, johet_tortareszelek, johet_fahej, johet_tejszinhab):
    if johet_vanilias_cukor and johet_tortareszelek:
        return False
    if johet_fahej and not johet_tejszinhab:
        return False
    if not johet_fahej and johet_tejszinhab:
        return False
    return True

# példa használat:
johet_vanilias_cukor = True
johet_tortareszelek = True
johet_fahej = True
johet_tejszinhab = False

if bananos_nyaflaty(johet_vanilias_cukor, johet_tortareszelek, johet_fahej, johet_tejszinhab):
    print("A banános nyaflaty jó!")
else:
    print("A banános nyaflaty nem jó.")

