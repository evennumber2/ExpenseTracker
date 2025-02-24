import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
CORS(app)

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["ExpenseTracker"]  
users_collection = db["users"]
expenses_collection = db["expenses"]

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Expense Tracker API is working!"}), 200

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if users_collection.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({"email": email, "password": hashed_password})

    return jsonify({"message": "User registered successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = users_collection.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=email)
    return jsonify({"access_token": access_token}), 200

@app.route("/add-expense", methods=["POST"])
@jwt_required()
def add_expense():
    user_email = get_jwt_identity()
    data = request.json
    data["user"] = user_email
    expenses_collection.insert_one(data)
    return jsonify({"message": "Expense added successfully!"}), 201

@app.route("/get-expenses", methods=["GET"])
@jwt_required()
def get_expenses():
    user_email = get_jwt_identity()
    expenses = list(expenses_collection.find({"user": user_email}, {"_id": 0}))
    return jsonify(expenses), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
