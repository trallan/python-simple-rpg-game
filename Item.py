class Item:
    def __init__(self, name: str, type: str, defense: int, value: int, weight: float):
        self.name = name
        self.type = type
        self.defense = defense
        self.value = value
        self.weight = weight


class Weapon(Item):
    def __init__(self, name: str, attack=0, defense=0, value=0, weight=0.0):
        super().__init__(name=name, type="rightHand", defense=defense, value=value, weight=weight)
        self.attack = attack
        
class Shield(Item):
    def __init__(self, name: str, attack=0, defense=0, value=0, weight=0.0):
        super().__init__(name=name, type="offHand", defense=defense, value=value, weight=weight)
        self.attack = attack

class Head(Item):
    def __init__(self, name: str, defense=0, value=0, weight=0.0):
        super().__init__(name=name, type="head", defense=defense, value=value, weight=weight)

class Armor(Item):
    def __init__(self, name: str, defense=0, value=0, weight=0.0):
        super().__init__(name=name, type="armor", defense=defense, value=value, weight=weight)

class Legs(Item):
    def __init__(self, name: str, defense=0, value=0, weight=0.0):
        super().__init__(name=name, type="legs", defense=defense, value=value, weight=weight)

class Boots(Item):
    def __init__(self, name: str, defense=0, value=0, weight=0.0):
        super().__init__(name=name, type="boots", defense=defense, value=value, weight=weight)

class Consumeable(Item):
    def __init__(self, name: str, health_restore=0, mana_restore=0, value=0, weight=0.0, defense=0):
        super().__init__(name=name, type="consumeable", value=value, weight=weight, defense=defense)
        self.health_restore = health_restore
        self.mana_restore = mana_restore