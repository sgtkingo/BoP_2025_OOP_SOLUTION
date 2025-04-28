from abc import ABC, abstractmethod
import random

from engine.objects.interfaces import IItem

"""
SOLUTION!
"""
class Weapon(IItem):
    def __init__(self, name, attack, defense, speed, level, cost, symbol="⚔️"):
        super().__init__(name, level, cost, symbol=symbol) # Level a cena je součástí třídy IItem
        # Ostatní parametry patří zbrani
        self.attack = attack
        self.defense = defense
        self.speed = speed

    # Očekává že útočně akce budou vracet hodnotu útoku
    @abstractmethod
    def bash(self) -> int:
        pass

    @abstractmethod
    def swing(self) -> int:
        pass

    # Obranná akce, ta bude vracet hodnotu obrany zbraně
    @abstractmethod
    def block(self) -> int:
        pass

class Sword(Weapon):
    # Nově bude mít meč i atributy level a cost
    # Ty važaduje prarodič IItem
    def __init__(self, name="Sword", level=1, cost=10):
      # Level lze aplikovat pro výpočet náhodných atributů zbraně
      attack  = 10 + random.randint(1, level)
      defense = 5 + random.randint(1, level)
      speed   = 7 + random.randint(1, level)
      super().__init__(name, attack, defense, speed, level, cost, symbol="🗡️")

    def bash(self) -> int:
        dmg = self.attack//2
        print(f"You bash with the pommel of your sword. DMG:{dmg}")
        return dmg

    def swing(self) -> int:
        dmg = self.attack+self.speed
        print(f"You swing your sword in a clean arc. DMG:{dmg}")
        return dmg

    def block(self) -> int:
        deff = (self.defense + self.speed)/2
        print(f"You blocking enemy with patronage. BLOCK:{deff}")
        return deff
    
"""
SOLUTION!
"""
class Food(IItem):
    # Přidám účinky
    benefits = {}

    def __init__(self, name, level, cost, benefits, symbol="🍌"):
        super().__init__(name, level, cost, symbol=symbol)
        self.benefits = benefits
    def __str__(self):
        return super().__str__() + f", benefits:{self.benefits}"

class Chest(IItem):
    # Přidám obsah
    content = {}

    def __init__(self, name, level):
        super().__init__(name, level, level*100, symbol="📦")
        self.generate_random_content()

    def generate_random_content(self):
        self.content = {}
        self.content["gold"] = random.randint(10, 10*self.level)
        weights = [0.2, 0.5, 0.3]
        items = [Sword("Ulumdiel", self.level, self.level*25), Food("Banana", 1, 1, {"health":10}), Food("Pie", 5, 28, {"health":50, "speed":5})]

        self.content["items"] = random.choices(items, weights, k=random.randint(self.level//2, self.level))

    def __str__(self):
        return super().__str__() + f", golds:{self.content.get('gold')}g, items:{[str(item) for item in self.content.get('items')]}"