def szamitas(szamok, definicio):
    if definicio == "összeg":
        eredmeny = sum(szamok)
    elif definicio == "szorzat":
        eredmeny = 1
        for szam in szamok:
            eredmeny *= szam
    elif definicio == "legnagyobb":
        eredmeny = max(szamok)
    elif definicio == "legkisebb":
        eredmeny = min(szamok)
    else:
        eredmeny = None
    return eredmeny

# Példa használat:

print(szamitas([1, 2, 3], "összeg")) # kimenet: 6
print(szamitas([4, 5, 6], "szorzat")) # kimenet: 120
print(szamitas([7, 8, 9], "legnagyobb")) # kimenet: 9
print(szamitas([10, 11, 12], "legkisebb")) # kimenet: 10


