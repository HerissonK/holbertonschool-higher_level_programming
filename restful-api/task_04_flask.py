#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Stockage des utilisateurs en mémoire
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


# Route racine /

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


# Route /data -> liste de tous les usernames

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys()))


# Route /status -> état de l'API

@app.route("/status", methods=["GET"])
def status():
    return "OK"


# Route /users/<username> -> informations d'un utilisateur

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Route /add_user -> ajouter un utilisateur (POST)

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Ajout de l'utilisateur dans le dictionnaire
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


# Point d'entrée du serveur Flask

if __name__ == "__main__":
    app.run()
