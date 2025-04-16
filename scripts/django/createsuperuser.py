"""
👤 createsuperuser.py — Auto-creates a Django superuser for dev or CI environments.

It uses environment variables: DJANGO_SUPERUSER_USERNAME, EMAIL, and PASSWORD.
"""

import os
import subprocess

def create_superuser():
    print("🧙 Creating superuser...")
    os.environ.setdefault("DJANGO_SUPERUSER_USERNAME", "admin")
    os.environ.setdefault("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
    os.environ.setdefault("DJANGO_SUPERUSER_PASSWORD", "admin123")

    subprocess.run(["python", "manage.py", "createsuperuser", "--noinput"], check=True)

if __name__ == '__main__':
    create_superuser()

