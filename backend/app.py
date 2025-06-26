from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/api/usage", methods=["GET"])
def get_usage():
    data = {
        "living_room": round(random.uniform(1.2, 4.5), 2),
        "bedroom": round(random.uniform(0.8, 2.3), 2),
        "kitchen": round(random.uniform(1.5, 3.7), 2),
    }
    data["total"] = round(data["living_room"] + data["bedroom"] + data["kitchen"], 2)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/api/usage", methods=["GET"])
def get_usage():
    # Simulate random electricity usage data
    data = {
        "living_room": round(random.uniform(1.2, 4.5), 2),
        "bedroom": round(random.uniform(0.8, 2.3), 2),
        "kitchen": round(random.uniform(1.5, 3.7), 2),
    }
    data["total"] = round(data["living_room"] + data["bedroom"] + data["kitchen"], 2)
    return jsonify(data)

if __name__ == "__main__":
    # Bind to 0.0.0.0 and use the PORT environment variable for Render compatibility
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
