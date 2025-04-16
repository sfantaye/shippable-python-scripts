import subprocess
import pytest
import os
from scripts.django import backup_db, restore_db

def test_backup(monkeypatch):
    monkeypatch.setenv("DB_NAME", "test_db")
    monkeypatch.setenv("DB_USER", "test")
    monkeypatch.setattr(subprocess, "run", lambda x, check: True)
    backup_db.backup_db()

def test_restore(monkeypatch):
    monkeypatch.setenv("DB_NAME", "test_db")
    monkeypatch.setenv("DB_USER", "test")
    monkeypatch.setattr(subprocess, "run", lambda x, check: True)
    restore_db.restore_db("backup.sql")
