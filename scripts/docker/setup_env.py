"""
import os
import subprocess

def create_venv():
    if not os.path.exists(".venv"):
        subprocess.run(["python3", "-m", "venv", ".venv"], check=True)
        print("✅ Virtual environment created.")
    else:
        print("ℹ️ Virtual environment already exists.")

def install_requirements():
    if os.path.exists("requirements.txt"):
        subprocess.run([".venv/bin/pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Requirements installed from requirements.txt")
    elif os.path.exists("pyproject.toml"):
        subprocess.run([".venv/bin/pip", "install", "poetry"], check=True)
        subprocess.run([".venv/bin/poetry", "install"], check=True)
        print("✅ Dependencies installed via Poetry.")
    else:
        print("❌ No recognized dependency file found.")

if __name__ == '__main__':
    create_venv()
    install_requirements()
