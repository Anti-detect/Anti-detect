#!/usr/bin/env python3
"""Quick markdown link smoke check (local approximation of CI link checker)."""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIX = ("mailto:", "#", "javascript:")
IGNORE = re.compile(
    r"github\.com/.*/(issues|pull)|img\.shields\.io|github\.com/.*/actions/workflows"
)
OK_CODES = {200, 206, 403}


def collect_links() -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for url in LINK_RE.findall(text):
            url = url.strip().split()[0]
            if url.startswith(SKIP_PREFIX):
                continue
            if not url.startswith(("http://", "https://")):
                target = (path.parent / url).resolve()
                if not target.exists():
                    found.setdefault(str(path.relative_to(ROOT)), set()).add(f"local:{url}")
                continue
            if IGNORE.search(url):
                continue
            found.setdefault(str(path.relative_to(ROOT)), set()).add(url)
    return found


def head(url: str) -> int | str:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "anti-detect-link-check"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception as exc:  # noqa: BLE001
        return str(exc)


def main() -> int:
    bad: list[str] = []
    for rel, urls in sorted(collect_links().items()):
        for url in sorted(urls):
            if url.startswith("local:"):
                bad.append(f"{rel}: missing {url[6:]}")
                continue
            code = head(url)
            if code not in OK_CODES:
                bad.append(f"{rel}: {url} -> {code}")
    for line in bad:
        print(line)
    print(f"checked; failures: {len(bad)}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
