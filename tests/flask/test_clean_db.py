"""
✅ test_clean_db.py — Ensures DB reset function works without error.
"""
import pytest
from scripts.flask import clean_db

def test_reset_database(monkeypatch):
    monkeypatch.setattr("scripts.flask.clean_db.db.drop_all", lambda: True)
    monkeypatch.setattr("scripts.flask.clean_db.db.create_all", lambda: True)
    clean_db.reset_database()
