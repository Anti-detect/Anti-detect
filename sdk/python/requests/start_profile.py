"""
Start a saved Multilogin X browser profile via Local Launcher API.
Source: Postman spec archive (Python / requests).
"""
import os
import requests

HOST = os.getenv("MLX_LAUNCHER_HOST", "launcher.mlx.yt")
PORT = os.getenv("MLX_LAUNCHER_PORT", "45001")
FOLDER_ID = os.environ["MLX_FOLDER_ID"]
PROFILE_ID = os.environ["MLX_PROFILE_ID"]
AUTOMATION = os.getenv("MLX_AUTOMATION_TYPE", "puppeteer")
HEADLESS = os.getenv("MLX_HEADLESS", "false").lower() in ("1", "true", "yes")

url = (
    f"https://{HOST}:{PORT}/api/v2/profile/f/{FOLDER_ID}/p/{PROFILE_ID}/start"
    f"?automation_type={AUTOMATION}&headless_mode={str(HEADLESS).lower()}"
)

response = requests.get(url, headers={"Accept": "application/json"}, timeout=120)
response.raise_for_status()
print(response.json())
