# Changelog

All notable documentation and hub changes for [Anti-detect/Anti-detect](https://github.com/Anti-detect/Anti-detect).

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- [docs/urls.md](docs/urls.md), [docs/locales.md](docs/locales.md), [docs/fingerprint-checklist.md](docs/fingerprint-checklist.md)
- [README.th.md](README.th.md) (Thai)
- [scripts/verify-docs.ps1](scripts/verify-docs.ps1) — local link/branding checks
- Catalog: [SessionBox](https://github.com/multilogin-automation/SessionBox)
- [docs/browser-landscape.md](docs/browser-landscape.md) — neutral anti-detect market / competitor keyword overview
- Localized profile READMEs: [README.zh-CN.md](README.zh-CN.md), [README.ru.md](README.ru.md), [README.id.md](README.id.md), [README.pt-BR.md](README.pt-BR.md), [README.ko.md](README.ko.md), [README.ja.md](README.ja.md)
- Docs CI **branding guard** — blocks legacy `adblogin` / old promo codes in README and docs (excludes workflow self-reference)
- Sync workflow: homepage drift warning
- GitHub topic `account-management` (20 topics total)
- Expanded SEO topics in [`.github/repo-metadata.json`](.github/repo-metadata.json) (`antidetect-browser`, `fingerprint-browser`, `multilogin-x`, …)

### Changed

- Rebranded hub as neutral **documentation-only** profile (MIT); removed third-party contact blocks
- Promo codes: **`SAAS50`**, **`MIN50`**; affiliate URL → Multilogin pricing with UTM params
- Homepage / FUNDING / issue templates point to official Multilogin pricing
- FAQ and glossary: EN + VI + ZH + RU sections
- Security reporting via GitHub advisories (no public email)

### Removed

- Telegram, legacy partner email/website/ecosystem links
- `adblogin` topic and ADBLogin branding across docs

## [1.1.1] - 2026-06-03

### Fixed

- `sync-repo-settings`: invalid `administration` permission (use `GH_METADATA_TOKEN` + drift checks)
- `labels.yml` format for EndBug/label-sync
- Markdown lint rules (MD051/MD060); link-check ignores for CI badges

### Added

- [docs/setup-github-metadata.md](docs/setup-github-metadata.md) — one-time PAT setup

## [1.1.0] - 2026-06-03

### Added

- Auto-sync GitHub About, homepage, topics via `sync-repo-settings.yml` + `repo-metadata.json`
- Label sync workflow and default issue labels
- Docs CI: verify all `multilogin-automation` repo URLs return HTTP 200

### Changed

- `scripts/set-github-about.ps1` reads from `repo-metadata.json`
- Linguist: mark `scripts/` as documentation (avoid "PowerShell" as primary language)

## [1.0.0] - 2026-06-03

### Added

- Vietnamese profile README ([README.vi.md](README.vi.md))
- Expanded docs: architecture, glossary, comparison, SEO checklist, GitHub profile setup
- GitHub Actions: markdown link check, labeler
- Scripts to update repo About/topics via API
- Verified open-source catalog (real @multilogin-automation repos)

### Fixed

- Removed broken links to non-existent `multilogin-x-python-automation-sdk`, `playwright-selenium-templates`, and `postman-api-collection` repos
- Pointed quick start to `multilogin-automation` `/templates` and official MLX repos

### Added (hub v1.0)

- SEO-structured README, LICENSE (MIT), SECURITY, CODE_OF_CONDUCT, CONTRIBUTING
- docs: getting-started, open-source-catalog, faq
- GitHub issue/PR templates

[Unreleased]: https://github.com/Anti-detect/Anti-detect/compare/v1.1.1...HEAD
[1.1.1]: https://github.com/Anti-detect/Anti-detect/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/Anti-detect/Anti-detect/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Anti-detect/Anti-detect/releases/tag/v1.0.0
