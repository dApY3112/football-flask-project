# src/tests/test_auth.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.security.auth import generate_jwt, decode_jwt

def test_jwt_generation():
    payload = {"user_id": 1, "role": "admin"}
    token = generate_jwt(payload)
    assert token is not None

def test_jwt_decoding():
    payload = {"user_id": 1, "role": "admin"}
    token = generate_jwt(payload)
    decoded = decode_jwt(token)
    assert decoded["user_id"] == 1
    assert decoded["role"] == "admin"
