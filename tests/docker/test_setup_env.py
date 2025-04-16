"""
✅ test_setup_env.py — Tests setup environment script with mock filesystem and subprocess.
"""
import os
import pytest
from unittest import mock
from scripts.flask import setup_env

def test_create_venv(monkeypatch):
    monkeypatch.setattr("os.path.exists", lambda x: False)
    monkeypatch.setattr("subprocess.run", lambda *a, **kw: True)
    setup_env.create_venv()

def test_install_requirements_txt(monkeypatch):
    monkeypatch.setattr("os.path.exists", lambda x: x == "requirements.txt")
    monkeypatch.setattr("subprocess.run", lambda *a, **kw: True)
    setup_env.install_requirements()
