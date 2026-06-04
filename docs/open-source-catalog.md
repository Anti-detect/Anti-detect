# Open-source catalog

Verified index of [@multilogin-automation](https://github.com/multilogin-automation) repositories. CI verifies every `github.com/multilogin-automation/*` link on push to `main`.

**Last reviewed:** 2026-06-04

---

## Core MLX automation

| Repository | Stars (approx.) | Focus | Link |
|------------|-----------------|-------|------|
| **multilogin-automation** | 10 | Master hub: MLX API, fingerprinting, `/templates` (Playwright stealth, config boilerplate) | [repo](https://github.com/multilogin-automation/multilogin-automation) |
| **multilogin-x-getting-started** | 4 | First-time setup, install, first profile launch | [repo](https://github.com/multilogin-automation/multilogin-x-getting-started) |
| **multilogin-x-id-token-retrieval-tools** | 3 | Access tokens, Profile IDs, Workspace IDs | [repo](https://github.com/multilogin-automation/multilogin-x-id-token-retrieval-tools) |

### Templates inside `multilogin-automation`

| File | Stack | Purpose |
|------|-------|---------|
| [`mlx_config_template.py`](https://github.com/multilogin-automation/multilogin-automation/blob/main/templates/mlx_config_template.py) | Python | Multilogin X API connection boilerplate |
| [`playwright_stealth.py`](https://github.com/multilogin-automation/multilogin-automation/blob/main/templates/playwright_stealth.py) | Playwright | Stealth hooks for high-fidelity browsers |
| [`.clinerules.example`](https://github.com/multilogin-automation/multilogin-automation/blob/main/templates/.clinerules.example) | AI agents | Rules for Windsurf/Cline-style tooling |

---

## Cookie & proxy utilities

| Repository | Focus | Link |
|------------|-------|------|
| multilogin_x_auto_cookie_collector | Auto-visit sites to warm cookies per profile | [repo](https://github.com/multilogin-automation/multilogin_x_auto_cookie_collector) |
| mlx_cookie_robot | Cookie Robot for Multilogin X | [repo](https://github.com/multilogin-automation/mlx_cookie_robot) |
| quick_profile_proxy | Launch quick MLX profile with proxy | [repo](https://github.com/multilogin-automation/quick_profile_proxy) |
| mlx_proxy_details | Script to read proxy details for automation | [repo](https://github.com/multilogin-automation/mlx_proxy_details) |
| MultiLogin | Modernized MultiLogin fork, MLX API automation | [repo](https://github.com/multilogin-automation/MultiLogin) |
| SessionBox | Multi-login session utility (check README) | [repo](https://github.com/multilogin-automation/SessionBox) |

---

## Fingerprint & profile managers (OSS)

| Repository | Focus | Link |
|------------|-------|------|
| undetectable-fingerprint-browser | OSS fingerprint spoofing (Canvas/WebGL/UA); Selenium/Playwright/Puppeteer | [repo](https://github.com/multilogin-automation/undetectable-fingerprint-browser) |
| CloakBrowser-Manager | Self-hosted profile manager, Multilogin-style isolation | [repo](https://github.com/multilogin-automation/CloakBrowser-Manager) |
| openMultiLogin | Open MultiLogin implementation (not obfuscated) | [repo](https://github.com/multilogin-automation/openMultiLogin) |

---

## Integrations & utilities

| Repository | Focus | Link |
|------------|-------|------|
| laravel-multilogin-sdk | Laravel integration (check repo README for status) | [repo](https://github.com/multilogin-automation/laravel-multilogin-sdk) |
| user-agent-utils | Parse and analyze User-Agent strings | [repo](https://github.com/multilogin-automation/user-agent-utils) |

---

## Pick by goal

| Goal | Start here |
|------|------------|
| Learn MLX from zero | multilogin-x-getting-started |
| Production templates (Python/Playwright) | multilogin-automation → `/templates` |
| API auth / IDs | multilogin-x-id-token-retrieval-tools |
| Cookie warming | multilogin_x_auto_cookie_collector or mlx_cookie_robot |

---

## SEO keywords per repo (maintainers)

- **multilogin-automation:** `multilogin x api`, `browser fingerprinting`, `stealth scraper`, `playwright stealth`
- **multilogin-x-getting-started:** `multilogin tutorial`, `browser automation setup`
- **undetectable-fingerprint-browser:** `fingerprint browser`, `anti-detect browser open source`
- **CloakBrowser-Manager:** `browser profile manager`, `multilogin alternative self-hosted`

---

## Promo codes

| Code | Use |
|------|-----|
| `SAAS50` | First-time / SaaS partner discount on Multilogin X |
| `MIN50` | Minimum-tier or follow-up checkout offers |

Checkout: [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Related

- [Getting started](getting-started.md)
- [Architecture](architecture.md)
- [Glossary](glossary.md)
- [Main README](../README.md)
