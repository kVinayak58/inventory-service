from flask import Flask, jsonify
import os

app = Flask(__name__)
SERVICE_NAME = os.getenv("SERVICE_NAME", "inventory-service")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
PORT = int(os.getenv("PORT", "5003"))


@app.route("/health")
def health():
    return jsonify({"status": "UP", "service": SERVICE_NAME, "environment": ENVIRONMENT})


@app.route("/api/inventory")
def list_items():
    return jsonify([{"id": 1, "service": SERVICE_NAME}])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
