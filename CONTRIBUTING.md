# Contributing

Thank you for improving the Anti-detect documentation and SDK hub.

## What belongs here

- README and `docs/` improvements (clarity, SEO, accuracy)
- SDK examples in [`sdk/`](sdk/) and [cookbook](docs/multilogin-api/cookbook/)
- FAQ in any supported locale
- API spec updates via `scripts/archive-postman-html.py`
- Typos, broken links, accessibility

Keep all content **self-contained in this repo** — do not add links to external kit organizations.

## Supported README locales

| File | Language |
|------|----------|
| [README.md](README.md) | English |
| [README.vi.md](README.vi.md) | Tiếng Việt |
| [README.zh-CN.md](README.zh-CN.md) | 中文 |
| [README.ru.md](README.ru.md) | Русский |
| [README.id.md](README.id.md) | Bahasa Indonesia |
| [README.pt-BR.md](README.pt-BR.md) | Português (BR) |
| [README.ko.md](README.ko.md) | 한국어 |
| [README.ja.md](README.ja.md) | 日本語 |
| [README.th.md](README.th.md) | ไทย |
| [README.es.md](README.es.md) | Español |

Sync promo codes **`SAAS50`** / **`MIN50`** and pricing URL across locales ([docs/urls.md](docs/urls.md)).

## How to contribute

1. Fork and branch from `main`.
2. One topic per pull request when possible.
3. Run locally: `python scripts/check-spec-integrity.py` and `.\scripts\verify-docs.ps1`
4. Keep **`SAAS50`** / **`MIN50`** and the [pricing URL](docs/urls.md) on every doc you touch ([pricing-cta.md](docs/pricing-cta.md)).

## Pull request checklist

- [ ] Links point to paths inside this repo or official Multilogin/Postman URLs
- [ ] No secrets in commits
- [ ] No legacy partner branding (`adblogin`, old promo codes, Telegram funnels)
- [ ] No external kit org links (CI enforces this)

## Issues

- **Docs / SDK:** use issue templates in this repo.
- **Security:** [SECURITY.md](SECURITY.md).

## Code of conduct

[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

---

**Multilogin X:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — **`SAAS50`** (Multilogin promo code) · **`MIN50`** (Multilogin Cloud Real Phone)

