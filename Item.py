class Item:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type


class Weapon(Item):
    def __init__(self, name: str, attack=0, defense=0, value=0, weight=0.0):
        super().__init__(name, type="weapon")
        self.name = name
        self.attack = attack
        self.defense = defense
        self.value = value
        self.weight = weight


class Consumeable(Item):
    def __init__(self, name: str, health_restore=0, mana_restore=0, value=0, weight=0.0):
        super().__init__(name, type="consumeable")
        self.name = name
        self.health_restore = health_restore
        self.mana_restore = mana_restore
        self.value = value
        self.weight = weight