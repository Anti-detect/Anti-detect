# SEO checklist (maintainers)

Use after every doc or catalog update.

## GitHub metadata

- [ ] About description ≤ 350 chars, starts with **anti-detect** or **browser fingerprinting**
- [ ] Website = `https://adblogin.com`
- [ ] 15–20 topics applied (no spam tags like `2027`, `draft`)
- [ ] Social preview image uploaded

## README.md

- [ ] Single H1 with primary keyword
- [ ] Primary keyword in first 100 words
- [ ] Table of contents for sections > 4
- [ ] All external links return 200 (CI workflow)
- [ ] Images have `alt` text
- [ ] FAQ uses question-style headings
- [ ] [README.vi.md](../README.vi.md) linked for Vietnamese SEO

## Topics (copy-paste)

```
anti-detect
browser-fingerprinting
browser-automation
multilogin
playwright
selenium
python
stealth
anti-bot
web-scraping
automation
fingerprint
headless-browser
mmo
profile-management
postman
api
devtools
testing
adblogin
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
- Telegram pin with `github.com/Anti-detect`
- Consistent anchor text: "Multilogin X automation", not "click here"

## Related

- [github-profile-setup.md](github-profile-setup.md)
