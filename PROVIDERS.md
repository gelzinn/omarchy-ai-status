# Providers & Authentication Guide

This document explains the authentication requirements and specific behaviors for the AI providers supported by **Omarchy AI Status**.

Our architecture ensures that **no API keys are hardcoded in the scripts**. Instead, they read tokens from your secure local configuration files.

## OpenCode (Go) & General OpenAI Compatible

- **Config file**: `~/.local/share/opencode/auth.json` (or your specific auth file).
- **Requirements**: The `query.sh` script will parse this JSON to extract your `access` tokens. Make sure your environment is properly authenticated with OpenCode.
- **Behavior**: Retrieves detailed metrics based on OpenCode's API standard.

## Gemini (via Antigravity CLI)

- **Config file**: Handled entirely by the Antigravity CLI environment.
- **Requirements**: You must be logged into Antigravity so the CLI can query Gemini's status.
- **Known Behavior**: The Gemini API retrieved via Antigravity **does not return reset times** for all usage periods. If you notice that some periods don't show a "Resets in X hours" label, this is a limitation of the API data provided, not a bug in the status bar rendering.

## Claude / Anthropic

- **Config file**: Often shares the `auth.json` format, or specific Anthropic config files.
- **Requirements**: Requires a valid token to query `https://api.anthropic.com/api/oauth/usage`.
- **Behavior**: Returns highly precise `remainingFraction` values and accurate `resetTime` values.

## Other Providers (Z.AI, Codex, Copilot, etc.)

Each provider inside `src/providers/<name>/` has a [`query.sh`](src/providers/) and a [`parse.py`](src/providers/) file. The `query.sh` fetches the raw data, and the `parse.py` formats it into a standardized JSON structure. If a provider is showing as "API unreachable" or 0%, check its specific `query.sh` file to see which local authentication file it is attempting to read (usually `~/.local/share/.../auth.json` or `~/.config/.../tokens.json`).

## Tip

Want to change how a provider formats its data? Check out its [`parse.py`](src/providers/) file. See the [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
