from engine.objects.interfaces import ICharacter

"""
SOLUTION!
"""
class Hero(ICharacter):
    # Přidám mu inventář
    inventory = {}
    # Přidám atributy
    attributes = {}

    def __init__(self, name, attributes, level=1, symbol="🧙‍♂️"):
        super().__init__(name, level, symbol=symbol)
        self.attributes = attributes
    def __str__(self):
      return super().__str__() + f", attributes:{self.attributes}"
    