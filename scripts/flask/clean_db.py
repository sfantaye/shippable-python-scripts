"""
🧼 clean_db.py — Drops and recreates all tables in a Flask SQLAlchemy DB.
"""
from app import db

def reset_database():
    db.drop_all()
    db.create_all()
    print("✅ Database reset successfully.")

if __name__ == '__main__':
    reset_database()

