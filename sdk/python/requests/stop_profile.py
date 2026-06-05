"""
Stop a running Multilogin X profile via Local Launcher API.
Source: Postman spec archive (Python / requests).
"""
import os
import requests

HOST = os.getenv("MLX_LAUNCHER_HOST", "launcher.mlx.yt")
PORT = os.getenv("MLX_LAUNCHER_PORT", "45001")
PROFILE_ID = os.environ["MLX_PROFILE_ID"]

url = f"https://{HOST}:{PORT}/api/v1/profile/stop/p/{PROFILE_ID}"

response = requests.get(url, headers={"Accept": "application/json"}, timeout=60)
response.raise_for_status()
print(response.json())
