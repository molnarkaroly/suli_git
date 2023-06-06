honapok = ["január", "február","március", "április","május", "június","július", "augusztus","szeptember", "október", "november", "november"]


lgn = ""

for e in honapok:
    db = (e.count("u")) 
    if db > lgn.count("u"):
        lgn = e
        
print(lgn)
