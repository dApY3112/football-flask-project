# src/routes/team.py
from flask import Blueprint, request, jsonify
from src.utils.db import execute_query, initialize_db
from src.utils.helpers import format_team_data

team_blueprint = Blueprint("team", __name__)

# Initialize the database
initialize_db()

# Corrected the route path to "/teams"
@team_blueprint.route("/teams", methods=["GET"])
def get_teams():
    rows = execute_query("SELECT * FROM teams")
    teams = [format_team_data(row) for row in rows]
    return jsonify(teams), 200

@team_blueprint.route("/teams", methods=["POST"])
def add_team():
    data = request.json
    execute_query(
        "INSERT INTO teams (name, country, founded_year) VALUES (?, ?, ?)",
        (data["name"], data["country"], data["founded_year"])
    )
    return jsonify({"message": "Team added successfully"}), 201
