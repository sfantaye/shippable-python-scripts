"""
♻️ restore_db.py — Restores a PostgreSQL DB dump.
"""
import subprocess
import os
import argparse

def restore_db(dump_file):
    db_name = os.getenv("DB_NAME", "postgres")
    user = os.getenv("DB_USER", "postgres")
    subprocess.run(["psql", "-U", user, "-d", db_name, "-f", dump_file], check=True)
    print(f"♻️ DB restored from {dump_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='SQL dump file path')
    args = parser.parse_args()
    restore_db(args.file)
