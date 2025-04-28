import random

def generate_nickname(archetype: str) -> str:
    """
    Generuje náhodnou přezdívku ve formátu: [adjektivum] [tvor] [emoji],
    kde tvor je vybrán podle zadaného archetypu ('npc', 'enemy', 'magic').

    :param archetype: Typ postavy ('npc', 'enemy', 'magic')
    :return: Náhodně vygenerovaná přezdívka
    """

    # Přídavná jména
    adjectives = ["Maxi", "Crazy", "Bald", "Invisible", "Singing"]

    # Emoji symboly
    emojis = ["😎", "⚔️", "🍩", "🔥", "👑"]

    # Slovník tvorů podle archetypu
    creatures_by_archetype = {
        "npc": ["Human", "Elf", "Ent", "Dwarf", "Villager"],
        "enemy": ["Orc", "Troll", "Goblin", "Bandit", "Ogre"],
        "magic": ["Unicorn", "Dragon", "Phoenix", "Ghost", "Fairy"]
    }

    # Kontrola platnosti archetypu
    if archetype not in creatures_by_archetype:
        raise ValueError(f"Unknown archetype: '{archetype}'")

    # Náhodný výběr adjektiva, tvora a emoji
    adj = random.choice(adjectives)
    creature = random.choice(creatures_by_archetype[archetype])
    emoji = random.choice(emojis)

    # Složení přezdívky
    return f"{adj} {creature} {emoji}"


def generate_description() -> str:
    """
    Vygeneruje náhodný popis postavy složený z více částí:
    vzhled, chování a fáma/pověst.

    :return: Popis ve formě souvislé věty.
    """

    # Vzhled postavy
    appearances = [
        "wears a tattered cloak",
        "has glowing red eyes",
        "is unusually tall",
        "smells of lavender",
        "has a mysterious scar"
    ]

    # Chování postavy
    behaviors = [
        "mumbles ancient words",
        "stares into the distance",
        "laughs at inappropriate times",
        "is constantly chewing something",
        "moves with unnatural grace"
    ]

    # Fámy nebo pověsti o postavě
    rumors = [
        "might be a retired assassin",
        "once stole a dragon’s egg",
        "can speak to animals",
        "never sleeps",
        "is hunted by bounty hunters"
    ]

    # Náhodné složení popisu
    part1 = random.choice(appearances)
    part2 = random.choice(behaviors)
    part3 = random.choice(rumors)

    # Vrátíme spojený popis
    return f"This character {part1}, {part2}, and {part3}."
