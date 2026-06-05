# SEO checklist (maintainers)

Use after every doc or catalog update.

## GitHub metadata

Source of truth: [`.github/repo-metadata.json`](../.github/repo-metadata.json) (synced by `sync-repo-settings.yml` on push to `main`).

- [ ] About description ≤ 350 chars, starts with **anti-detect** or **browser fingerprinting**
- [ ] Website = Multilogin pricing URL (see `repo-metadata.json` → `homepage`)
- [ ] **Exactly ≤ 20** GitHub topics (API limit); see `repo-metadata.json`
- [ ] Social preview image uploaded (UI only — not automatable without image asset)

## README.md

- [ ] Single H1 with primary keyword
- [ ] Primary keyword in first 100 words
- [ ] Table of contents for sections > 4
- [ ] All external links return 200 (CI workflow)
- [ ] Images have `alt` text
- [ ] FAQ uses question-style headings
- [ ] Localized READMEs linked: VI, ZH, RU, ID, PT-BR, KO, JA, TH, ES ([locales.md](locales.md))
- [ ] MMO guide + Playwright integration docs linked from main README
- [ ] [urls.md](urls.md) matches all README pricing links
- [ ] [browser-landscape.md](browser-landscape.md) uses neutral competitor keywords (no disparagement)

## Topics (copy-paste)

```
anti-detect
antidetect-browser
browser-fingerprinting
fingerprint-browser
browser-automation
multilogin
multilogin-x
playwright
selenium
puppeteer
python
stealth
anti-bot
web-scraping
headless-browser
browser-profiles
profile-management
undetectable-browser
mmo
account-management
```

## Internal linking

- [ ] New doc linked from [docs/README.md](README.md)
- [ ] Internal links point to paths in this repo ([repository-map.md](repository-map.md))
- [ ] No links to external third-party kit organizations (CI enforces self-contained docs)

## Freshness signals

- [ ] Update [CHANGELOG.md](../CHANGELOG.md) on meaningful doc changes
- [ ] Bump "Last reviewed" in catalog when verifying links

## Off-GitHub promotion (optional)

- Dev.to / Medium article linking to this profile
- Consistent anchor text: "Multilogin X automation", not "click here"

## Related

- [github-profile-setup.md](github-profile-setup.md)
- [Main README](../README.md)
