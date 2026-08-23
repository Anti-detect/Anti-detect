# Maintenance workflow

Routine checklist to keep this repository stable as docs + SDK examples grow.

## Local pre-push flow

Run in repo root:

```powershell
python scripts/mlx-doctor.py
.\scripts\verify-docs.ps1
python scripts/check-spec-integrity.py
python scripts/parse-api-html.py
python scripts/build-api-catalog.py
python -m unittest discover -s sdk/python/tests -v
python -m py_compile sdk/python/mlx_client.py sdk/python/mlx_cli.py sdk/python/profile_catalog.py sdk/python/requests/*.py sdk/python/http_client/*.py scripts/*.py
```

## Locale README sync

After editing [README.md](../README.md), sync promo blocks manually across `README.*.md` (fully translated locales). `expand-locale-readme.py` only regenerates English shells — prefer hand edits for VI, ZH, RU, KO, TH, ID, PT-BR, ES, JA.

## Affiliate CTAs

Every `docs/**/*.md` and `sdk/**/*.md` must include **`SAAS50`**, **`MIN50`**, and the [pricing URL](urls.md). CI enforces this.

```powershell
python scripts/inject-affiliate-cta.py
```

Placement guide: [pricing-cta.md](pricing-cta.md). No changelog — this hub does not track commit history.

## Updating API archive safely

1. Save Postman pages temporarily into `API-HTML/`.
2. Run:

```powershell
python scripts/archive-postman-html.py
python scripts/check-spec-integrity.py
python scripts/build-api-catalog.py
```

1. Delete `API-HTML/` again (only `docs/multilogin-api/spec/` is long-term source of truth).

## CI guardrails

- `docs-ci.yml` (push + PR): branding guard, repo-link verify, markdown lint, Python compile, spec-integrity.
- `weekly-docs-verify.yml`: scheduled re-check + generated catalog drift warning.

## If integrity check fails

- Compare `docs/multilogin-api/spec/postman-collection-meta.json` and `launcher-endpoints.json`.
- Ensure every exported sample listed in metadata exists under `spec/code-samples/<language>/<variant>/`.
- Re-run `archive-postman-html.py` if metadata and sample folders diverged.

---

**Start with Multilogin X for free:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · paid plans from $7.08/mo · codes **`SAAS50`** · **`MIN50`**

