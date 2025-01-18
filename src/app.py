# src/app.py
from flask import Flask, jsonify, request
from routes.team import team_blueprint
from routes.player import player_blueprint
from security.logger import log_event

app = Flask(__name__)  # Enforce strict slashes


# Register Blueprints
app.register_blueprint(team_blueprint, url_prefix="/teams")
app.register_blueprint(player_blueprint, url_prefix="/players")

# Middleware for logging requests
@app.before_request
def log_request():
    log_event(f"Request to {request.path} from {request.remote_addr}")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Football Backend API!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
