import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        self.health = health
        self.strength = strength

    def battleCry(self):
        return f"Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking: Viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon: Saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        rand_saxon = self.saxonArmy[random.randint(0, len(self.saxonArmy) - 1)]
        rand_viking = self.vikingArmy[random.randint(0, len(self.vikingArmy) - 1)]
        rand_saxon.receiveDamage(rand_viking.strength)
        
    
    # def saxonAttack(self):
    #     # your code here

    # def showStatus(self):
    #     # your code here
    # pass