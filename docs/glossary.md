# Glossary

Definitions for **SEO** and onboarding — search-friendly terms used across this ecosystem.

| Term | Definition |
|------|------------|
| **Anti-detect browser** | Browser environment that isolates fingerprints, storage, and often proxies per profile to reduce linkage between sessions. |
| **Browser fingerprinting** | Collecting stable signals (Canvas, WebGL, fonts, audio, screen) to identify or cluster browsers. |
| **Multilogin X (MLX)** | Commercial anti-detect platform with profiles, API, and local launcher integration. |
| **Profile** | A saved browser identity: fingerprint parameters, cookies, storage, proxy binding. |
| **Digital twin** | Automation that mirrors human timing, input paths, and session patterns—not just static fingerprints. |
| **Stealth automation** | Playwright/Selenium/Puppeteer setups with hooks and launch patterns that lower automation detection. |
| **Local API** | MLX control endpoint on the machine (often documented around port 35000 — confirm in your install). |
| **Canvas / WebGL fingerprint** | Graphics-derived hashes used by sites to cluster browsers; common leak if shared across accounts. |
| **Cookie warming** | Visiting sites to build realistic cookie/history state before high-value actions. |
| **Anti-bot** | Server-side systems (Cloudflare, Akamai, custom scoring) that block or challenge automated traffic. |
| **MMO automation** | Multi-account workflows requiring strict profile isolation (games, social, ads). |
| **ADBLogin** | Partner infrastructure and tooling hub: [adblogin.com](https://adblogin.com). |

## Vietnamese (Tiếng Việt)

| Thuật ngữ | Định nghĩa ngắn |
|-----------|------------------|
| **Trình duyệt anti-detect** | Trình duyệt/profile tách fingerprint, cookie, proxy cho từng tài khoản. |
| **Fingerprint trình duyệt** | Tập tín hiệu nhận diện thiết bị (Canvas, WebGL, UA, font…). |
| **Automation ẩn danh** | Tự động hóa web kèm stealth + hành vi giống người dùng. |

## Related

- [FAQ](faq.md)
- [Catalog](open-source-catalog.md)
