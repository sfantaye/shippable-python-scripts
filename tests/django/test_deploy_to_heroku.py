# tests/test_deploy_to_heroku.py

import pytest
from unittest import mock
import subprocess
from scripts.django.deploy_to_heroku import deploy, heroku_login, create_heroku_app, push_to_heroku, run_migrations

# Mock subprocess.run to prevent actual Heroku commands from running
@pytest.fixture
def mock_subprocess_run():
    with mock.patch("subprocess.run") as mock_run:
        yield mock_run

def test_heroku_login(mock_subprocess_run):
    mock_subprocess_run.return_value.returncode = 0  # Simulate successful login
    heroku_login()
    mock_subprocess_run.assert_called_with(["heroku", "login"], check=True)

def test_create_heroku_app(mock_subprocess_run):
    mock_subprocess_run.return_value.returncode = 0  # Simulate app creation success
    create_heroku_app()
    mock_subprocess_run.assert_called_with(["heroku", "create"], check=True)

def test_push_to_heroku(mock_subprocess_run):
    mock_subprocess_run.return_value.returncode = 0  # Simulate successful push
    push_to_heroku()
    mock_subprocess_run.assert_called_with(["git", "push", "heroku", "main"], check=True)

def test_run_migrations(mock_subprocess_run):
    mock_subprocess_run.return_value.returncode = 0  # Simulate successful migration
    run_migrations()
    mock_subprocess_run.assert_called_with(["heroku", "run", "python manage.py migrate"], check=True)

def test_deploy(mock_subprocess_run):
    # Test the full deployment pipeline
    mock_subprocess_run.return_value.returncode = 0  # Simulate successful deployment steps
    deploy()
    
    # Assert all steps were called
    mock_subprocess_run.assert_any_call(["heroku", "login"], check=True)
    mock_subprocess_run.assert_any_call(["heroku", "create"], check=True)
    mock_subprocess_run.assert_any_call(["git", "push", "heroku", "main"], check=True)
    mock_subprocess_run.assert_any_call(["heroku", "run", "python manage.py migrate"], check=True)
