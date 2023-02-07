class Warrior:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def fight(self, opponent):
        while self.health > 0 and opponent.health > 0:
            opponent.health -= self.strength
            if opponent.health <= 0:
                print(f"{self.name} nyert a harcban.")
                break
            self.health -= opponent.strength
            if self.health <= 0:
                print(f"{opponent.name} nyert a harcban.")
                break

warrior1 = Warrior("Harcos 1", 100, 20)
warrior2 = Warrior("Harcos 2", 100, 35)

warrior1.fight(warrior2)
