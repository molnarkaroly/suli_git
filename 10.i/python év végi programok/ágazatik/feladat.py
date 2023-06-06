fogyasztás = int(input("Adja meg az auto fogyasztásást pl [l/100]: "))

# ha egész érték amit be kér akkor int() ha nem egy egész hanem valós szám akkor float() és ponttal kell megadni pl: 6.5 NEM 6,5

tank = int(input("A benzintank érete literben: "))

távolság = int(input("A megtenni kívánt út hossza: "))

km = tank / fogyasztás  * 100

print(f"Az autó {km} kilómétert tud megtenni ha tele tankall indul")

print(f'Az út során {"nem " if km >= távolság else " "}kell tankolnunk ')
