class Enemy:
    def __init__(self, name: str, hp: int, atk: int, defense: int, exp: int, gold: int):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.exp = exp
        self.loot = []