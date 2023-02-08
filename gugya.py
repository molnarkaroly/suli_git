import keyboard
import time

class Dog:
    def __init__(self, name, éhes, kaja, suly):
        self.name = name
        self.kaja = kaja
        self.ehes = éhes
        self.suly = suly

    def rohangál(self, éhes=False):
        if self.ehes == True:
            print ("nem futik")
        else:
            print ("futkosik")
            self.ehes = True
            self.suly -= 1
            print(self.suly)

    def eszik(self, kaja):
        if self.ehes == True:
            print(f'{self.name} eszik')
            self.suly += kaja
            self.ehes = False
            print (self.suly)
        else:
            print (f'{self.name} a gugya nem éhes')
            self.ehes = False

    def voice(self):
        print("woof")

    
dog = Dog("Ubul", False, 0, 12 )

while True:
    if keyboard.is_pressed("a"):
        dog.voice()
        time.sleep(0.2)
    if keyboard.is_pressed("s"):
        dog.eszik(1)
        time.sleep(0.2)
    if keyboard.is_pressed("d"):
        dog.rohangál()
        time.sleep(0.2)
    if keyboard.is_pressed("f"):
        break
        time.sleep(0.2)


