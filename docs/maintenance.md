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

After editing [README.md](../README.md), regenerate shorter locales from the English template:

```powershell
python scripts/expand-locale-readme.py
```

Fully translated locales (VI, ZH, RU, KO) are maintained manually. Re-run the script only for `th`, `id`, `pt-BR`, `es`, `ja` unless you merge manual translations back.

## Updating API archive safely

1. Save Postman pages temporarily into `API-HTML/`.
2. Run:

```powershell
python scripts/archive-postman-html.py
python scripts/check-spec-integrity.py
python scripts/build-api-catalog.py
```

3. Delete `API-HTML/` again (only `docs/multilogin-api/spec/` is long-term source of truth).

## CI guardrails

- `docs-ci.yml` (push + PR): branding guard, repo-link verify, markdown lint, Python compile, spec-integrity.
- `weekly-docs-verify.yml`: scheduled re-check + generated catalog drift warning.

## If integrity check fails

- Compare `docs/multilogin-api/spec/postman-collection-meta.json` and `launcher-endpoints.json`.
- Ensure every exported sample listed in metadata exists under `spec/code-samples/<language>/<variant>/`.
- Re-run `archive-postman-html.py` if metadata and sample folders diverged.
