Kiro is read through its own CLI, **`kiro-cli`**. AI Status shells out to it (`kiro-cli chat /usage`) and parses the result — so as long as `kiro-cli` is installed and signed in, there's nothing else to configure.

## Requirements

- **`kiro-cli`** installed and on your `PATH`
- A signed-in Kiro account (so `kiro-cli whoami` succeeds)

## Step 1 — Install and sign in to `kiro-cli`

Install the Kiro CLI and log in. You can confirm you're authenticated with:

```bash
kiro-cli whoami --format json
```

If that prints your account, AI Status is good to go — it runs `kiro-cli chat --no-interactive /usage` under the hood.

## Step 2 — Enable it in AI Status

Right-click the AI Status module to open the config TUI, make sure **Kiro** is enabled, then left-click to refresh.

## What it tracks

Your usage percentage and its reset timer.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Shows nothing | `kiro-cli` isn't installed or isn't on `PATH` — install it and check `command -v kiro-cli`. |
| Still blank | You're not signed in — `kiro-cli whoami --format json` should return your account; log in if it doesn't. |
| Slow to update | The CLI is queried on each refresh; a slow `kiro-cli` response delays the update. |

Run the provider's fetch script by hand to see the raw output:

```bash
bash ~/.local/share/ai-status/packages/lib/src/providers/kiro/query.sh
```
