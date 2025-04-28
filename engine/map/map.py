import numpy as np
import random

from engine.map.map_elements import *

"""
SOLUTION!
"""
# Generátor jednoduché náhodné mapy
def generate_map(width: int, height: int, elements:IMapElement, weights:list) -> np.ndarray:
    grid = np.empty((height, width), dtype=object)

    for y in range(height):
        for x in range(width):
            tile_class = random.choices(elements, weights)[0]
            grid[y, x] = tile_class()

    return grid

# Funkce pro výpis mapy do konzole
def print_map(grid: np.ndarray):
    for row in grid:
        print(''.join(tile.render() for tile in row))


"""
SOLUTION!
"""
# Tvoje OOP mapa:
class Map:
    def __init__(self, width: int, height: int, terrains:dict, name="Unknown map", generate_inplace=True):
        self.map_arr = None
        self.width = width
        self.height = height
        self.elements = terrains.get("elements")
        self.weights = terrains.get("weights")
        # Generate defaut random map
        if generate_inplace:
          self.generate_random()
        # Set name
        self.name = name

    def generate_random(self):
        print("🗺️ Creating map... Please wait.")
        self.map_arr = generate_map(self.width, self.height, self.elements, self.weights)

    def get(self, x:int, y:int) -> IMapElement:
        if not self.in_bounds(x,y):
            return None
        return self.map_arr[y][x]

    def get_map(self):
        return self.map_arr

    def get_size(self):
        return self.width, self.height

    def get_area(self):
        return self.width * self.height

    def in_bounds(self, x:int, y:int):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_walkable(self, x:int, y:int):
        if not self.in_bounds(x,y):
            return False
        return self.get(x, y).is_walkable()

    def render(self):
        print_map(self.get_map())