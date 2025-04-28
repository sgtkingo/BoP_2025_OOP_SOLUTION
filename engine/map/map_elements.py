"""
SOLUTION!
"""
from abc import ABC, abstractmethod
import numpy as np
import random

# Rozhraní pro prvky mapy
class IMapElement(ABC):

    @abstractmethod
    def render(self) -> str:
        """Vrátí znakovou reprezentaci prvku (např. '.' nebo '#')"""
        pass

    @abstractmethod
    def is_walkable(self) -> bool:
        """Vrací True, pokud je možné přes prvek přejít"""
        pass

# Tráva – obyčejné pole
class Grass(IMapElement):
    def render(self) -> str:
        return '.'

    def is_walkable(self) -> bool:
        return True

# Zeď – nepřekonatelná překážka
class Wall(IMapElement):
    def render(self) -> str:
        return '#'

    def is_walkable(self) -> bool:
        return False

# Voda – třeba zpomaluje, ale dá se projít (v budoucnu)
class Water(IMapElement):
    def render(self) -> str:
        return '~'

    def is_walkable(self) -> bool:
        return True