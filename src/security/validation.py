# src/security/validation.py
from pydantic import BaseModel, ValidationError

class TeamModel(BaseModel):
    name: str
    country: str
    founded_year: int

def validate_team_input(data):
    try:
        TeamModel(**data)
        return True, None
    except ValidationError as e:
        return False, e.errors()
