import subprocess
import pytest
from scripts.django import check_db_ready

def test_wait_for_db_success(monkeypatch):
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: 0)
    assert check_db_ready.wait_for_db(max_retries=2) == True

def test_wait_for_db_failure(monkeypatch):
    def fail_run(*args, **kwargs):
        raise subprocess.CalledProcessError(1, "cmd")
    monkeypatch.setattr(subprocess, "run", fail_run)

    with pytest.raises(Exception, match="Database not ready after multiple retries."):
        check_db_ready.wait_for_db(max_retries=2, delay=0)

