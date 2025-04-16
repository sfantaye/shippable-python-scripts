"""
💾 backup_db.py — Dumps the database into a file (PostgreSQL).
"""
import subprocess
import os
from datetime import datetime

def backup_db():
    filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    db_name = os.getenv("DB_NAME", "postgres")
    user = os.getenv("DB_USER", "postgres")
    subprocess.run(["pg_dump", "-U", user, "-f", filename, db_name], check=True)
    print(f"📦 Backup saved to {filename}")

if __name__ == '__main__':
    backup_db()
