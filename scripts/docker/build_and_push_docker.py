"""
🐳 build_and_push_docker.py — Builds and pushes a Docker image to Docker Hub.
"""
import subprocess

IMAGE_NAME = "your-dockerhub-username/your-image-name"

def build_docker_image():
    subprocess.run(["docker", "build", "-t", IMAGE_NAME, "."], check=True)
    print("✅ Docker image built.")

def push_docker_image():
    subprocess.run(["docker", "push", IMAGE_NAME], check=True)
    print("📦 Docker image pushed to Docker Hub.")

if __name__ == '__main__':
    build_docker_image()
    push_docker_image()
