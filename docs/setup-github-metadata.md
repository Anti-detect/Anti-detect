# One-time GitHub metadata setup

GitHub Actions **cannot** update repository About/topics with the default `GITHUB_TOKEN` on personal accounts. Choose **one** method below.

## Option A — Repository secret (automatic on every push)

1. Create a [classic PAT](https://github.com/settings/tokens) with scope **`repo`** (or fine-grained: Administration + Metadata on this repository).
2. In https://github.com/Anti-detect/Anti-detect/settings/secrets/actions → **New repository secret**
3. Name: `GH_METADATA_TOKEN` · Value: your PAT
4. Push to `main` or run workflow **Sync repository settings** manually.

Source of truth: [`.github/repo-metadata.json`](../.github/repo-metadata.json)

## Option B — PowerShell script (local)

```powershell
$env:GITHUB_TOKEN = "ghp_YOUR_PAT"
.\scripts\set-github-about.ps1
```

## Option C — GitHub UI (manual)

Copy from [seo-checklist.md](seo-checklist.md), [urls.md](urls.md), and [repo-metadata.json](../.github/repo-metadata.json):

- **Description:** Anti-detect browser fingerprinting hub: Multilogin X guides, stealth Playwright/Selenium templates, and browser profile automation docs.
- **Website:** Multilogin pricing URL in `homepage` field
- **Topics:** list in seo-checklist

## Verify

```powershell
(Invoke-RestMethod https://api.github.com/repos/Anti-detect/Anti-detect).description
(Invoke-RestMethod https://api.github.com/repos/Anti-detect/Anti-detect/topics -Headers @{Accept='application/vnd.github.mercy-preview+json'}).names
```

## Related

- [github-profile-setup.md](github-profile-setup.md) — social preview, pinned repos
- [Main README](../README.md)

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**

