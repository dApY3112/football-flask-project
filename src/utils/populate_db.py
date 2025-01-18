# src/utils/populate_db.py
import os
import sys
# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_root)
from src.utils.db import execute_query
def populate_data():
    teams = [
        {"name": "Manchester United", "country": "England", "founded_year": 1878},
        {"name": "Real Madrid", "country": "Spain", "founded_year": 1902},
        {"name": "Barcelona", "country": "Spain", "founded_year": 1899},
        {"name": "Juventus", "country": "Italy", "founded_year": 1897},
        {"name": "Paris Saint-Germain", "country": "France", "founded_year": 1970},
        {"name": "Bayern Munich", "country": "Germany", "founded_year": 1900},
        {"name": "Liverpool", "country": "England", "founded_year": 1892},
        {"name": "Chelsea", "country": "England", "founded_year": 1905},
        {"name": "AC Milan", "country": "Italy", "founded_year": 1899},
        {"name": "Borussia Dortmund", "country": "Germany", "founded_year": 1909},
    ]

    players = [
        {"name": "Cristiano Ronaldo", "team_id": 1},
        {"name": "Bruno Fernandes", "team_id": 1},
        {"name": "Karim Benzema", "team_id": 2},
        {"name": "Vinícius Júnior", "team_id": 2},
        {"name": "Lionel Messi", "team_id": 3},
        {"name": "Pedri", "team_id": 3},
        {"name": "Paulo Dybala", "team_id": 4},
        {"name": "Adrien Rabiot", "team_id": 4},
        {"name": "Kylian Mbappé", "team_id": 5},
        {"name": "Neymar Jr.", "team_id": 5},
        {"name": "Robert Lewandowski", "team_id": 6},
        {"name": "Thomas Müller", "team_id": 6},
        {"name": "Mohamed Salah", "team_id": 7},
        {"name": "Virgil van Dijk", "team_id": 7},
        {"name": "Raheem Sterling", "team_id": 8},
        {"name": "Thiago Silva", "team_id": 8},
        {"name": "Zlatan Ibrahimović", "team_id": 9},
        {"name": "Olivier Giroud", "team_id": 9},
        {"name": "Jude Bellingham", "team_id": 10},
        {"name": "Marco Reus", "team_id": 10},
    ]

    for team in teams:
        execute_query(
            "INSERT INTO teams (name, country, founded_year) VALUES (?, ?, ?)",
            (team["name"], team["country"], team["founded_year"])
        )

    for player in players:
        execute_query(
            "INSERT INTO players (name, team_id) VALUES (?, ?)",
            (player["name"], player["team_id"])
        )

if __name__ == "__main__":
    populate_data()
