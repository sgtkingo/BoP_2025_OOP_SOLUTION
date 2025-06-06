# Globální importy
import numpy as np
import random

# Importuj potřebné lokální moduly a třídy
from engine.map.map import Map
from engine.map.map_elements import *

from engine.generators.name_generators import generate_nickname, generate_description

from engine.objects.items import *
from engine.objects.characters import *
from engine.objects.hero import Hero


"""
SOLUTION!
"""
class World:
    """
    Třída reprezentující herní svět, který obsahuje mapu a objekty.
    Svět je tvořen 2D mřížkou, kde každý prvek může obsahovat různé objekty.
    Svět také obsahuje hrdinu, který je umístěn na mapě.
    """
    def __init__(self, map:Map, hero: Hero):
        """
        Inicializuje herní svět.

        Args:
            map (Map): Instance třídy Map, která reprezentuje herní mapu.
            hero (Hero): Hrdina, který bude umístěn do světa.
        """
        # Ulož si hrdinu
        self.hero:Hero = hero

        # Inicializace mapy
        self.map:Map = map

        # Inicializace 2D vrstvy objektů
        self.objects_layer = np.empty((map.height, map.width), dtype=object)
        for y in range(map.height):
            for x in range(map.width):
                self.objects_layer[y, x] = []

    def generate(self):
        print(f"🧭 Starting generating {self.map.name} world...")
        self.map.generate_random()
        # Umísti hráče na náhodnou pozici na mapě
        hx = random.randint(0, self.map.width - 1)
        hy = random.randint(0, self.map.height - 1)
        # Zkontroluj, zda je pozice volná (neobsazená)
        # Pokud není, najdi jinou pozici
        while not self.map.get(hx, hy).is_walkable():
            hx = random.randint(0, self.map.width - 1)
            hy = random.randint(0, self.map.height - 1)
        # Umísti hrdinu do hry
        self.set(hx, hy, self.hero)

        number_of_objects = self.map.get_area()
        for _ in range(number_of_objects):
          # Enemy
          if random.random() <= 0.025:
            enemy = Enemy(generate_nickname("enemy"), random.randint(1, 36))
            x, y = random.randint(0, self.map.width - 1), random.randint(0, self.map.height - 1)
            self.set(x, y, enemy)

          # NPC
          if random.random() <= 0.015:
            name = generate_nickname(random.choice(["npc", "magic"]))
            desc = generate_description()
            npc = NPC(name, desc, random.randint(1, 36))
            x, y = random.randint(0, self.map.width - 1), random.randint(0, self.map.height - 1)
            self.set(x, y, npc)

        # Truhly
        for _ in range(number_of_objects):
          if random.random() <= 0.01:
            chest = Chest("Chest", random.randint(1, 36))
            x, y = random.randint(0, self.map.width - 1), random.randint(0, self.map.height - 1)
            self.set(x, y, chest)

        # Vzácné předměty
        sword = Sword("Sword Of Truth", 36, 10000)
        food = Food("God Mana", 36, 1000, {"health": 1000, "mana": 1000, "speed": 100}, symbol="🍭")

        self.set(random.randint(0, self.map.width - 1),
                 random.randint(0, self.map.height - 1), sword)

        self.set(random.randint(0, self.map.width - 1),
                 random.randint(0, self.map.height - 1), food)

    def set(self, x: int, y: int, obj: ICharacter | IItem):
        """Umístí objekt do světa a aktualizuje jeho souřadnice."""
        if self.map.in_bounds(x, y):
            # Přidej objekt na novou pozici
            obj.set_position(x, y)
            self.objects_layer[y, x].append(obj)

    def move(self, obj: ICharacter | IItem, x: int, y: int):
        """Pohne objektem na novou pozici."""
        if self.map.in_bounds(x, y):
            # Odstraň objekt z předchozí pozice
            if obj in self.get(obj.x, obj.y):
                self.objects_layer[obj.y, obj.x].remove(obj)
            # Přidej objekt na novou pozici
            obj.set_position(x, y)
            self.objects_layer[y, x].append(obj)

    def get(self, x: int, y: int):
        return self.objects_layer[y, x]  # vrací seznam objektů

    def get_characters_at(self, x: int, y: int):
        return [obj for obj in self.get(x, y) if isinstance(obj, ICharacter)]

    def get_items_at(self, x: int, y: int):
        return [obj for obj in self.get(x, y) if isinstance(obj, IItem)]