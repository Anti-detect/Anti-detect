"""Start profile using stdlib http.client (no requests dependency)."""
import os
import json
import http.client
from urllib.parse import urlencode

HOST = os.getenv("MLX_LAUNCHER_HOST", "launcher.mlx.yt")
PORT = int(os.getenv("MLX_LAUNCHER_PORT", "45001"))
FOLDER_ID = os.environ["MLX_FOLDER_ID"]
PROFILE_ID = os.environ["MLX_PROFILE_ID"]
AUTOMATION = os.getenv("MLX_AUTOMATION_TYPE", "puppeteer")
HEADLESS = os.getenv("MLX_HEADLESS", "false").lower() in ("1", "true", "yes")

qs = urlencode({"automation_type": AUTOMATION, "headless_mode": str(HEADLESS).lower()})
path = f"/api/v2/profile/f/{FOLDER_ID}/p/{PROFILE_ID}/start?{qs}"

conn = http.client.HTTPSConnection(HOST, PORT, timeout=120)
conn.request("GET", path, headers={"Accept": "application/json"})
res = conn.getresponse()
body = res.read().decode()
if res.status >= 400:
    raise RuntimeError(f"{res.status} {body}")
print(json.loads(body))
