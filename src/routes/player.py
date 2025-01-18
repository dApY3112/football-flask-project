# src/routes/player.py
from flask import Blueprint, jsonify
from src.utils.db import execute_query
from src.utils.helpers import format_player_data

player_blueprint = Blueprint("player", __name__)

@player_blueprint.route("/", methods=["GET"])
def get_players():
    rows = execute_query("SELECT * FROM players")
    players = [format_player_data(row) for row in rows]
    return jsonify(players), 200
