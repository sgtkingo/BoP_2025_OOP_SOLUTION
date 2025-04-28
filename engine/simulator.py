import pickle
import random
from IPython.display import clear_output

from engine.world import World
from engine.objects.hero import Hero
from engine.objects.interfaces import ICharacter, IItem

"""
SOLUTION!
"""
class Simulator:
    """Třída simulující herní svět."""
    def __init__(self, world: World = None):
        """
        Konstruktor simulátoru.
        Pokud není předán žádný svět, vytvoří se až ve start_game().
        """
        self.world = world

    def start_game(self):
        """Vytvoří nový svět pouze pokud ještě neexistuje a spustí hru."""
        if self.world is None:
            hero = Hero(name="Player", level=1, symbol="🧙‍♂️")
            self.world = World(width=100, height=100, hero=hero)

        self.world.generate()
        self.run()

    def save_game(self, filename="savegame.pkl"):
        """Uloží aktuální svět do souboru."""
        if self.world is None:
            print("❌ Není co ukládat.")
            return
        with open(filename, "wb") as f:
            pickle.dump(self.world, f)
        print("💾 Hra uložena.")

    def load_game(self, filename="savegame.pkl"):
        """Načte svět ze souboru a pokračuje."""
        try:
            with open(filename, "rb") as f:
                self.world = pickle.load(f)
            print("📂 Hra načtena.")
            self.run()
        except FileNotFoundError:
            print("❌ Uložená hra nenalezena.")

    def run(self):
        print("🎲 Starting the game... Enjoy!")
        """Hlavní herní smyčka."""
        while True:
            self.print_view()

            command = input("\nZadej příkaz (w/a/s/d, save, load, quit): ").strip().lower()

            if command == "quit":
                print("👋 Hra ukončena.")
                break
            elif command == "save":
                self.save_game()
            elif command == "load":
                self.load_game()
                break  # nová smyčka se spustí po načtení
            elif command in ["w", "a", "s", "d"]:
                dx, dy = 0, 0
                if command == "w": dy = -1
                if command == "s": dy = 1
                if command == "a": dx = -1
                if command == "d": dx = 1

                hero = self.world.hero
                new_x = hero.x + dx
                new_y = hero.y + dy

                if self.world.map.in_bounds(new_x, new_y) and self.world.map.get(new_x, new_y).is_walkable():
                    self.world.set(new_x, new_y, hero)
                else:
                    print("🚫 Nelze tam jít.")
            else:
                print("❓ Neznámý příkaz.")

    def print_view(self, view_window=(20,10)):
        """Zobrazí čtvercovou oblast kolem hráče."""
        clear_output(wait=True)

        hero = self.world.hero
        w_half = view_window[0] // 2
        h_half = view_window[1] // 2

        print("🌍 World View:\n")
        for dy in range(-h_half, h_half):
            row = ""
            for dx in range(-w_half, w_half):
                map_x = hero.x + dx
                map_y = hero.y + dy

                if dx == 0 and dy == 0:
                    row += hero.render()
                    continue

                if not self.world.map.in_bounds(map_x, map_y):
                    row += "X"
                    continue

                cell = self.world.get(map_x, map_y)
                char = next((o for o in cell if isinstance(o, ICharacter)), None)
                item = next((o for o in cell if isinstance(o, IItem)), None)

                if char:
                    row += char.render()
                elif item:
                    row += item.render()
                else:
                    row += self.world.map.get(map_x, map_y).render()
            print(row)