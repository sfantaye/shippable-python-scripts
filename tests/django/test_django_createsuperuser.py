import subprocess
import os
import pytest
from scripts.django import createsuperuser

def test_create_superuser_env(monkeypatch):
    monkeypatch.setenv("DJANGO_SUPERUSER_USERNAME", "tester")
    monkeypatch.setenv("DJANGO_SUPERUSER_EMAIL", "test@example.com")
    monkeypatch.setenv("DJANGO_SUPERUSER_PASSWORD", "secure123")

    called = {}

    def mock_run(cmd, check):
        called['cmd'] = cmd
        called['check'] = check

    monkeypatch.setattr(subprocess, "run", mock_run)
    createsuperuser.create_superuser()

    assert os.environ["DJANGO_SUPERUSER_USERNAME"] == "tester"
    assert called['cmd'] == ["python", "manage.py", "createsuperuser", "--noinput"]

