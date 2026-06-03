# Changelog

All notable documentation and hub changes for [Anti-detect/Anti-detect](https://github.com/Anti-detect/Anti-detect).

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

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

[Unreleased]: https://github.com/Anti-detect/Anti-detect/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/Anti-detect/Anti-detect/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Anti-detect/Anti-detect/releases/tag/v1.0.0
