#!/usr/bin/env python3
"""
Extract code snippets into sdk/_generated/.
Source: API-HTML/*.html (optional) or docs/multilogin-api/spec/code-samples/ (default).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API_DIR = ROOT / "API-HTML"
SPEC_SAMPLES = ROOT / "docs" / "multilogin-api" / "spec" / "code-samples"
SDK = ROOT / "sdk" / "_generated"

LANG_MAP = {
    "Multilogin X API-Python-Client.html": ("python", "http_client"),
    "Multilogin X API-Python-Request.html": ("python", "requests"),
    "Multilogin X API-C#.html": ("csharp", "HttpClient"),
    "Multilogin X API-JAVA.html": ("java", "OkHttp"),
}

TAG = re.compile(r"<[^>]+>")
ENTITY = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&#39;": "'"}


def clean_html_code(raw: str) -> str:
    text = TAG.sub("", raw)
    for k, v in ENTITY.items():
        text = text.replace(k, v)
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text.strip()


def extract_blocks(html: str) -> list[str]:
    blocks = re.findall(r"<pre[^>]*><code[^>]*>(.*?)</code></pre>", html, re.DOTALL)
    return [clean_html_code(b) for b in blocks if len(clean_html_code(b)) > 80]


def extract_endpoints(html: str) -> list[tuple[str, str]]:
    return re.findall(
        r'<span class="sc-fzoaKM diFeSb">(GET|POST|PUT|DELETE|PATCH)</span>'
        r'<span class="sc-fzomuh[^"]*">([^<]+)</span>',
        html,
    )


def copy_from_spec() -> None:
    if not SPEC_SAMPLES.is_dir():
        print(f"No {SPEC_SAMPLES} — run archive-postman-html.py first.")
        return
    count = 0
    for lang_dir in SPEC_SAMPLES.iterdir():
        if not lang_dir.is_dir():
            continue
        for variant_dir in lang_dir.iterdir():
            if not variant_dir.is_dir():
                continue
            dest = SDK / lang_dir.name / variant_dir.name
            dest.mkdir(parents=True, exist_ok=True)
            for f in variant_dir.glob("block_*"):
                (dest / f.name).write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
                count += 1
    print(f"Copied {count} blocks from spec/ to {SDK}")


def main() -> None:
    if API_DIR.is_dir() and list(API_DIR.glob("*.html")):
        for fname, (lang, variant) in LANG_MAP.items():
            path = API_DIR / fname
            if not path.exists():
                continue
            html = path.read_text(encoding="utf-8", errors="ignore")
            endpoints = extract_endpoints(html)
            blocks = extract_blocks(html)
            out_dir = SDK / lang / variant
            out_dir.mkdir(parents=True, exist_ok=True)
            for i, block in enumerate(blocks[:8]):
                ext = {"python": "py", "csharp": "cs", "java": "java"}[lang]
                (out_dir / f"block_{i + 1:02d}.{ext}").write_text(block + "\n", encoding="utf-8")
            print(f"{fname} -> {lang}/{variant}: {len(endpoints)} endpoints, {len(blocks)} blocks")
    else:
        copy_from_spec()


if __name__ == "__main__":
    main()
