"""
🚀 run_server.py — Boots up the Flask development server with debug mode.
"""
from app import app

if __name__ == '__main__':
    app.run(debug=True)
