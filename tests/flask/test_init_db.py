"""
✅ test_init_db.py — Tests the DB initialization logic.
"""
import pytest
from scripts.flask import init_db

def test_initialize_database(monkeypatch):
    monkeypatch.setattr("scripts.flask.init_db.db.create_all", lambda: True)
    init_db.initialize_database()

# --- auth_utils.py ---
"""
