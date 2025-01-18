# src/tests/test_validation.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.security.validation import validate_team_input

def test_valid_input():
    valid_data = {"name": "Team A", "country": "USA", "founded_year": 1990}
    result, _ = validate_team_input(valid_data)
    assert result is True

def test_invalid_input():
    invalid_data = {"name": "Team B", "country": "USA"}
    result, errors = validate_team_input(invalid_data)
    assert result is False
