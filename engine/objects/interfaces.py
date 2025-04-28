"""
SOLUTION!
"""
from abc import ABC, abstractmethod

class ICharacter(ABC):
    """
    Interface for a character in the game.

    This abstract base class defines the structure and behavior
    that all character implementations must follow.
    """
    name = ""
    level = 0
    life = 0
    exp = 0
    x = 0
    y = 0
    is_alive = True
    symbol = ""

    def __init__(self, name:str, level = 1, symbol="🧝"):
      self.name = name
      self.level = level
      self.life = 100 + 10 * level
      self.exp = 1000 * level
      self.x = 0
      self.y = 0
      self.is_alive = True
      self.symbol = symbol

    def render(self):
      return self.symbol

    def set_position(self, x:int, y:int):
      self.x = x
      self.y = y

    def __str__(self):
        alive = "ALIVE" if self.is_alive else "DEAD"
        return f"Character info: {self.symbol}{self.name} ({alive}), level: {self.level}, life: {self.life}, exp: {self.exp}, is on cord [{self.x}, {self.y}]"
    
    
"""
SOLUTION!
"""
from abc import ABC, abstractmethod

class IItem(ABC):
    """
    Interface for a items in the game.

    This abstract base class defines the structure and behavior
    that all items implementations must follow.
    """
    name = ""
    level = 0
    cost = 0
    x = 0
    y = 0
    symbol = ""

    def __init__(self, name:str, level:int, cost:int, symbol="📦"):
        self.name = name
        self.level = level
        self.cost = cost
        self.x = 0
        self.y = 0
        self.symbol = symbol

    def render(self):
      return self.symbol

    def set_position(self, x:int, y:int):
      self.x = x
      self.y = y

    # Metoda __str__ je velmi užitečná, umožňuje nám customizovat co se má vypsat když třídu vypíšeme pomocí print
    def __str__(self):
        return f"Item  info: {self.symbol}{self.name} [{self.level}], cost:{self.cost}g"