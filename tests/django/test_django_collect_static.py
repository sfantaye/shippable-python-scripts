import subprocess
import pytest
from scripts.django import collect_static

def test_collect_static_runs(monkeypatch):
    called = {}

    def mock_run(cmd, check):
        called['cmd'] = cmd
        called['check'] = check
        return 0

    monkeypatch.setattr(subprocess, "run", mock_run)
    collect_static.collect_static()

    assert called['cmd'] == ["python", "manage.py", "collectstatic", "--noinput"]
    assert called['check'] is True

