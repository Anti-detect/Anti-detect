# Multilogin X API spec (archived)

Professional archive migrated from `API-HTML/` Postman Save-Page exports on **2026-06-04**.

**Source of truth** for maintainers and scripts — safe to delete `API-HTML/` after this exists in git.

## Files

| File | Purpose |
|------|---------|
| [postman-collection-meta.json](postman-collection-meta.json) | Categories, auth, bases, export manifest |
| [launcher-endpoints.json](launcher-endpoints.json) | Canonical Launcher paths |
| [code-samples/](code-samples/) | Extracted Postman code blocks per language |

## Live doc (always newer)

https://documenter.getpostman.com/view/28533318/2s946h9Cv9

## Re-archive after new HTML save

```bash
# Drop new *.html into API-HTML/, then:
python scripts/archive-postman-html.py
python scripts/build-api-catalog.py
# Delete API-HTML/ again if desired
```

## Runnable SDK

Curated scripts (not raw blocks): [`sdk/`](../../../sdk/)
