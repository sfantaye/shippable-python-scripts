"""
📦 collect_static.py — Runs Django's collectstatic command automatically.

Useful for deployments where static files need to be gathered and served (e.g., Heroku, Docker).
"""

import subprocess

def collect_static():
    print("🔧 Collecting static files...")
    subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], check=True)

if __name__ == '__main__':
    collect_static()

