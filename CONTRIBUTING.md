# Contributing

Thank you for helping improve the Anti-detect GitHub presence.

## What belongs here

This profile repository welcomes:

- README and `docs/` improvements (clarity, SEO, accuracy)
- Fixed or new links to [@multilogin-automation](https://github.com/multilogin-automation) kits
- FAQ additions in any supported locale (see below)
- Typos, broken badges, and accessibility (`alt` text on images)
- Neutral updates to [docs/browser-landscape.md](docs/browser-landscape.md) (factual, no disparagement)

Executable automation code should go to the appropriate kit repo under **multilogin-automation**, not here.

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

Keep promo codes **`SAAS50`** / **`MIN50`** and the Multilogin pricing URL in sync across locales.

## How to contribute

1. Fork the repository and create a branch from `main`.
2. Make focused changes; one topic per pull request when possible.
3. Use clear commit messages (e.g. `docs: add Playwright quickstart link`).
4. Open a pull request with:
   - What changed and why
   - Screenshots if UI/markdown layout changed

## SEO / docs maintainers

After catalog changes:

1. Follow [docs/seo-checklist.md](docs/seo-checklist.md)
2. Update [CHANGELOG.md](CHANGELOG.md)
3. Verify links (CI runs on push)
4. Keep GitHub topics ≤ **20** in [`.github/repo-metadata.json`](.github/repo-metadata.json)

## Pull request checklist

- [ ] Links use `https://` and point to live destinations (catalog: existing repos only)
- [ ] Headings follow logical order (one H1 in README; H2 for sections)
- [ ] New images include descriptive `alt` text
- [ ] No secrets, API keys, or personal data in commits
- [ ] No legacy partner branding (`adblogin`, old promo codes, Telegram funnels)

## Issues

- **Documentation / links:** use a general issue or the support template.
- **Bugs in SDKs/templates:** open an issue on the specific [multilogin-automation](https://github.com/multilogin-automation) repository.
- **Security:** see [SECURITY.md](SECURITY.md).

## Code of conduct

By participating, you agree to abide by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
