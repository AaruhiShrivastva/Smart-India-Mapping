import json
import os
from backend.auth import get_password_hash

# Simple JSON file database for demo purposes
DB_FILE = "backend/users_db.json"

def get_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {"users": []}

def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)

def user_exists(username: str, email: str) -> bool:
    db = get_db()
    return any(u["username"] == username or u["email"] == email for u in db["users"])

def create_user(username: str, email: str, password: str) -> dict:
    db = get_db()
    user_id = max([u["id"] for u in db["users"]], default=0) + 1
    user = {
        "id": user_id,
        "username": username,
        "email": email,
        "password": get_password_hash(password)
    }
    db["users"].append(user)
    save_db(db)
    return user

def get_user_by_username(username: str) -> dict:
    db = get_db()
    for user in db["users"]:
        if user["username"] == username:
            return user
    return None

def get_user_by_id(user_id: int) -> dict:
    db = get_db()
    for user in db["users"]:
        if user["id"] == user_id:
            return user
    return None
