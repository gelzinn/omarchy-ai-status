Antigravity doesn't expose a usage API, so AI Status reads it the same way you would in a terminal: it drives the **`agy`** CLI through a pseudo-terminal, sends `/usage`, and parses the quota output. All you need is the `agy` CLI installed and logged in.

> Because it scripts an interactive CLI, this provider is a little slower to refresh than the API-based ones, and Gemini's data may not include reset timers for every window — a limitation of the CLI's output.

## Requirements

- The **Antigravity CLI (`agy`)** installed and on your `PATH`
- A signed-in `agy` session

## Step 1 — Install and sign in to `agy`

Install the Antigravity CLI. On first run, `agy` opens a browser-based login — complete it once:

```bash
agy
```

After you're signed in, launching `agy` drops you at the `Welcome to the Antigravity CLI` prompt. That's exactly what AI Status automates (it sends `/usage` and reads the response).

## Step 2 — Enable it in AI Status

Right-click the AI Status module to open the config TUI, make sure **Antigravity** is enabled, then left-click to refresh. Give it a few seconds — driving the CLI takes longer than a plain API call.

## What it tracks

A **weekly** limit and a **5-hour** rolling limit for each model group — Gemini and Claude/GPT.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Shows nothing | `agy` isn't installed or on `PATH` — install it and check `command -v agy`. |
| Blank / times out | You're not signed in, or the CLI didn't reach the `/usage` output within ~15s. Run `agy` yourself, sign in, and try `/usage` manually. |
| Missing reset times (Gemini) | Expected — the CLI doesn't report reset timers for every Gemini window. |

Run the provider's fetch script by hand to see the raw output:

```bash
python3 ~/.local/share/ai-status/packages/lib/src/providers/antigravity/query.py
```
