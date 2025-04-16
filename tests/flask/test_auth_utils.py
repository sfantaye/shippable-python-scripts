"""
✅ test_auth_utils.py — Verifies password hashing and checking.
"""
from scripts.flask import auth_utils

def test_hash_and_check_password():
    raw_pw = "testpass123"
    hashed_pw = auth_utils.hash_password(raw_pw)
    assert isinstance(hashed_pw, str)
    assert auth_utils.check_password(raw_pw, hashed_pw)
    assert not auth_utils.check_password("wrongpass", hashed_pw)
