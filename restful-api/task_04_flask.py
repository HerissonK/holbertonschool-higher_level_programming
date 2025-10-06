#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200


@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys())), 200


@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "OK"}), 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user_route():
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
