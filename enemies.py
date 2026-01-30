from Enemy import Enemy

troll = Enemy(
    name="Troll",
    hp=75,
    atk=10,
    defense=2,
    exp=50,
    gold=10
)

ENEMIES = {
    "troll": troll,
}