from flask import Blueprint, request, jsonify, current_app
from sqlalchemy.orm import Session
from database import get_db
from models import User
import hashlib
import jwt
from datetime import datetime, timedelta

users_bp = Blueprint("users", __name__, url_prefix="/users")

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

@users_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    db = next(get_db())
    try:
        db_user = User(
            username=data["username"],
            email=data["email"],
            password_hash=hash_password(data["password"])
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return jsonify({"message": "User registered successfully", "user_id": db_user.user_id}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": "Registration failed, possibly duplicate username/email"}), 400

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    db = next(get_db())
    user = db.query(User).filter(User.username == data["username"]).first()
    if user and user.password_hash == hash_password(data["password"]):
        token = jwt.encode(
            {"user_id": user.user_id, "exp": datetime.utcnow() + timedelta(hours=24)},
            current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return jsonify({"token": token, "user_id": user.user_id}), 200
    return jsonify({"error": "Invalid username or password"}), 401