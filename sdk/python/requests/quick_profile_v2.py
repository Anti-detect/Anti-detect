"""Quick Profile v2 — proxy in parameters block (v3 moves proxy to root)."""
import json
import os
import requests

HOST = os.getenv("MLX_LAUNCHER_HOST", "launcher.mlx.yt")
PORT = os.getenv("MLX_LAUNCHER_PORT", "45001")
url = f"https://{HOST}:{PORT}/api/v2/profile/quick"

payload = {
    "browser_type": "mimic",
    "core_version": 124,
    "os_type": "linux",
    "is_headless": False,
    "parameters": {
        "flags": {
            "navigator_masking": "custom",
            "proxy_masking": "custom",
            "timezone_masking": "custom",
        },
        "proxy": {
            "host": os.getenv("MLX_PROXY_HOST", "host.example"),
            "type": "http",
            "port": int(os.getenv("MLX_PROXY_PORT", "8080")),
            "username": os.getenv("MLX_PROXY_USER", ""),
            "password": os.getenv("MLX_PROXY_PASS", ""),
        },
    },
}

response = requests.post(
    url,
    headers={"Content-Type": "application/json", "Accept": "application/json"},
    data=json.dumps(payload),
    timeout=120,
)
response.raise_for_status()
print(response.json())
