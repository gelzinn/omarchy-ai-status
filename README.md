# Omarchy AI Status

<img width="348" height="954" alt="Screenshot" src="https://github.com/user-attachments/assets/dcba0b97-d462-452e-b1b6-000cc445b803" />

A Waybar module designed for the Omarchy environment that monitors and displays the usage limits and status of various AI coding assistants and API providers in real-time.

## Features

- **Real-time Monitoring** -- Tracks multiple API providers.
- **Visuals** -- Uses smooth alpha-based pulsing animations and Braille spinners to present an elegant loading UI directly in your Waybar.
- **Modular Provider Architecture** -- Each provider is handled independently, allowing seamless addition of new tools.
- **Inter-process Synchronization** -- A central Python daemon runs persistently without bogging down your system, utilizing a file-based lock and PID registration to coordinate on-click manual refreshes reliably.

## Repository Structure

- `src/bin/waybar-ai-status` -- The single entry point CLI to run the daemon or trigger a refresh.
- `src/core/` -- The core Python package containing separated logic (rendering, state, data fetching, daemon).
- `src/providers/` -- Directory containing specific query and parsing logic for each distinct AI service (e.g., Claude, Copilot, Z.AI, Codex).

## Requirements & Supported Providers

Most of the scripts read credentials stored by `opencode`, `antigravity`, or other specific auth formats.

Check out the [Providers & Authentication Guide](PROVIDERS.md) to understand exactly how each provider gets its data, where you need to configure your tokens, and known API behaviors (like Gemini's reset time limitations).

## Setup

Run the install script:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/gelzinn/omarchy-ai-status/main/install.sh)
```

Or if you have the repo cloned:

```bash
./install.sh
```

Running the same command again will update to the latest version and restart Waybar automatically.

Then add the module to your `config.jsonc` in Waybar:

```jsonc
"custom/ai-status": {
    "format": "{}",
    "return-type": "json",
    "exec": "~/.local/bin/waybar-ai-status daemon",
    "on-click": "~/.local/bin/waybar-ai-status refresh",
    "tooltip": true
}
```

## Security

This repository does **not** contain any API keys or personal session cookies.

The provider scripts are configured to dynamically read these from your existing local authentication JSON files.
