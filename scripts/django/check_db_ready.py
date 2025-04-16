"""
⏱ check_db_ready.py — Repeatedly checks if the DB is ready using Django's check command.

Useful during Docker or CI container startup before migrations.
"""

import subprocess
import time

def wait_for_db(max_retries=10, delay=3):
    for i in range(max_retries):
        try:
            subprocess.run(["python", "manage.py", "check"], check=True)
            print("✅ Database is ready!")
            return True
        except subprocess.CalledProcessError:
            print(f"⏳ Waiting for DB... retry {i + 1}/{max_retries}")
            time.sleep(delay)
    raise Exception("❌ Database not ready after multiple retries.")

if __name__ == '__main__':
    wait_for_db()

