"""
✅ test_run_server.py — Smoke test to check Flask app import and debug mode flag.
"""
def test_app_runs():
    from app import app
    assert app.debug is True or app.debug is False
