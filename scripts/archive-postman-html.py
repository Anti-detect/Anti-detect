#!/usr/bin/env python3
"""
One-time (or repeat) migration: Postman Save-Page HTML -> docs/multilogin-api/spec/
Run before deleting API-HTML/. Source of truth becomes spec/ JSON + markdown.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API_DIR = ROOT / "API-HTML"
SPEC = ROOT / "docs" / "multilogin-api" / "spec"

LANG_FILES = {
    "Multilogin X API-Python-Request.html": ("python", "requests"),
    "Multilogin X API-Python-Client.html": ("python", "http.client"),
    "Multilogin X API-C#.html": ("csharp", "HttpClient"),
    "Multilogin X API-JAVA.html": ("java", "OkHttp"),
}

TAG = re.compile(r"<[^>]+>")
ENTITY = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&#39;": "'", "&nbsp;": " "}

CANONICAL_ENDPOINTS = [
    {
        "id": "start-profile",
        "method": "GET",
        "path": "/api/v2/profile/f/{folder_id}/p/{profile_id}/start",
        "name": "Start Browser Profile",
        "query": {"automation_type": "puppeteer|selenium|...", "headless_mode": "true|false"},
        "surface": "launcher",
    },
    {
        "id": "stop-profile",
        "method": "GET",
        "path": "/api/v1/profile/stop/p/{profile_id}",
        "name": "Stop Browser Profile",
        "surface": "launcher",
    },
    {
        "id": "quick-profile-v2",
        "method": "POST",
        "path": "/api/v2/profile/quick",
        "name": "Start Quick Profile",
        "surface": "launcher",
    },
    {
        "id": "quick-profile-v3",
        "method": "POST",
        "path": "/api/v3/profile/quick",
        "name": "Start Quick Profile v3",
        "surface": "launcher",
        "notes": "proxy at root body; fingerprint under parameters",
    },
]

CATEGORIES = [
    {"id": "launcher", "title": "Launcher", "summary": "Start, stop, quick browser profiles (local agent)"},
    {"id": "profile-management", "title": "Profile Management", "summary": "Create, update, delete profiles (cloud)"},
    {"id": "profile-access", "title": "Profile Access Management", "summary": "Sign-in, tokens, workspaces"},
    {"id": "profile-data", "title": "Browser Profile Data", "summary": "Unlock encrypted profile data"},
]


def clean_code(raw: str) -> str:
    text = TAG.sub("", raw)
    for k, v in ENTITY.items():
        text = text.replace(k, v)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def extract_code_blocks(html: str) -> list[str]:
    blocks = re.findall(r"<pre[^>]*><code[^>]*>(.*?)</code></pre>", html, re.DOTALL)
    return [clean_code(b) for b in blocks if len(clean_code(b)) > 60]


def extract_paths(html: str) -> list[str]:
    paths = re.findall(r'"(/api/[^"]+)"', html)
    out = sorted({p.replace("&amp;", "&") for p in paths})
    # normalize UUID examples to placeholders
    normalized = []
    for p in out:
        p = re.sub(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
            "{uuid}",
            p,
            flags=re.I,
        )
        normalized.append(p)
    return sorted(set(normalized))


def main() -> None:
    if not API_DIR.is_dir():
        print(f"No {API_DIR} — using existing spec only.")
        return

    meta = {
        "schema_version": 1,
        "archived_at": date.today().isoformat(),
        "source": {
            "type": "postman-documenter-save-page",
            "live_url": "https://documenter.getpostman.com/view/28533318/2s946h9Cv9",
            "html_files": list(LANG_FILES.keys()),
        },
        "bases": {
            "cloud": "https://api.multilogin.com",
            "launcher_example": "https://launcher.mlx.yt:45001",
        },
        "auth": {
            "type": "Bearer",
            "token_lifetime_minutes": 30,
            "refresh_path": "/user/refresh_token",
            "refresh_method": "POST",
        },
        "categories": CATEGORIES,
        "endpoints": CANONICAL_ENDPOINTS,
    }

    samples_dir = SPEC / "code-samples"
    samples_dir.mkdir(parents=True, exist_ok=True)
    parsed = []

    for fname, (lang, variant) in LANG_FILES.items():
        path = API_DIR / fname
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8", errors="ignore")
        blocks = extract_code_blocks(html)
        lang_dir = samples_dir / lang / variant.replace(".", "_")
        lang_dir.mkdir(parents=True, exist_ok=True)

        manifest = []
        for i, block in enumerate(blocks, start=1):
            ext = {"python": "py", "csharp": "cs", "java": "java"}[lang]
            out_name = f"block_{i:02d}.{ext}"
            (lang_dir / out_name).write_text(block + "\n", encoding="utf-8")
            manifest.append({"file": out_name, "chars": len(block)})

        entry = {
            "html_file": fname,
            "language": lang,
            "variant": variant,
            "api_paths_extracted": extract_paths(html),
            "samples": manifest,
        }
        parsed.append(entry)

        index_path = lang_dir / "index.json"
        index_path.write_text(json.dumps(entry, indent=2), encoding="utf-8")

    meta["exports"] = parsed
    SPEC.mkdir(parents=True, exist_ok=True)
    (SPEC / "postman-collection-meta.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )
    (SPEC / "launcher-endpoints.json").write_text(
        json.dumps(CANONICAL_ENDPOINTS, indent=2), encoding="utf-8"
    )

    readme = SPEC / "README.md"
    readme.write_text(
        f"""# Multilogin X API spec (archived)

Professional archive migrated from `API-HTML/` Postman Save-Page exports on **{date.today().isoformat()}**.

**Source of truth** for maintainers and scripts — safe to delete `API-HTML/` after this exists in git.

## Files

| File | Purpose |
|------|---------|
| [postman-collection-meta.json](postman-collection-meta.json) | Categories, auth, bases, export manifest |
| [launcher-endpoints.json](launcher-endpoints.json) | Canonical Launcher paths |
| [code-samples/](code-samples/) | Extracted Postman code blocks per language |

## Live doc (always newer)

https://documenter.getpostman.com/view/28533318/2s946h9Cv9

## Re-archive after new HTML save

```bash
# Drop new *.html into API-HTML/, then:
python scripts/archive-postman-html.py
python scripts/build-api-catalog.py
# Delete API-HTML/ again if desired
```

## Runnable SDK

Curated scripts (not raw blocks): [`sdk/`](../../../sdk/)
""",
        encoding="utf-8",
    )

    print(f"Archived to {SPEC}")
    print(f"  meta: postman-collection-meta.json")
    print(f"  samples: {len(parsed)} language exports")


if __name__ == "__main__":
    main()
