from flask import Flask, render_template
from GameState import GameState
from Player import Player
from items import *

app = Flask(__name__)

player = Player()
gameState = GameState(player)
gameState.mode = None

gameState.player.inventory.append(woodenSword)
gameState.player.inventory.append(ironSword)
gameState.player.inventory.append(ironSword)
gameState.player.inventory.append(demonSword)


@app.route("/")
def start():
    return render_template("index.html", gameState=gameState)

@app.route("/<state>")
def state(state=None):
    gameState.mode = state
    return render_template("index.html", gameState=gameState)