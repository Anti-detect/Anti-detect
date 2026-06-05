# Recipe 04 — Multi-account rotation

## When to use

- **MMO**, marketplace, or ads workflows with **one MLX profile per account**.
- Same Python script, different `folder_id` / `profile_id` per row.
- Sequential rotation (safe default) before parallel fleet scaling.

## Pattern

```text
for each account in profiles.json:
    start profile
    attach automation (CDP port)
    run business logic
    stop profile  ← always, even on exception
```

## Profile list file

Copy [`profiles.example.json`](../../../sdk/python/recipes/profiles.example.json) → `profiles.json`:

```json
{
  "profiles": [
    {
      "label": "shop-account-1",
      "folder_id": "uuid-folder",
      "profile_id": "uuid-profile"
    }
  ]
}
```

Set `MLX_PROFILES_JSON` to your file path if not using the default beside the script.

## Runnable code

**Python:** [`sdk/python/recipes/04_batch_rotation.py`](../../../sdk/python/recipes/04_batch_rotation.py)

Replace `run_job()` with Playwright attach from [Recipe 02](02-playwright-attach.md).

## Operational rules

- **Never** share one profile across unrelated accounts.
- Align proxy country with profile timezone ([mmo-automation-guide.md](../../mmo-automation-guide.md)).
- Pilot 2–3 profiles before running hundreds.

## Scaling up

For parallel workers, run multiple machines or agents — each with its own launcher port and profile subset. Split `profiles.json` by worker ID.
