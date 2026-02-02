from flask import Flask, render_template, request, url_for
from GameState import GameState
from Player import Player
from enemies import ENEMIES
from items import *

app = Flask(__name__)

player = Player()
gameState = GameState(player)

gameState.player.inventory.append(woodenSword)
gameState.player.inventory.append(ironSword)
gameState.player.inventory.append(demonSword)
gameState.player.inventory.append(woodenShield)
gameState.player.inventory.append(healthPotion)
gameState.player.inventory.append(manaPotion)

gameState.player.equipItem(woodenShield)
gameState.player.equipItem(leatherHelmet)
gameState.player.equipItem(leatherArmor)
gameState.player.equipItem(leatherLegs)
gameState.player.equipItem(leatherBoots)
gameState.player.equipItem(demonSword)

VALID_STATES = {"shop", "battle", "inventory", "exploration"}

@app.route("/")
def start():
    return render_template("index.html", gameState=gameState)

@app.route("/<state>")
def state(state=None):
    if state not in VALID_STATES:
        return "404", 404

    zone = request.args.get("zone")
    enemy_key = request.args.get("enemy", None)

    if enemy_key:
        enemy = ENEMIES.get(enemy_key)
    else:
        enemy = None

    gameState.state = state
    gameState.zone = zone
    gameState.enemy = enemy

    return render_template(f"{state}.html", gameState=gameState)


if __name__ == "__main__":
    app.run(debug=True)