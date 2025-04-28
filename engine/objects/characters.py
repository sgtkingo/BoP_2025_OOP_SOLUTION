import random

from engine.objects.interfaces import ICharacter

"""
SOLUTION!
"""
class Enemy(ICharacter):
    attack = 0
    defence = 0
    def __init__(self, name, level):
        super().__init__("ENEMY:"+name, level, symbol="🧌")
        self.attack = 10 + random.randint(1, level)
        self.defence = 10 + random.randint(1, level)
    def __str__(self):
      return super().__str__() + f", attack:{self.attack}, defence:{self.defence}"


class NPC(ICharacter):
    description=""

    def __init__(self, name, description, level, symbol="🧝"):
        super().__init__("NPC:"+name, level)
        self.description = description