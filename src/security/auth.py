# src/security/auth.py
import jwt
from datetime import datetime, timedelta
from flask import request, jsonify

SECRET_KEY = "your_secret_key"

def generate_jwt(payload):
    payload["exp"] = datetime.utcnow() + timedelta(hours=1)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}

def token_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is missing"}), 403
        try:
            decoded = decode_jwt(token.split(" ")[1])
            request.user = decoded
        except Exception as e:
            return jsonify({"error": str(e)}), 403
        return f(*args, **kwargs)
    return wrapper
