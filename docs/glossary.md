# Glossary

Definitions for **SEO** and onboarding — search-friendly terms used across this ecosystem.

| Term | Definition |
|------|------------|
| **Anti-detect browser** | Browser environment that isolates fingerprints, storage, and often proxies per profile to reduce linkage between sessions. |
| **Antidetect browser** | Common spelling variant of anti-detect browser (same concept). |
| **Fingerprint browser** | Browser or profile stack optimized to control Canvas, WebGL, fonts, and UA signals. |
| **Browser fingerprinting** | Collecting stable signals (Canvas, WebGL, fonts, audio, screen) to identify or cluster browsers. |
| **Multilogin X (MLX)** | Commercial anti-detect platform with profiles, API, and local launcher integration. |
| **Browser profile manager** | Tooling to create, store, and launch many isolated browser profiles. |
| **Profile** | A saved browser identity: fingerprint parameters, cookies, storage, proxy binding. |
| **Digital twin** | Automation that mirrors human timing, input paths, and session patterns—not just static fingerprints. |
| **Stealth automation** | Playwright/Selenium/Puppeteer setups with hooks and launch patterns that lower automation detection. |
| **Local API** | MLX control endpoint on the machine (often documented around port 35000 — confirm in your install). |
| **Canvas / WebGL fingerprint** | Graphics-derived hashes used by sites to cluster browsers; common leak if shared across accounts. |
| **Cookie warming** | Visiting sites to build realistic cookie/history state before high-value actions. |
| **Anti-bot** | Server-side systems (Cloudflare, Akamai, custom scoring) that block or challenge automated traffic. |
| **MMO automation** | Multi-account workflows requiring strict profile isolation (games, social, ads). |
| **Undetectable browser** | Marketing term for stacks that minimize automation and fingerprint leakage (commercial or OSS). |
| **Cloud Real Phone** | Multilogin cloud-hosted **real Android devices** (not emulators) for genuine mobile fingerprints. |
| **MIN50** | Promo code for Multilogin Cloud Real Phone / entry cloud phone bundles at checkout. |
| **SAAS50** | Promo code for Multilogin X desktop plans in this hub's affiliate checkout link. |
| **Launcher API** | Local MLX agent HTTP API — start/stop/quick profiles ([cookbook](multilogin-api/cookbook/)). |

## Vietnamese (Tiếng Việt)

| Thuật ngữ | Định nghĩa ngắn |
|-----------|------------------|
| **Trình duyệt anti-detect** | Profile tách fingerprint, cookie, proxy cho từng tài khoản. |
| **Fingerprint trình duyệt** | Tập tín hiệu nhận diện thiết bị (Canvas, WebGL, UA, font…). |
| **Automation ẩn danh** | Tự động hóa web kèm stealth + hành vi giống người dùng. |

## 中文

| 术语 | 简要定义 |
|------|----------|
| **反检测浏览器** | 每配置文件隔离指纹、存储与代理。 |
| **指纹浏览器** | 控制 Canvas/WebGL/字体等信号的浏览器配置。 |

## Русский

| Термин | Кратко |
|--------|--------|
| **Антидетект-браузер** | Изоляция отпечатка и хранилища на профиль. |
| **Fingerprint browser** | Управление Canvas/WebGL/шрифтами/UA. |

## Related

- [FAQ](faq.md)
- [Repository map](repository-map.md)
