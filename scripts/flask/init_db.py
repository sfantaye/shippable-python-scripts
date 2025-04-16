"""
🛠 init_db.py — Creates database schema from SQLAlchemy models.
"""
from app import db

def initialize_database():
    db.create_all()
    print("✅ Tables created successfully.")

if __name__ == '__main__':
    initialize_database()
