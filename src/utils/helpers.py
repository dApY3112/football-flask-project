# src/utils/helpers.py
import json
from flask import Response

def json_response(data, status_code=200):
    """Helper function to format JSON responses."""
    return Response(
        response=json.dumps(data),
        status=status_code,
        mimetype="application/json"
    )

def format_team_data(team):
    """Format team data for consistent API responses."""
    return {
        "id": team[0],
        "name": team[1],
        "country": team[2],
        "founded_year": team[3]
    }

def format_player_data(player):
    """Format player data for consistent API responses."""
    return {
        "id": player[0],
        "name": player[1],
        "team_id": player[2]
    }
