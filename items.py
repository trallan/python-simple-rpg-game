from Item import *

# Weapons
woodenSword = Weapon("Wooden Sword", 5, 2, 10, 15.5)
ironSword = Weapon("Iron Sword", 12, 5, 35, 17.5)
demonSword = Weapon("Demon Sword", 55, 20, 550, 35.4)

# Shields
woodenShield = Shield("Wooden Shield", 0, 5, 5, 10.5)

# Armor Head
leatherHelmet = Head("Leather Helmet", 1, 3, 2.5)

# Armors Armor
leatherArmor = Armor("Leather Armor", 1, 2, 4.5)

# Armors Legs
leatherLegs = Legs("Leather Legs", 1, 2, 3.5)

# Armors Boots
leatherBoots = Boots("Leather Boots", 1, 2, 2.5)

healthPotion = Consumeable("Small Health Potion", 25, 0, 5, weight=0.2)
manaPotion = Consumeable("Small Mana Potion", 0, 25, 5, weight=0.2)