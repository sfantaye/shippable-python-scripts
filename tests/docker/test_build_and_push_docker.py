
"""
✅ test_build_and_push_docker.py — Tests Docker build and push operations.
"""
import pytest
from scripts.flask import build_and_push_docker

def test_build_docker_image(monkeypatch):
    monkeypatch.setattr("subprocess.run", lambda *a, **kw: True)
    build_and_push_docker.build_docker_image()

def test_push_docker_image(monkeypatch):
    monkeypatch.setattr("subprocess.run", lambda *a, **kw: True)
    build_and_push_docker.push_docker_image()
