from Item import *

# name: str, attack=0, defense=0, value=0, weight=0.0
woodenSword = Weapon("🗡️ Wooden Sword", 5, 2, 10, 15.5)
ironSword = Weapon("🗡️ Iron Sword", 12, 5, 35, 17.5)
demonSword = Weapon("🗡️ Demon Sword", 55, 20, 550, 35.4)

healthPotion = Consumeable("🧪 Small Health Potion", 25, 0, 5, weight=0.2)
manaPotion = Consumeable("🧪 Small Mana Potion", 0, 25, 5, weight=0.2)