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
from flask import send_from_directory
import os

@app.route('/')
def serve_index():
    return send_from_directory('../frontend/build', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend/build', path)