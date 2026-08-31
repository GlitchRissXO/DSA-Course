# Module 01.2
# Lab 2: Save Slots
# Date: 08.19.2026
#
# PURPOSE
# Building a game save system to see how Python copies nested objects.
# The save slot has to stay frozen while the live character keeps changing.
#
# RULES:
# Inventory must be a list inside the character.
# Prove the save is independent with an `is` check, not by reading the output.


def new_character(name):
    return {
        "name": name,
        "hp": 100,
        "inventory": ["sword", "potion"],
        "health": 100
    }

def save_game(character): 
    return {
        "name": character["name"],
        "hp": character["hp"],
        "inventory": character["inventory"][:],
        "health": character["health"]
        
    }

hero = new_character("Riss")
slot1 = save_game(hero)

hero["inventory"].append("cursed dagger")
hero["hp"] = 12
hero["health"] = 28

print("lIVE:", hero)
print("SAVE:", slot1)
print("Shared Inventory:", hero["inventory"] is slot1["inventory"])

