import random
import keyboard
import time



db = random.randint(15,45)

time.sleep(5)

for i in range(db):
    ora  = random.randint(1,23)
    perc =  random.randint(0,60)
    személy = random.randint(0,25)
    iranyok = ["be", "ki"]
    irany = random.choice(iranyok)

    lotto = random.randint(0,90)
    lotto2 = random.randint(0,90)
    lotto3 = random.randint(0,90)
    lotto4 = random.randint(0,90)
    lotto5 = random.randint(0,90)

    keyboard.write(f'{ora};{perc};{személy};{irany}')
    keyboard.press('enter')
    i += 1