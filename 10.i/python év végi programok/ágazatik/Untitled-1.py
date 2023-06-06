ar = int(input("Kérem a termék árát..."))                                                 #10000 
euro = float(input("Mennyi az euro árfolyam...").replace(",","."))                        #385.56
van = float(input("Hány eurod van?...").replace(",","."))                                 #15

if ar < van * euro:
    print("Van elég eurod megvenni a terméket")
else:
    print("Nincs elég eurod")


'''
Kérem a termék árát...1000
Mennyi az euro árfolyam...385.56
Hány eurod van?...15
Van elég eurod megvenni a terméket
'''