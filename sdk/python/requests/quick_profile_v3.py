"""
Start a Quick Profile v3 (ephemeral) via Local Launcher API.
Source: Postman spec archive — trimmed payload for readability.
"""
import os
import json
import requests

HOST = os.getenv("MLX_LAUNCHER_HOST", "launcher.mlx.yt")
PORT = os.getenv("MLX_LAUNCHER_PORT", "45001")

url = f"https://{HOST}:{PORT}/api/v3/profile/quick"

payload = {
    "browser_type": "mimic",
    "core_version": 124,
    "os_type": "linux",
    "automation": "selenium",
    "is_headless": False,
    "parameters": {
        "flags": {
            "audio_masking": "mask",
            "fonts_masking": "custom",
            "geolocation_masking": "custom",
            "graphics_masking": "custom",
            "navigator_masking": "custom",
            "proxy_masking": "custom",
            "timezone_masking": "custom",
            "webrtc_masking": "custom",
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
