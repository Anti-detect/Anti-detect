# SEO checklist (maintainers)

Use after every doc or catalog update.

## GitHub metadata

Source of truth: [`.github/repo-metadata.json`](../.github/repo-metadata.json) (synced by `sync-repo-settings.yml` on push to `main`).

- [ ] About description ≤ 350 chars, starts with **anti-detect** or **browser fingerprinting**
- [ ] Website = Multilogin pricing URL (see `repo-metadata.json` → `homepage`)
- [ ] 18–21 topics applied (no spam tags like `2027`, `draft`)
- [ ] Social preview image uploaded (UI only — not automatable without image asset)

## README.md

- [ ] Single H1 with primary keyword
- [ ] Primary keyword in first 100 words
- [ ] Table of contents for sections > 4
- [ ] All external links return 200 (CI workflow)
- [ ] Images have `alt` text
- [ ] FAQ uses question-style headings
- [ ] Localized READMEs linked: VI, ZH, RU, ID, PT-BR

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
automation
fingerprint
headless-browser
browser-profiles
profile-management
undetectable-browser
mmo
```

## Internal linking

- [ ] New doc linked from [docs/README.md](README.md)
- [ ] Catalog lists only **existing** repos (verify via GitHub API)
- [ ] Broken kit URLs removed or redirected to `multilogin-automation`

## Freshness signals

- [ ] Update [CHANGELOG.md](../CHANGELOG.md) on meaningful doc changes
- [ ] Bump "Last reviewed" in catalog when verifying links

## Off-GitHub promotion (optional)

- Dev.to / Medium article linking to this profile
- Consistent anchor text: "Multilogin X automation", not "click here"

## Related

- [github-profile-setup.md](github-profile-setup.md)
- [Main README](../README.md)
