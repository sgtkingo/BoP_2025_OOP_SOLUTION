"""
SOLUTION!
"""
import random  # Importuje knihovnu pro náhodné generování

def roll(k=6):
    """Hodí kostkou s k stranami a vrátí výsledek hodu."""
    return random.randint(1, k)  # Vrátí náhodné číslo mezi 1 a k (včetně)