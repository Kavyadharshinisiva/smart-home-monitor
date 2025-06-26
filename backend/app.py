from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route("/api/usage", methods=["GET"])
def get_usage():
    # Simulated electricity usage values (you can replace with real sensor data)
    data = {
        "living_room": round(random.uniform(1.2, 4.5), 2),
        "bedroom": round(random.uniform(0.8, 2.3), 2),
        "kitchen": round(random.uniform(1.5, 3.7), 2),
    }
    data["total"] = round(data["living_room"] + data["bedroom"] + data["kitchen"], 2)
    return jsonify(data)

# Use dynamic port for deployment (Render, Railway, etc.)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
