import subprocess

def run():
    print("Applying migrations...")
    subprocess.run(["python", "manage.py", "migrate"])
    print("Running tests...")
    subprocess.run(["pytest"])

if __name__ == '__main__':
    run()
