# scripts/django/deploy_to_heroku.py

import subprocess
import sys
import os

def heroku_login():
    """
    Logs into Heroku via the Heroku CLI.
    """
    print("Logging into Heroku...")
    subprocess.run(["heroku", "login"], check=True)

def create_heroku_app():
    """
    Creates a new Heroku app if one doesn't exist. This assumes you're in the root directory of your project.
    """
    print("Creating Heroku app...")
    result = subprocess.run(
        ["heroku", "create"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode == 0:
        print(f"Heroku app created: {result.stdout.decode()}")
    else:
        print(f"Error creating app: {result.stderr.decode()}")
        sys.exit(1)

def push_to_heroku():
    """
    Pushes the local codebase to Heroku.
    """
    print("Pushing to Heroku...")
    subprocess.run(["git", "push", "heroku", "main"], check=True)

def run_migrations():
    """
    Runs database migrations on Heroku after the app has been deployed.
    """
    print("Running migrations on Heroku...")
    subprocess.run(["heroku", "run", "python manage.py migrate"], check=True)

def deploy():
    """
    Full deployment routine for a Django project to Heroku.
    """
    try:
        heroku_login()
        create_heroku_app()
        push_to_heroku()
        run_migrations()
        print("Deployment to Heroku successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during deployment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    deploy()

