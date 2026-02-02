class Player:
    def __init__(self):
        self.name = "Player"
        self.level = 1
        self.exp = 0
        self.hp = 100
        self.armor = 0
        self.max_hp = 100
        self.damage = 5
        self.inventory = []
        self.equipment_head = None
        self.equipment_armor = None
        self.equipment_legs = None
        self.equipment_boots = None
        self.equipment_rightHand = None
        self.equipment_offHand = None

    def equipItem(self, item):
        if item.type == "rightHand":
            if self.equipment_rightHand == None:
                self.equipment_rightHand = item
                self.armor += item.defense
                self.damage += item.attack
            else:
                self.armor -= self.equipment_rightHand.defense
                self.damage -= self.equipment_rightHand.attack
                self.equipment_rightHand = item
                self.armor += item.defense
                self.damage += item.attack
        elif item.type == "offHand":
            if self.equipment_offHand == None:
                self.equipment_offHand = item
                self.armor += item.defense
            else:
                self.armor -= self.equipment_offHand.defense
                self.equipment_offHand = item
                self.armor += item.defense
        elif item.type == "head":
            if self.equipment_head == None:
                self.equipment_head = item
                self.armor += item.defense
            else:
                self.armor -= self.equipment_head.defense
                self.equipment_head = item
                self.armor += item.defense
        elif item.type == "armor":
            if self.equipment_armor == None:
                self.equipment_armor = item
                self.armor += item.defense
            else:
                self.armor -= self.equipment_armor.defense
                self.equipment_armor = item
                self.armor += item.defense
        elif item.type == "legs":
            if self.equipment_legs == None:
                self.equipment_legs = item
                self.armor += item.defense
            else:
                self.armor -= self.equipment_legs.defense
                self.equipment_legs = item
                self.armor += item.defense
        elif item.type == "boots":
            if self.equipment_boots == None:
                self.equipment_boots = item
                self.armor += item.defense
            else:
                self.armor -= self.equipment_boots.defense
                self.equipment_boots = item
                self.armor += item.defense
        else:
            return "Cant equip that item"
        