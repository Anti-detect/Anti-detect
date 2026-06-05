"""Minimal .env loader (no python-dotenv dependency)."""
from pathlib import Path


def load_env(path: str | Path | None = None) -> None:
    import os

    if path is None:
        path = Path(__file__).resolve().parents[1] / ".env"
    path = Path(path)
    if not path.is_file():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)
